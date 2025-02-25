# -*- coding: utf-8 -*-
from kss._modules.hangulization.hangulize import *


class Latin(Language):
    """For transcribing Latin."""

    __iso639__ = {1: 'la', 2: 'lat', 3: 'lat'}
    __tmp__ = ',;%'

    vowels = u'aeëiouüy'
    vl = 'cfpst'
    so = 'lmnr'
    notation = Notation([
        (u'æ', 'ae'),
        (u'œ', 'oe'),
        ('maior', 'maJor'),
        ('traian', 'traJan'),
        (u'{@}ë', '%e'),
        (u'ë', 'e'),
        (u'ü{@}', 'u%'),
        (u'ü', 'u'),
        ('jj', 'j'),
        ('^j{@}', 'J'),
        ('{@}j{@}', 'J'),
        ('j', 'i'),
        ('^i{@}', 'J'),
        ('^iv{@}', 'iV'),
        ('^iv', 'Ju'),
        ('w', 'V'),
        ('qv{@}', 'qu'),
        ('qu{a|e|i}', 'cW'),
        ('q', 'c'),
        ('gu{a|e|i}', 'gW'),
        ('^u{@}', 'V'),
        ('^v{@}', 'V'),
        ('{@}l', 'lQ'),
        ('{@}m', 'mQ'),
        ('{@}n', 'nQ'),
        ('{@}r', 'rQ'),
        ('{@|Q}u{@}', 'V'),
        ('{@|Q}v{@}', 'V'),
        ('Q', None),
        ('vv{@}', 'uV'),
        ('v', 'u'),
        ('y', 'i'),
        ('{a|o}e', 'i'),
        ('bb', 'b'),
        ('k', 'c'),
        ('xx', 'x'),
        ('x', 'cs'),
        ('cc', 'c'),
        ('dd', 'd'),
        ('ff', 'f'),
        ('gg', 'g'),
        ('hh', 'h'),
        ('ll', 'l'),
        ('{@}mm{@}', 'm,m'),
        ('{@}nn{@}', 'n,n'),
        ('pp', 'p'),
        ('rr', 'r'),
        ('ss', 's'),
        ('tt', 't'),
        ('zz', 'z'),
        ('{c|p|t}h', None),
        ('n{c|g}', 'N'),
        ('{@}b{s|t}', 'p,'),
        ('{@}c{<vl>}', 'c,'),
        ('{@}p{<vl>}', 'p,'),
        ('^l', 'l;'),
        ('^m', 'm;'),
        ('^n', 'n;'),
        ('l$', 'l,'),
        ('m$', 'm,'),
        ('n$', 'n,'),
        ('l{@|m,|n,}', 'l;'),
        ('{,}l', 'l;'),
        ('m{@}', 'm;'),
        ('n{@}', 'n;'),
        ('l', 'l,'),
        ('m', 'm,'),
        ('n', 'n,'),
        (',,', ','),
        (',;', None),
        (',l,', 'l,'),
        (',m,', 'm,'),
        (',n,', 'n,'),
        ('l{m;|n;}', 'l,'),
        (';', None),
        ('b', Choseong(B)),
        ('c,', Jongseong(G)),
        ('c', Choseong(K)),
        ('d', Choseong(D)),
        ('f', Choseong(P)),
        ('g', Choseong(G)),
        ('h', Choseong(H)),
        ('^l', Choseong(L)),
        ('{,}l', Choseong(L)),
        ('l,', Jongseong(L)),
        ('l', Jongseong(L), Choseong(L)),
        ('m,', Jongseong(M)),
        ('m', Choseong(M)),
        ('n,', Jongseong(N)),
        ('n', Choseong(N)),
        ('N', Jongseong(NG)),
        ('p,', Jongseong(B)),
        ('p', Choseong(P)),
        ('r', Choseong(L)),
        ('s', Choseong(S)),
        ('t', Choseong(T)),
        ('V', Choseong(B)),
        ('z', Choseong(J)),
        ('Ja', Jungseong(YA)),
        ('Je', Jungseong(YE)),
        ('Ji', Jungseong(I)),
        ('Jo', Jungseong(YO)),
        ('Ju', Jungseong(YU)),
        ('Wa', Jungseong(WA)),
        ('We', Jungseong(WE)),
        ('Wi', Jungseong(WI)),
        ('a', Jungseong(A)),
        ('e', Jungseong(E)),
        ('i', Jungseong(I)),
        ('o', Jungseong(O)),
        ('u', Jungseong(U)),
    ])

    def normalize(self, string):
        additional = {u'Ë': u'ë', u'Ü': u'ü', u'Æ': u'æ', u'Œ': u'œ'}
        return normalize_roman(string, additional)


__lang__ = Latin
