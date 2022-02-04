# WITH FASTA FILE ------

import operator

def printSeq(key, seq, k, output):
    with open(output, "a") as output:
        print(key, file = output)
        kmers = {}
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            if kmer in kmers:
                kmers[kmer] += 1
            else:
                kmers[kmer] = 1

        for kmer, count in kmers.items():
            print(kmer + "\t" + str(count), file = output)

        sortedKmer = sorted(kmers.items(), reverse=True)

        for item in sortedKmer:
            print(item[0] + "\t" + str(item[1]), file = output)

def buildKmers(input, k, output):
    with open(input, 'r') as file:
        seq = ""
        key = ""
        for line in file.readlines():
            if line.startswith(">"):
                if key and seq:
                    printSeq(key, seq, k, output)
                key = line.strip()
                seq = ""
            else:
                seq += line.strip()
        printSeq(key, seq, k, output)

buildKmers("amyloid-beta.fasta", 5, "test.txt")
