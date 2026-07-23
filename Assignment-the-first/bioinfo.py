#!/usr/bin/env python

# Author: Adrian Lee <aylee@uoregon.edu>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
'''

__version__ = "0.4"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = set("ATGC")
RNA_bases = set("AUGC")

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score. Returns the numerical phred quality score'''
    return ord(letter) - 33

def qual_score(phred_score: str) -> float:
    '''Takes a set of phred scores for a single sequence and returns the average of the phred quality scores across the entire sequence'''
    total = 0
    for i in range(len(phred_score)):
        total += convert_phred(phred_score[i])
        # print(i, phred_score[i], total)
    average = total / len(phred_score)
    return average

def validate_base_seq(seq: str, RNAflag: bool=False):
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    seq = seq.upper()
    UTnuc = "U" if RNAflag else "T"
    return len(seq) == seq.count(UTnuc) + seq.count("A") + seq.count("C") + seq.count("G")

def gc_content(DNA):
    '''Given a valid sequence, returns GC content of a DNA or RNA sequence as a decimal between 0 and 1.'''
    assert validate_base_seq(DNA) or validate_base_seq(DNA, RNAflag=True), "NOT DNA STRING"

    DNA = DNA.upper()
    return (DNA.count("G") + DNA.count("C")) / len(DNA)

def calc_median(lst: list) -> int:
    '''calculates the median of a list. Takes the middle number or the average of the middle 2 if there's an even number of digits'''
    #print(len(lst))
    lst = sorted(lst)
    middle = len(lst) / 2
    #print(middle)
    if middle % 1 == 0:
        #print("ya")
        median = (lst[int(middle) - 1] + lst[int(middle)]) / 2
    else:
        median = lst[int(middle)]
    return median

def oneline_fasta(file, out):
    '''takes a fasta file as input. Makes sure the sequence lines per 
    record are on a singular line (fasta record becomes two lines)
    so it is easier to parse downstream'''
    with open(file, "r") as fi:
        with open(out, "w") as fo:
            dnaLine = ""
            for line in fi:
                line = line.strip()
                if line.startswith(">") and dnaLine != "":
                    fo.write(f"{dnaLine}\n")
                    fo.write(f"{line}\n")
                    dnaLine = ""
                else:
                    dnaLine += line
            fo.write(f"{dnaLine}\n")

def reverse_complement(index: str) -> str:
    bases = {"A":"T", "T":"A", "C":"G", "G":"C", "N":"N"}
    complement = ""
    for i in index:
        complement += bases[i]
    reverseComplement = "".join(reversed(complement))
    return reverseComplement

def phred_threshold(index: str, threshold: int) -> bool:
    for i in index:
        current = convert_phred(i)
        if current < threshold:
            return False
    return True

if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    # These tests are run when you execute this file directly (instead of importing it)
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")
    assert qual_score("I") == 40, "wrong"
    assert qual_score("II") == 40, "wrong"
    assert qual_score("I$") == 21.5, "wrong"
    print("Your qual_score function is working! Nice job")
    assert validate_base_seq("ATGC") == True, "wrong"
    assert validate_base_seq("atgc") == True, "wrong"
    assert validate_base_seq("ATGX") == False, "wrong"
    assert validate_base_seq("AUGC", RNAflag=True) == True
    print("Your validate_base_seq function is working! Nice job")
    assert gc_content("GC") == 1.0, "wrong"
    assert gc_content("AT") == 0.0, "wrong"
    assert gc_content("ATGC") == 0.5, "wrong"
    print("Your gc_content function is working! Nice job")
    assert calc_median([1]) == 1, "wrong"
    assert calc_median([1, 2, 3]) == 2, "wrong"
    assert calc_median([1, 2, 3, 4]) == 2.5, "wrong"
    print("Your calc_median function is working! Nice job")
    print(reverse_complement("NCTTCGAC")) # GTCGAAGN