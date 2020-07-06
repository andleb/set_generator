# -*- coding: utf-8 -*-
"""
@author: Andrej Leban
#@Filename : OG_reviews.py
#@Date : 2020-07-06-19-02
"""

from dataclasses import dataclass
import enum


class QV(enum.Enum):
    Quant = enum.auto
    Verbal = enum.auto


class Diff(enum.Enum):
    Easy = enum.auto
    Medium = enum.auto
    Hard = enum.auto


class PSDS(enum.Enum):
    PS = enum.auto
    DS = enum.auto
    NA = None


@dataclass(init=True)
class Problem:
    qv: QV
    num: int
    psds: PSDS
    diff: Diff


### DATA
# Here I am following the OG classification

Algebra = {
    "Applied"  : [Problem(QV.Quant, 198, PSDS.DS, Diff.Easy)] +
                 [Problem(QV.Quant, n, PSDS.PS, Diff.Easy)
                  for n in (49, 19)] +
                 [Problem(QV.Quant, n, PSDS.DS, Diff.Medium)
                  for n in (226, 238)],
    "Abs"      : [Problem(QV.Quant, n, PSDS.DS, Diff.Medium)
                  for n in (230, 239)],
    "Eqs"      : [Problem(QV.Quant, 202, PSDS.DS, Diff.Easy)],
    "Exp"      : [Problem(QV.Quant, 186, PSDS.DS, Diff.Easy)] +
                 [Problem(QV.Quant, n, PSDS.PS, Diff.Easy)
                  for n in (42, 45)],
    "Factoring": [Problem(QV.Quant, 3, PSDS.PS, Diff.Easy)] +
                 [Problem(QV.Quant, 247, PSDS.DS, Diff.Medium)],
    "1stDgEq"  : [Problem(QV.Quant, n, PSDS.DS, Diff.Easy)
                  for n in (177, 204, 208)] +
                 [Problem(QV.Quant, n, PSDS.PS, Diff.Easy)
                  for n in (10, 16, 31, 44, 41)],
    "Fractions": [Problem(QV.Quant, 27, PSDS.PS, Diff.Easy)],
    "InEq"     : [Problem(QV.Quant, 181, PSDS.DS, Diff.Easy),
                  Problem(QV.Quant, 9, PSDS.PS, Diff.Easy)] +
                 [Problem(QV.Quant, n, PSDS.DS, Diff.Medium) for n in (240, 251)],
    "Opint"    : [Problem(QV.Quant, 7, PSDS.PS, Diff.Easy)],
    "Oprat"    : [Problem(QV.Quant, 25, PSDS.PS, Diff.Easy),
                  Problem(QV.Quant, 231, PSDS.DS, Diff.Medium)],
    "Order"    : [Problem(QV.Quant, 18, PSDS.PS, Diff.Easy)],
    "LinEq"    : [Problem(QV.Quant, 199, PSDS.DS, Diff.Easy)],
    "Percents" : [Problem(QV.Quant, 209, PSDS.DS, Diff.Easy),
                  Problem(QV.Quant, 61, PSDS.DS, Diff.Easy)],
    "Ratio"    : [Problem(QV.Quant, 55, PSDS.PS, Diff.Easy)],
    "2ndDgEq"  : [Problem(QV.Quant, n, PSDS.PS, Diff.Easy) for n in (2, 26, 56)] +
                 [Problem(QV.Quant, 252, PSDS.DS, Diff.Medium)],
    "Seqs"     : [Problem(QV.Quant, 250, PSDS.DS, Diff.Medium)],
    "SimEq"    : [Problem(QV.Quant, 207, PSDS.DS, Diff.Easy),
                  Problem(QV.Quant, 234, PSDS.DS, Diff.Medium)],],
    "Simplify" : [Problem(QV.Quant, 28, PSDS.PS, Diff.Easy)],
    "Stats"    : [Problem(QV.Quant, 72, PSDS.PS, Diff.Easy)]
}
