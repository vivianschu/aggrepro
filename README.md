# aggrepro


## Pipeline
### 1. Producing fragments
#### Separate fragments of size k from fasta file
```python
# WITH FASTA FILE ------

import operator

def printSeq(header, seq, k, output):
    with open(output, "a") as output:
        kmers = {}
        for i in range(len(seq) - k + 1):
            # Extract kmer
            kmer = seq[i:i+k]
            if kmer in kmers:
                kmers[kmer][0] += 1
            else:
                kmers[kmer] = [1, i, i+k]
        
        for kmer, count in kmers.items():
            temp_header = header.split("|")[:2]
            out_header = "|".join(str(x) for x in temp_header)
            out_header = out_header + " Count" + str(kmers[kmer][0]) + " Posn" + str(kmers[kmer][1]) + "-" + str(kmers[kmer][2]) + ""
            print(out_header, file = output)
            print(kmer, file = output)

def buildKmers(input, k, output):
    with open(input, 'r') as file:
        seq = ""
        header = ""
        for line in file.readlines():
            if line.startswith(">"):
                if header and seq:
                    printSeq(header, seq, k, output)
                header = line.strip()
                seq = ""
            else:
                seq += line.strip()
        printSeq(header, seq, k, output)
```

Run buildKmers:
```python
buildKmers("[FILE.FASTA]", n, "OUTPUT.FASTA")
```
