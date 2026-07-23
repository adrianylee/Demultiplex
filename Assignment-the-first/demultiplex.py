#!/usr/bin/env python
import bioinfo
import gzip
import argparse

R1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
R2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
R3 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz"
R4 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"
indexes = "/projects/bgmp/shared/2017_sequencing/indexes.txt"

def demultiplex(R1: str, R2: str, R3: str, R4: str, indexes: str, threshold: int):
    readPairs = {}
    hop = {}
    unknown = {}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--threshold", type=int, required=True)
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()