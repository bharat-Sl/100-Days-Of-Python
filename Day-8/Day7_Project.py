#Project Day7
import Day7_project_alphabet as pa
import math

def under_26(shift):
    more= math.floor(shift/26)
    return shift

def shift_alphabet(character,shift):
    index=pa.alphabet.index(character)
    new_index=index+shift
    if(index>24):
        new_index-=24
    return pa.alphabet[new_index]

def caesar(text,shift):
    output_string=''
    type_='encode'
    for char in text:
        output_string=output_string+shift_alphabet(char,shift)
    if(shift<0):
        type_='decode'
    print(f"Here's the {type_}d result: {output_string}")



print(pa.logo)
run=True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift=under_26(shift=int(input("Type the shift number:\n")))
    if(direction=='encode'):
        caesar(text=text,shift=shift)
    else:
        caesar(text=text,shift=-shift)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    if restart.lower() != "yes":
        run=False
        print("Goodbye")
    else:
        print('\n')