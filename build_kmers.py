def build_kmers(k):
  '''
  build_kmers takes input kmer size k and returns a list of all kmers of a specified input protein sequence.
  '''
  print('Enter the protein sequence: ')
  sequence = input()
  
  sequence_length = len(sequence)
  print('The length of your sequence is', sequence_length, '.')
  
  kmers = []
  while sequence_length > k:
    kmers.append(sequence[0:k])
    sequence = sequence[1:]
    sequence_length -= 1
  
  return(kmers)
