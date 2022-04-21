# waterfall group code, 4/14/22
import string
import random
from time import sleep
import datetime

def main():  # return option number
    print(
        "\n1: Text to Number \n2: Text to Binary \n3: Multiples of Number \n4: Text Cipher \n5: Random CS fun fact \n6: DNA to RNA \n7: How many days left in the school year \n8: Exit"
    )
    while True:
        print("\nEnter an option below:")
        try:
            opt = int(input("\n"))
            if 0 < opt <= 8:
                break
        except:
            pass
    return opt


def text_cipher():  # Jack's function - I love this library so much now -
    #https://docs.python.org/3/library/string.html
    print(
        "\nNote: This will only properly work with messages made out of letters and space.\n"
    )
    while True:
        message = input("\nEnter message: ")
        text = message.lower()
        doing = input("\nAre you encoding or decoding this message? [encode] or [decode] ")
        try:
            if doing == "encode":
                shift = 3
              # a string of the alphabet, both uppercase and lowercase
                alphabet = string.ascii_letters
              # move the alphabet over dependant on our shift (3)
                shifted_alphabet = alphabet[shift:] + alphabet[:shift]
              # creates a translation table -
              # https://docs.python.org/3/library/stdtypes.html?highlight=maketrans#str.maketrans
                table = str.maketrans(alphabet, shifted_alphabet)
              # translate the message into the shifted alphabet with the translation table we just made
                print("Encrypted text:", message.translate(table))
                break

            elif doing == "decode":  # same process as encoding except,
                shift = -3  # the shift is reversed!
                # (you can clap now)
                alphabet = string.ascii_letters
                shifted_alphabet = alphabet[shift:] + alphabet[:shift]
                table = str.maketrans(alphabet, shifted_alphabet)
                print("Decrypted text:", message.translate(table))
                break

            else:
                print("\nInvalid choice\n")
        except:  # if someone throws special characters in that break the cipher
            print("Please only use letters and space")


def text_to_number():  # Alana
    num = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        " ": " - "
    }
    while True:
      message = input("\nPlease enter a message you would like to convert to numbers: ").lower()
      message2 = ""
      try:
        for i in message:
          message2 += str(num[i])
          message2 += " "
        print(message2)
        break
      except:
        print("\nPlease only input letters.")

def text_to_binary():
    Alph = {
        "a": "01100001",
        "b": "01100010",
        "c": "01100011",
        "d": "01100100",
        "e": "01100101",
        "f": "01100110",
        "g": "01100111",
        "h": "01101000",
        "i": "01101001",
        "j": "01101010",
        "k": "01101011",
        "l": "01101100",
        "m": "01101101",
        "n": "01101110",
        "o": "01101111",
        "p": "01110000",
        "q": "01110001",
        "r": "01110010",
        "s": "01110011",
        "t": "01110100",
        "u": "01110101",
        "v": "01110110",
        "w": "01110111",
        "x": "01111000",
        "y": "01111001",
        "z": "01111010",
        " ": "00100000"
    }

    while True:
      message = input("\nPlease enter a message you would like to convert to binary: ").lower()
      message2 = ""
      try:
        for i in message:
          message2 += str(Alph[i])
          message2 += " "
        print(message2)
        break
      except:
        print("\nPlease only input letters.")
        
        
def multiples_of_num(): #Abhash
    # inputting two numbers, ex. 5,7, should return 7 multiples of 5
  mult_num = int(input("Enter the number: "))
  amnt = int(input("Enter the desired amount of multiples: "))

  print(amnt, "multiples of", mult_num, ": ")
  for i in range(1, amnt+1):
    print(mult_num*i, end =" ")
  print("\n")

    



def fun_fact():
  with open("funfacts.txt") as f:
    lines = f.readlines()
    print("\n")
    print(random.choice(lines))


def timeleftschool():
  today = datetime.date.today()
  end = datetime.date(2022, 6, 20)
  #print(end)
  #print(today)
  diff = (end - today)
  diff = str(diff)
  diff = diff[:7]
  #print(diff)
  
  print(diff,"left before school gets out")


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


# runtime
if __name__ == '__main__':
    while True:
        sleep(.5)
        choice = main()

        if choice == 1:
            text_to_number()

        elif choice == 2:
            text_to_binary()

        elif choice == 3:
            multiples_of_num()

        elif choice == 4:
            text_cipher()

        elif choice == 5:
            fun_fact()
          
        elif choice == 6: # reserved for Shale
            rna_main()
            
        elif choice == 7:
            timeleftschool()
        elif choice == 8: 
            break
