#! /usr/bin/python
# Filename: chardiff.py
# Description:
# Author: Pushpendre Rastogi
# Created: Tue Apr  7 11:53:47 2015 (-0400)
# Last-Updated:
#           By:
#     Update #: 15

# Commentary:
# A command line utility to give character level diffs using Google's
# library
from diff_match_patch import diff_match_patch
from itertools import izip_longest
import argparse

parser = argparse.ArgumentParser(description='chardiff shows the diff in words between files along with line numbers. The line numbers start at 1')
parser.add_argument("original_file")
parser.add_argument("new_file")
args = parser.parse_args()
dmp=diff_match_patch()

def diff_wordWord(text1, text2, dmp):
    a = dmp.diff_linesToWords(text1, text2)
    lineText1 = a[0]
    lineText2 = a[1]
    lineArray = a[2]
    diffs = dmp.diff_main(lineText1, lineText2, False);
    dmp.diff_charsToLines(diffs, lineArray);
    return diffs

for idx, (l1, l2) in enumerate(izip_longest(open(args.original_file), open(args.new_file))):
    # d = dmp.diff_main(l1, l2)
    # dmp.diff_cleanupSemantic(d)
    d = diff_wordWord(l1, l2, dmp)
    d2= [e for e in d if e[0]!=0]
    if d2 != []:
        removal = [e for e in d2 if e[0] == -1]
        addition = [e for e in d2 if e[0] == 1]
        print (idx+1), removal, addition
