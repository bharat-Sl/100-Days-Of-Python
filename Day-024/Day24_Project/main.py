#Project Day24
import os
os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-024\Day15_Project")

with open("./Input/Names/invited_names.txt",mode="r") as file:
    names=file.read().split("\n")
    print(names)
with open("./Input/Letters/starting_letter.docx",mode="r") as file:
    letter=file.read()
    print(letter)
for name in names:
    file=open(f"./Output/ReadyToSend/{name.split(' ')[0]}_Invitation.docx",mode="w+")
    new_letter=letter.replace("[name]",name)
    file.write(new_letter)
    file.close()