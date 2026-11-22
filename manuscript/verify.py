import argparse
import hashlib
import json
from math import comb, factorial, gcd, isqrt
from pathlib import Path
from urllib.request import Request, urlopen


def primes_through(limit):
    candidates = bytearray(b'\x01') * (limit + 1)
    candidates[:2] = b'\x00\x00'
    for divisor in range(2, isqrt(limit) + 1):
        if candidates[divisor]:
            start = divisor * divisor
            candidates[start:limit + 1:divisor] = b'\x00' * ((limit - start) // divisor + 1)
    return [value for value, prime in enumerate(candidates) if prime]


def witness_set(number, primes):
    witnesses = {prime for prime in primes if prime ** 3 <= number}
    if number < 8 and number % 4 in (2, 3):
        witnesses.add(2)
    if number < 27 and number % 3 == 2:
        witnesses.add(3)
    return witnesses


def predicted_witness(number, prime, exponent):
    if exponent < 3:
        return prime ** exponent <= number
    return prime in witness_set(number, [prime])


def load_oeis(sequence, directory):
    filename = 'b' + sequence[1:] + '.txt'
    url = 'https://oeis.org/' + sequence + '/' + filename
    if directory is None:
        request = Request(url, headers={'User-Agent': 'prime-cube-counts/1.0 (research table verification)',
                                        'Accept': 'text/plain'})
        with urlopen(request, timeout=45) as response:
            content = response.read(2 * 1024 * 1024 + 1)
        assert len(content) <= 2 * 1024 * 1024
    else:
        content = (directory / filename).read_bytes()
    entries = {}
    for line in content.decode('utf-8').splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            index, value = map(int, line.split())
            assert index not in entries
            entries[index] = value
    assert set(range(1, 10001)) <= entries.keys()
    return entries, {'sequence': sequence, 'url': url,
                     'sha256': hashlib.sha256(content).hexdigest(), 'terms_compared': 10000}


def linked_checks(primes):
    coefficient_limit = 512
    coefficients = [0] * (coefficient_limit + 1)
    for prime in primes:
        if prime ** 3 > coefficient_limit:
            break
        for number in range(prime ** 3, coefficient_limit + 1):
            coefficients[number] += 1
    for number in (2, 3, 6, 7):
        coefficients[number] += 1
    for number in range(2, 27, 3):
        coefficients[number] += 1
    least_common_multiple = 1
    for number in range(1, coefficient_limit + 1):
        assert coefficients[number] == len(witness_set(number, primes))
        least_common_multiple = least_common_multiple * number // gcd(least_common_multiple, number)
        for exponent in (1, 2, 3):
            expected = sum(prime ** exponent <= number for prime in primes)
            actual = sum(least_common_multiple % (prime ** exponent) == 0
                         for prime in primes if prime <= number)
            assert actual == expected
        three_divisors = sum(sum(value % divisor == 0 for divisor in range(1, value + 1)) == 3
                             for value in range(1, number + 1))
        assert three_divisors == sum(prime ** 2 <= number for prime in primes)
    coprime_maxima = []
    for limit in range(1, 65):
        states = {0: 0}
        for value in range(4, limit + 1):
            if value in primes:
                continue
            factors = sum(1 << index for index, prime in enumerate(primes)
                          if prime <= value and value % prime == 0)
            updated = dict(states)
            for used, size in states.items():
                if used & factors == 0:
                    union = used | factors
                    updated[union] = max(updated.get(union, 0), size + 1)
            states = updated
        maximum = max(states.values())
        assert maximum == sum(prime ** 2 <= limit for prime in primes)
        coprime_maxima.append(maximum)
    for number in range(1, 129):
        value = factorial(number)
        actual = sum(value % prime == 0 for prime in primes if prime <= number)
        expected = sum(prime <= number for prime in primes)
        assert actual == expected
        partitions = sum(smaller in primes for smaller in range(1, number + 1))
        assert partitions == expected
    return {
        'generating_function_coefficients': {'n_min': 1, 'n_max': coefficient_limit},
        'lcm_exponent_interpretations': {'n_min': 1, 'n_max': coefficient_limit,
                                        'exponents': [1, 2, 3]},
        'three_divisor_interpretation': {'n_min': 1, 'n_max': coefficient_limit},
        'pairwise_coprime_composite_maximum': {
            'n_min': 1, 'n_max': 64,
            'method': 'exhaustive dynamic programming over disjoint prime-factor masks',
            'maxima': coprime_maxima},
        'factorial_factors_and_two_part_partitions': {'n_min': 1, 'n_max': 128}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--oeis-directory', type=Path)
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    primes = primes_through(10000)
    small_primes = [prime for prime in primes if prime <= 97]
    comparisons = 0
    for number in range(1, 513):
        for prime in small_primes:
            coefficient = comb(number * prime, prime)
            for exponent in (1, 2, 3):
                actual = coefficient % (prime ** exponent) != number
                expected = predicted_witness(number, prime, exponent)
                assert actual == expected, (number, prime, exponent, actual, expected)
                comparisons += 1
    original_comparisons = 0
    for number in range(1, 88):
        bad = {prime for prime in primes[:100]
               if comb(number * prime, prime) % (prime ** 3) != number}
        assert bad == witness_set(number, primes)
        original_comparisons += 100
    metadata = []
    counts, description = load_oeis('A222759', arguments.oeis_directory)
    metadata.append(description)
    terminal, description = load_oeis('A222760', arguments.oeis_directory)
    metadata.append(description)
    for number in range(1, 10001):
        bad = witness_set(number, primes)
        assert len(bad) == counts[number], (number, bad, counts[number])
        maximum = max(bad, default=1)
        first_good_tail = next(prime for prime in primes if prime > maximum)
        assert first_good_tail == terminal[number], (number, first_good_tail, terminal[number])
        predicted_companion = 5 if number == 5 else primes[len(bad)]
        assert first_good_tail == predicted_companion
        assert (len(bad) >= 1) == (number not in (1, 4))
        assert (len(bad) >= 2) == (number >= 27 or number in (2, 8, 11, 14, 17, 20, 23, 26))
    siblings = linked_checks(primes)
    checked_thresholds = []
    for index in range(3, 9):
        prime = primes[index - 1]
        boundary = prime ** 3
        assert len(witness_set(boundary - 1, primes)) == index - 1
        assert len(witness_set(boundary, primes)) == index
        checked_thresholds.append({'k': index, 'prime': prime, 'sharp_threshold': boundary})
    for exponent in range(4, 13):
        assert comb(10, 5) % (5 ** exponent) == 252
    summary = {
        'status': 'pass',
        'integer_binomial_checks': {
            'n_min': 1, 'n_max': 512, 'primes': small_primes,
            'exponents': [1, 2, 3], 'comparisons': comparisons,
            'method': 'math.comb followed by exact integer remainder'},
        'original_mathematica_range': {
            'n_min': 1, 'n_max': 87, 'first_primes': 100,
            'comparisons': original_comparisons, 'method': 'math.comb'},
        'oeis_comparisons': metadata,
        'sharp_threshold_checks': checked_thresholds,
        'higher_power_obstruction': {
            'source_status': 'uniform higher-power assertion not asserted in the source',
            'n': 2, 'p': 5, 'binomial': 252, 'checked_exponents': list(range(4, 13)),
            'all_exponents_argument': '252 < 5^4 <= 5^e for every integer e >= 4'},
        'sibling_checks': siblings,
        'small_count_levels_and_companion_relation': {'n_min': 1, 'n_max': 10000},
        'coverage': {
            'written_proofs': ['finite witness set', 'exact count', 'sharp growth threshold',
                               'least eventual good prime', 'modulus p and p^2 counts',
                               'all small count levels', 'companion relation except n=5',
                               'linked elementary interpretations and generating functions',
                               'prime-number-theorem consequences'],
            'lean_declaration': 'D5.S3.Arith.PrimeRemainders.OeisA222759Growth.result',
            'lean_statement': 'k >= 3 and n >= p_(p_k^3) imply k distinct prime witnesses',
            'finite_checks': 'the displayed finite ranges'}}
    output = json.dumps(summary, indent=2, sort_keys=True) + '\n'
    if arguments.output:
        arguments.output.write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
