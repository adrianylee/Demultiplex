#!/usr/bin/env python

import gzip
import bioinfo
import matplotlib.pyplot as plt

R1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
I1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
I2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz"
R2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"
files = [(R1, "R1"), (I1, "I1"), (I2, "I2"), (R2, "R2")]

def initializeEmptyList(size: int) -> list:
    return [0.0] * size

def calculateDistribution():
    for file, name in files:
        with gzip.open(file, "rt") as fi:
            i = 0
            perBaseQualityScore = []
            for line in fi:
                line = line.strip()
                if (i + 1) % 4 == 0:
                    if len(perBaseQualityScore) == 0:
                        perBaseQualityScore = initializeEmptyList(len(line))
                    for pos, score in enumerate(line):
                        perBaseQualityScore[pos] += bioinfo.convert_phred(score)

                i += 1

            records = i // 4

            for pos in range(len(perBaseQualityScore)):
                perBaseQualityScore[pos] /= records

        with open("averageQS.txt", "a") as fo:
            fo.write(f"{name}: {perBaseQualityScore}\n")

        base_pos = [0] * len(perBaseQualityScore)
        for i in range(len(perBaseQualityScore)):
            base_pos[i] = i

        plt.bar(base_pos, perBaseQualityScore)
        plt.title(f"Average Quality Score at Each Base Value Position Across {name}")
        plt.xlabel("Base Position")
        plt.ylabel("Average Quality Score")
        plt.savefig(f"{name}.png")
        plt.close()

calculateDistribution()

                    
