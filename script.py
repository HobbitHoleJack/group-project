def print_menu(): #Shale
    print("===================")
    print("1: DNA to RNA")
    print("0: Exit the program")
dna_to_rna_dict = {
  "C": "G", 
  "A": "U",
  "G": "C",
  "T": "A"
}

def dna_to_rna(dna_seq):
    rna_seq = ""
    # iterate each character in the DNA sequences
    for dna_char in dna_seq:
        # check if the character is valid
        if dna_char in dna_to_rna_dict.keys():
            # convert each character from DNA to RNA using the dictionary
            rna_seq += dna_to_rna_dict[dna_char]
        else:
            # did not recognize the character
            rna_seq += '?'
    return rna_seq

# main program
def rna_main():
  while True:
      print_menu()
      try:
        option = int(input("Enter an option here: "))
        try:
            if option == 0:
                break # exit the program
            elif option == 1:
                dna_seq = input("Enter the DNA sequences (CAGT): ") # CACGTAGACTGAGGACTCCTCTTC
                rna_seq = dna_to_rna(dna_seq)
                print("The RNA sequences is:", rna_seq)
            else:
                print("We don't recognize the option " + option)
        except:
            pass
      except:
        print("We don't recognize the option")
  print("Good Bye!")