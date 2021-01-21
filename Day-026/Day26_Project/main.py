#Project Day26
import os

os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-026\Day26_Project")
import pandas as pd

nato_phonetic_alphabet=pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict={row.letter:row.code for (index,row) in nato_phonetic_alphabet.iterrows()}

user_string=input("Enter a string to convert into NATO phonetic dictionary:").upper()
phonetic_user_string=[nato_dict[char] for char in list(user_string)]
print(phonetic_user_string)
