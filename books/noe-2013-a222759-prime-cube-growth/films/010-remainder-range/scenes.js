'use strict';

const primeFilmTitle = (title, subtitle) => {
  txt(title, W / 2, 190, {size: 66, fam: F.orb, w: 900, align: 'center', c: C.white});
  txt(subtitle, W / 2, 270, {size: 34, fam: F.zh, align: 'center', c: C.cyan});
};

const primeFilmLabel = (label, x, y, alpha = 1, colour = C.white, size = 42) => {
  txt(label, x, y, {size, fam: F.mono, w: 700, align: 'center', c: colour, a: alpha});
};

SCENES.range = scene => {
  primeFilmTitle('A REMAINDER HAS A CEILING', '余数不能达到除数');
  primeFilmLabel('choose(16, 2) = 120', W / 2, 390, 1, C.white, 50);
  const visible = at(scene, 1, 0.6);
  for (let value = 0; value < 8; value += 1) {
    const x = W / 2 + 115 * (value - 4);
    panel(x - 47, 500, 94, 100, visible, value === 0 ? C.cyan : C.white, '');
    primeFilmLabel(String(value), x, 568, visible, value === 0 ? C.cyan : C.white);
  }
  primeFilmLabel('8', W / 2 + 460, 568, visible, C.now);
  primeFilmLabel('120 mod 8 = 0', W / 2, 730, visible, C.cyan, 46);
  primeFilmLabel('prime cube ≤ n  ⇒  remainder ≠ n', W / 2, 820, at(scene, 2, 0.6), C.now, 36);
};

SCENES.corrections = scene => {
  primeFilmTitle('WHEN THE INPUT FITS', '当输入落在余数范围内');
  primeFilmLabel('p ≥ 5,  n < p³  ⇒  remainder = n', W / 2, 406, 1, C.cyan, 46);
  const visible = at(scene, 1, 0.55);
  panel(W / 2 - 660, 510, 620, 210, visible, C.now, 'EXTRA 2');
  panel(W / 2 + 40, 510, 620, 210, visible, C.now, 'EXTRA 3');
  primeFilmLabel('n < 8', W / 2 - 350, 600, visible, C.white);
  primeFilmLabel('n mod 4 = 2 or 3', W / 2 - 350, 670, visible, C.white, 32);
  primeFilmLabel('n < 27', W / 2 + 350, 600, visible, C.white);
  primeFilmLabel('n mod 3 = 2', W / 2 + 350, 670, visible, C.white, 32);
};

SCENES.threshold = scene => {
  primeFilmTitle('THE STEP AT 125', '第三个例外在 125 出现');
  const after = at(scene, 1, 0.65);
  panel(W / 2 - 620, 400, 540, 310, 1, C.cyan, 'n = 124');
  panel(W / 2 + 80, 400, 540, 310, after, C.now, 'n = 125');
  primeFilmLabel('2³, 3³', W / 2 - 350, 550, 1, C.white, 54);
  primeFilmLabel('2³, 3³, 5³', W / 2 + 350, 550, after, C.white, 54);
  primeFilmLabel('2 exceptions', W / 2 - 350, 643, 1, C.cyan, 36);
  primeFilmLabel('3 exceptions', W / 2 + 350, 643, after, C.now, 36);
  primeFilmLabel('125 sharp  ·  691 sufficient', W / 2, 815, at(scene, 2, 0.6), C.white, 37);
};

SCENES.scope = () => {
  primeFilmTitle('SUFFICIENT IS NOT SHARP', '充分条件不是准确门槛');
  primeFilmLabel('Noe: the nested prime bound gives witnesses', W / 2, 420, 1, C.cyan, 34);
  primeFilmLabel('Ma & Zhang: the cube bound is exact for k ≥ 3', W / 2, 545, 1, C.white, 34);
  primeFilmLabel('OEIS A222759  ·  doi:10.5281/zenodo.24405795', W / 2, 775, 1, C.white, 26);
};
