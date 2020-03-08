# set_generator
GMAT OG 2020 practice set generator, with some support for OG 2019.
The software was written for personal use as a helper for practice.

GMAT is a registered trademark of GMAC.

## set_generator.py
The main program. The user interface consists of three functions:

### generate_set
Generates a set of *nProb* problems of all types but Reading Comprehension.
The categories can be further specified, refer to the inline documentation.

### generate_set_rc
Generates a set for Reading Comprehension practice. Due to the nature of the problem type, the 
setting here is twofold: first one specifies the number of passages, *nPass*, and subsequently the
number of questions per passage, *nQs*. The actual number returned might be lower, if a passage is shorter
or questions have been exhausted.
The sub-categories can be further specified, refer to the inline documentation.

### ignore
The iterable *ignored* is added to the permanently ignored, i.e. done, problems, saved in a generated *ignored.json* file in
the root directory. Upon import the contents of the file are parsed and imported.

## dicts2020.py
Holds the OG2020 problem classification.

## dicts2019.py
Holds the OG2019 problem classification with no RC problems.

## converter.py
Contains a limited OG2020 : OG2019 (and vice-versa) conversion map. 
Requires [*bidict*](https://pypi.org/project/bidict/).
