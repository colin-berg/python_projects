""" 
This program reads each suspects DNA (I/O), splits these string into codons, iterates through the codon list to see if there is a match, and determines the suspect that was the criminal
"""

sample = ['GTA','GGG','CAC']

#file iterator 
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, 'r') as f:
    for line in f:
      dna_data += line
  return dna_data

#splits text into increments of 3 and adds them to the codons list
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i + 3) < len(dna):
      codons.append(dna[i:i + 3])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

#calls previous functions to determine if suspect is criminal based on dna match 
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "The number of matches is %s. DNA profile matches. Continue the investigation." % (num_matches)
  else:
    print "The suspect can be set free."

is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')
