# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:50:12 2019

@author: Andrej Leban
"""

import itertools as it
import numpy as np

# TODO:
#      * easy, med, hard

### IGNORE SET
import json
with open("ignored.json", 'r') as f:
    _ignored = set()
    for el in json.load(f):
        # typing
        try:
            _ignored.add(int(el))
        except ValueError:
            _ignored.add(el)

with open("ignored_extra.json", 'r') as f:
    _ignored_extra = set()
    for el in json.load(f):
        _ignored_extra.add(el)

from dicts2020 import *

_tot = {
        "FDPs": FDPs,
        "Algebra": Algebra,
        "WP": WP,
        "Geometry": Geometry,
        "NumProp": NumProp,
        "CR": CR,
        "RC": RC,
        "SC": SC
        }
_quant = {"FDPs", "Algebra", "WP", "Geometry", "NumProp"}
_verb = {"CR", "RC", "SC"}


def generate_set(nProb: int, qvb='b', cats=frozenset(), subcats=frozenset(),
                 psds='b', **kwargs):
    """
    OG problem set builder for all but RC problems.

    :param nProb: the total number of problems
    :param qvb: 'q' - quant, 'v' - verbal, 'b' - both
    :param cats: categories within quant and verbal
    :param subcats: sub-categories within the above categories
    :param psds: 'p' - problem solving, 'd' - data sufficiency, 'b' - both
    :param kwargs:
    :return: a list of problem numbers generated
    """

    def build_quant():
        source = []

        if not len(cats):
            newCats = _quant
        else:
            newCats = cats

        for cat in newCats:
            if cat not in _quant:
                continue

            # all the subcats
            if not len(subcats):
                if psds == 'p':
                    newSubcats = tuple(_tot[cat]["PS"].keys())
                elif psds == 'd':
                    newSubcats = tuple(_tot[cat]["DS"].keys())
                else:
                    newSubcats = set(list(_tot[cat]["PS"].keys()) +
                                     list(_tot[cat]["DS"].keys()))
            else:
                newSubcats = subcats

            for subcat in newSubcats:
                if psds == 'p':
                    source += _tot[cat]["PS"][subcat]
                elif psds == 'd':
                    source += _tot[cat]["DS"][subcat]
                else:
                    # not a given that they share all the subcats
                    try:
                        source += _tot[cat]["PS"][subcat]
                    except KeyError:
                        pass
                    try:
                        source += _tot[cat]["DS"][subcat]
                    except KeyError:
                        pass
        return source

    def build_verbal():

        source = []
        if psds != 'b':
            raise RuntimeError("PS/DS split only makes sense for"
                               "quant problems!")
        if not len(cats):
            newCats = _verb
        else:
            newCats = cats

        for cat in newCats:
            if cat not in _verb:
                continue

            # all the subcats
            if not len(subcats):
                newSubcats = tuple(_tot[cat].keys())
            else:
                newSubcats = subcats

            for subcat in newSubcats:
                source += _tot[cat][subcat]

        return source

    # to help the IDE, declare the var
    source = None

    if qvb == 'q':
        source = build_quant()

    elif qvb == 'v':
        source = build_verbal()

    elif qvb == 'b':
        source = build_quant() + build_verbal()

    source = list(filter(lambda el: el not in _ignored, source))

    while nProb >= 1:
        try:
            ret = sorted(np.array(source)
                         [sorted(np.random.choice(len(source), (nProb,),
                                                  replace=False))])
            break

        except ValueError:
            nProb -= 1

    if nProb < 1:
        raise RuntimeError("Seems you've run out of problems for the selected"
                           "categories:" + str(cats) + ": " + str(subcats))
    # typing
    for i in range(len(ret)):
        try:
            ret[i] = int(ret[i])
        except ValueError:
            ret[i] = ret[i]

    return sorted(filter(lambda el: not isinstance(el, int), ret)) +\
        sorted(filter(lambda el: isinstance(el, int), ret))


def generate_extraSimple(nProb: int, qvb='b', psds='b', rc=False):
    """
    """

    candsQ, candsV = [], []

    if qvb == 'q':
        if psds == 'ps':
            candsQ = [i for i in generate_extraSimple.ps]
        elif psds == 'ds':
            candsQ = [i for i in generate_extraSimple.ds]
        else:
            candsQ = [i for i in generate_extraSimple.ps] +\
                     [i for i in generate_extraSimple.ds]
    elif qvb == 'v':
        if not rc:
            candsV = [i for i in generate_extraSimple.cr] + \
                     [i for i in generate_extraSimple.sc]
        else:
            candsV = [i for i in generate_extraSimple.cr] + \
                     [i for i in generate_extraSimple.sc] + \
                     [i for i in generate_extraSimple.rc]
    else:
        if psds == 'ps':
            candsQ = [i for i in generate_extraSimple.ps]
        elif psds == 'ds':
            candsQ = [i for i in generate_extraSimple.ds]
        else:
            candsQ = [i for i in generate_extraSimple.ps] +\
                     [i for i in generate_extraSimple.ds]

        candsV = [i for i in generate_extraSimple.cr] + \
                 [i for i in generate_extraSimple.sc]
        if rc:
            candsV += [i for i in generate_extraSimple.rc]

    # Since we're dealing with 2 books, I'm using a prefix Q/V to disambiguate.
    # This, however, makes the elements strings.

    candsQ = list(map(lambda s: 'Q' + s, map(str, candsQ)))
    candsV = list(map(lambda s: 'V' + s, map(str, candsV)))

    cands = list(filter(lambda e: e not in _ignored_extra, candsQ + candsV))

    ret = []

    while nProb >= 1:
        try:
            ret = sorted(np.array(cands)
                         [sorted(np.random.choice(len(cands), (nProb,),
                                                  replace=False))])
            break

        except ValueError:
            nProb -= 1

    if nProb < 1:
        raise RuntimeError("Seems you've run out of problems.")

    return sorted(ret)


generate_extraSimple.ps = range(1, 177)
generate_extraSimple.ds = range(177, 320)
generate_extraSimple.rc = range(1, 102)
generate_extraSimple.cr = range(102, 200)
generate_extraSimple.sc = range(200, 313)


def generate_set_rc(nPass: int, nQs: int, subcats=frozenset()):
    """
    OG problem set builder for RC problems.

    :param nPass: number of passages desired.
    :param nQs: (max) number of questions per passage.
    :param subcats: subcategories desired
    :param kwargs:
    :return: list of lists: questions grouped by passage
    """

    source = []

    # all the subcats
    if not len(subcats):
        newSubcats = tuple(RC.keys())
    else:
        newSubcats = subcats

    for subcat in newSubcats:
        source += RC[subcat]

    # find out passages from contiguous q numbers
    source = sorted(source, key=_sortkey)
    split_source = []

    for rng in RC_pass:

        def filterKey(el):
            r0 = rng[0] if isinstance(rng[0], int) else int(rng[0][1:])
            r1 = rng[1] if isinstance(rng[1], int) else int(rng[1][1:])

            if isinstance(el, int):
                return el in range(r0, r1 +1)
            elif isinstance(el, str):
                return int(el[1:]) in range(r0, r1 + 1)
            else:
                raise TypeError

        split_source.append(list(filter(filterKey, source)))

    a_ss = np.array([np.array(list(filter(lambda el: el not in _ignored, row)))
                     for row in split_source])

    ret = []
    passages = sorted(np.random.choice(np.shape(a_ss)[0], (nPass,),
                                       replace=False))
    for iPass in passages:
        err = True
        q = nQs

        while err:
            try:
                selRow = list(a_ss[iPass]
                                    [sorted(np.random.choice(np.shape(
                                            a_ss[iPass])[0], (q,),
                                            replace=False))])

                # fix numpy int format which messes up the json serialization
                for i in range(len(selRow)):
                    try:
                        selRow[i] = int(selRow[i])
                    except TypeError:
                        # string etc.
                        pass

                ret.append(selRow)
                err = False

            except ValueError:
                # not enough qs in a passage, choose less
                q -= 1

    return ret


def _countTot(dic):
    """
    Will count the number of atomic elements in the dictionary
    """

    ll = 0

    for e in dic:
        if isinstance(dic[e], dict):
            # subdictionary
            ll += _countTot(dic[e])

        else:
            try:
                ll += len(dic[e])
            except Exception:
                ll += 1

    return ll


def _sortkey(el):
    if isinstance(el, int):
        return el
    elif isinstance(el, str):
        return int(el[1:])


def _groupSequence(l):

    temp_list = it.cycle(l)
    next(temp_list)

    def isConsec(el):
        if isinstance(el, int):
            return el + 1 == next(temp_list)
        elif isinstance(el, str):
            try:
                return int(el[1:]) + 1 == int(next(temp_list)[1:])
            except TypeError:
                return False

    groups = it.groupby(l, key=isConsec)

    for k, v in groups:
        if k:
            yield tuple(v) + (next((next(groups)[1])), )


def ignore(ignored: set):
    """
    Add the iterable ignored to the permanently ignored problems.

    :param ignored:
    """
    global _ignored

    _ignored = set(_ignored).union(set(ignored))
    with open("ignored.json", 'w') as f:
        json.dump(list(_ignored), f)


if __name__ == "__main__":

   # res = generate_set(6, 'b', cats=_quant | _verb - {"RC"})
   # print(res)
   # res2 = generate_set_rc(1, 3)
   # print(res2)
   #
   # print("Done " + str(round(len(_ignored) / _countTot(_tot) * 100, 2))
   #       + "% of problems")

   ## Add done problems to the ignored set
   # ignore(res)
   # ignore([p for group in res2 for p in group])

    resE = generate_extraSimple(10)
    print(resE)
