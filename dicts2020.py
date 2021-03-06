# -*- coding: utf-8 -*-
"""
@author: Andrej Leban
#@Filename : dicts2019.py
#@Date : 2019-10-28-10-43
"""

# these are OG2020 numbers unless stated otherwise
FDPs = {
        "PS": {
                "FDPs": [42, 112, 135],
                "DigitsNDecimals": ["D1", 103, 139, 147, 192, 200, 203, 219,
                                    225],
                "Fractions": ["D8", 8, 11, 20, 43, 50, 57, 69, 73, 74, 80, 89,
                              102, 132, 163, 167, 220],
                "Percents": ["D12", "D21", 4, 7, 16, 19, 34, 51, 67, 71, 78,
                             87, 93, 94, 105, 113, 114, 125, 126, 131, 153,
                             169, 172, 191, 207, 210, 216],
                "Ratios": [12, 14, 39, 48, 160]
               },
        "DS": {
                "FDPs": [282],
                "DigitsNDecimals": ["D25", 266, 291, 348, 351, 370, 389, 405,
                                    410, 444, 455, 459],
                "Fractions": [336, 443],
                "Percents": ["D40", 247, 260, 263, 267, 276, 344, 363, 378, 379, 381, 388, 396, 407, 416, 453],
                "Ratios": [235, 238, 239, 240, 243, 244, 249, 279, 319, 346, 366, 391, 424, 458]
               }
        }

# including the new category "Equations, Inequalities & VICs" under "Formulas"
Algebra = {
        "PS": {
                "LinEq": [10, 22, 29, 47, 55, 92, 150, 157, 186],
                "ExpNRoots": ["D17", 76, 101, 117, 161, 180, 209, 213, 223,
                              230],
                "QuadEq": ["D16", 82, 90, 104, 116, 128, 155, 168, 215, 222,
                           226],
                "Formulas": ["D3", 59, 79, 95, 115, 129, 184, 196, 198, 206,
                             212, 111],
                "InEq": [26, 35, 61, 85, 122, 185, 189, 193, 228]
               },
        "DS": {
                "LinEq": ["D35", 232, 255, 280, 297, 313, 314, 327, 340, 359,
                          365, 373, 447, 460],
                "ExpNRoots": ["D44", 252, 259, 262, 296, 302, 353, 386, 398,
                              406, 432],
                "QuadEq": [286, 305, 337, 357, 422],
                "Formulas": [250, 287, 420, 433, 251, 290, 292, 298, 311, 312,
                             326],
                "InEq": ["D33", "D37", 281, 362, 368, 375, 392, 393, 395, 411,
                         415, 417, 426, 457]
               }
        }

WP = {
        "PS": {
                "Transl": [2, 5, 9, 17, 18, 23, 33, 36, 45, 46, 64, 65, 75,
                           143, 188, 190],
                "Rates": ["D24", 77, 83, 110, 118, 130, 133, 199],
                "Overlap": ["D4", "D6", "D14", 123, 124, 152, 208, 229],
                "Stats": ["D9", 3, 21, 30, 54, 63, 91, 121, 134, 136, 137, 144,
                          151, 158, 164, 166, 179, 194, 211, 217],
                "WAv": [15, 107, 138, 149, 171, 227],
                "ConsecInts": ["D2", 88, 120, 197, 204],
                "Extra": [49, 86, 173]
               },
        "DS": {
                "Transl": ["D27", "D30", 233, 236, 294, 295, 309, 315, 342, 349,
                           350, 354, 383, 401, 408, 449],
                "Rates": ["D38", 356, 397, 430, 436],
                "Overlap": ["D29", "D34", "D47", 258, 264, 274, 275, 283, 323,
                            361, 418, 445],
                "Stats": ["D31", "D32", "D43", "D46", 231, 234, 241, 242, 253,
                          254, 303, 320, 338, 339, 377, 382, 384, 414, 431,
                          434, 437, 441, 448, 450, 451, 452],
                "WAv": [404, 429],
                "ConsecInts": [304, 372, 374, 380, 419],
                "Extra": ["D45", 270, 300, 307, 347, 385, 394, 428]
               },
        }

Geometry = {
        "PS": {
                "LinesNAngles": [31, 32],
                "Polygons": [1, 52, 70, 97, 98, 100, 109, 202, 224],
                "Triangles": ["D10", "D19", 37, 40, 56, 99, 145, 156, 159,
                              174],
                "Circles": ["D5", "D20", "D22", 25, 44, 72, 96, 106, 119, 146,
                            177],
                "Coord": [6, 13, 62, 68, 84, 183, 218]
              },
        "DS": {
                "LinesNAngles": [269],
                "Polygons": [246, 317, 324, 330, 332, 333, 335, 358, 360, 369,
                             371, 376, 423, 456],
                "Triangles": ["D28", "D48", 237, 268, 289, 306, 328, 329, 334,
                              402, 409, 440, 442, 454],
                "Circles": ["D36", 261, 271, 273, 321, 322, 331, 345, 399,
                            425, 427, 435],
                "Coord": ["D39", 272, 325, 387, 403, 438, 439]
              },
        }

# including the new category "Foundations of Math" as a separate subcategory
NumProp = {
        "PS": {
                "DivNPrimes": ["D13", "D15", "D18", "D23", 58, 60, 66, 81, 108,
                               127, 141, 154, 165, 175, 176, 178, 181, 195,
                               205],
                "ExpNRoots": [41],
                "PosNNeg": [38],
                "Comb": ["D11", 140, 148, 182, 187, 201, 214],
                "Prob": ["D7", 24, 142, 162, 170, 221],
                "FOM": [27, 28, 53]
              },
        "DS": {
                "DivNPrimes": ["D26", "D42", 248, 299, 301, 310, 318, 341, 343,
                               352, 390, 412, 413, 446],
                "OddsNEvens": [284, 285, 288, 293],
                "PosNNeg": ["D41", 256, 257, 265, 278, 308, 316, 364, 367, 400,
                            421],
                "Prob": [245, 277, 355]
              },
        }


### Verbal

CR = {
      "DescRole": [635, 643, 657, 663, 665, 681, 686, 700, 701, 714, 730, 738,
                   742, 743, 750],
      "FTA": ["D76", 612, 622, 623, 651, 659, 664, 667, 675, 679, 690, 692,
              693, 694, 706, 719, 726, 728, 736, 741, 746, 748],
      "Strength": ["D73", "D75", "D80", 610, 611, 614, 618, 620, 621, 624, 626,
                   627, 628, 629, 631, 632, 634, 636, 639, 641, 644, 645, 646,
                   647, 649, 652, 655, 661, 662, 671, 674, 677, 678, 680, 683,
                   684, 685, 691, 695, 696, 697, 698, 699, 702, 715, 717, 722,
                   732, 739, 740, 752],
      "Weak": ["D66", "D68", "D71", "D74", "D78", "D82", 615, 619, 625, 630,
               653, 656, 658, 666, 670, 672, 673, 687, 688, 703, 707, 708, 710,
               711, 713, 716, 718, 720, 733, 737, 745, 749, 755, 757, 758],
      "EvalArg": ["D69", "D70", "D77", 638, 723, 727, 729, 734, 735, 754],
      "EvalConcl": [689, 704],
      "Flaw": [642, 668, 724],
      "Infer": ["D72", "D79", 617, 660, 676, 709, 725, 744, 753],
      "Discr": ["D67", "D81", 613, 616, 633, 637, 640, 648, 650, 654, 669, 682,
                705, 712, 721, 731, 747, 751, 756]
      }

RC = {
      "Infer": ["D51", "D52", "D53", "D57", "D58", "D63", 463, 465, 467, 469,
                472, 474, 478, 479, 480, 486, 488, 491, 492, 495, 501, 503,
                506, 509, 510, 512, 515, 516, 517, 518, 519, 522, 523, 528,
                529, 531, 534, 538, 540, 544, 546, 554, 555, 556, 557, 560,
                561, 566, 567, 571, 572, 577, 578, 579, 582, 585, 586, 587,
                590, 591, 592, 593, 594, 599, 600, 602, 603, 608, 609],
      "MainIdea": ["D50", "D54", "D56", "D60", 461, 464, 475, 477, 525, 532,
                   533, 543, 549, 550, 558, 563, 565, 570, 583],
      "Paragraph": [511, 581],
      "Structure": ["D49", 530, 548, 574],
      "PrimPurpose": [482, 500, 508],
      "Purpose": [481, 541, 542, 551, 559, 568, 575, 589, 596, 601, 606, 607],
      "SpecDetail": ["D55", "D59", "D61", "D62", "D64", "D65", 462, 466, 468,
                     470, 471, 473, 483, 485, 487, 489, 490, 493, 494, 496,
                     497, 498, 499, 502, 504, 505, 507, 513, 514, 520, 521,
                     524, 526, 527, 536, 537, 539, 547, 552, 553, 562, 569,
                     573, 576, 580, 584, 588, 595, 597, 598, 605],
      "SpecPurpose": [484],
      "Strength": [545],
      "Weak": [476, 535, 564, 604]
     }

# The intervals for RC questions belonging to the same passage
RC_pass = [
           ("D49", "D53"),
           ("D54", "D59"),
           ("D60", "D65"),
           (464, 466),
           (464, 466),
           (467, 468),
           (469, 472),
           (473, 476),
           (477, 481),
           (482, 485),
           (486, 489),
           (490, 493),
           (493, 501),
           (502, 509),
           (510, 514),
           (515, 519),
           (520, 524),
           (524, 527),
           (528, 532),
           (532, 538),
           (539, 542),
           (543, 545),
           (546, 549),
           (550, 555),
           (556, 558),
           (559, 564),
           (565, 569),
           (570, 575),
           (576, 579),
           (580, 582),
           (583, 590),
           (591, 595),
           (596, 602),
           (603, 606),
           (607, 609),
           ]

SC = {
      "Meaning": [768, 774, 782, 793, 796, 798, 808, 824, 827, 845, 872, 873,
                  881, 892, 898],
      "SVA": ["D89", "D91", 775, 786, 803, 849, 853, 854, 859, 871, 889, 899,
              901, 907],
      "Struc": [761, 764, 769, 771, 772, 773, 817, 819, 823, 833, 834, 837,
                847, 851, 877, 885],
      "Mods": ["D88", "D92", "D97", 762, 765, 767, 787, 794, 801, 802, 804,
               806, 807, 810, 812, 822, 826, 828, 832, 835, 839, 840, 846, 848,
               850, 855, 870, 876, 882, 886, 890, 893, 897],
      "Parallel": ["D84", "D87", "D94", "D96", "D98", "D99", 759, 760, 763,
                   776, 784, 788, 792, 795, 799, 809, 811, 813, 816, 818, 820,
                   829, 830, 831, 842, 844, 857, 860, 863, 866, 868, 888, 895,
                   902],
      "Compar": ["D83", "D85", "D95", "D100", 770, 777, 779, 781, 785, 790,
                 797, 800, 825, 836, 838, 852, 858, 861, 867, 875, 880, 883,
                 884, 891, 906],
      "Pron": ["D90", 778, 843, 862, 865, 869, 874, 879, 896],
      "Verbs": [783, 805, 814, 821, 894, 903, 904],
      "Idioms": ["D86", "D93", 766, 780, 789, 791, 815, 841, 856, 864, 878,
                 887, 900, 905]
      }
