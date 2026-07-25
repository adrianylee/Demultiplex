Problem: Want to take in Illumina sequencing data and sort it for index hopping/matches/unknown, given known barcodes/indexes.

Output: A dictionary of all index matches (including index-hops) and a count of unknown sequences (based off of indexes)

Unit Tests

```
R1, R4 --> Biological Reads (no indexes, and they shouldn't reverse complement)
R2, R3 --> Index Reads (reverse complements)

indexes.txt

def reverse_complement(index1):
    '''function that returns the reverse complement of the given string'''
    returns indexReversedComplemented
Input: ACGT
Output: TGCA

def phred(index):
    '''takes in an index and returns True if any character is below the threshold quality score'''
    return True/False
Input: J
Output: 41
Input: #
Output: 2 


def initialize_indexes(R1, R2, R3, R4):
    '''initialize dictionary with every valid index pair'''
    itertools to create the combinations of everything initialize dictionary all values at 0
    return dict
Input: AACC CCAA
Output: {AACC-AACC: 0, AACC-CCAA: 0, CCAA-CCAA: 0, CCAA-AACC: 0}


def demultiplex(R1, R2, R3, R4, quality_score_cutoff):
    unknown = 0
    hopped = 0
    open R1, R2, R3, R4:
        
    while True:
        read 4 lines from each of the files and store all information in different variables

        reverse_complement(R3 index)

        if R2 index not in indexes or R3 index not in indexes:
            unknown += 1
            write R1 and R4 to unknown FASTQ
            continue

        if R2 index contains "N" or R3 index contains "N":
            unknown += 1
            write R1 and R4 to unknown FASTQ
            continue

        if phred(R2 quality, quality_score_cutoff) == True or phred(R3 quality, quality_score_cutoff) == True:
            unknown += 1
            write R1 and R4 to unknown FASTQ
            continue

        if R2 index == reverse_complement(R3 index):
            update dictionary
            write R1 and R4 to matched FASTQ
            add R2Index-R3Index to header

        else:
            hopped += 1
            update dictionary
            write R1 and R4 to index hopping FASTQ
            add R2Index-R3Index to header

    return dictionary, unknown

```
