#challenge 3

import os
os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-026\Challenge3")

def listing(file):
    file_contents=file.read()
    temp_list=file_contents.split("\n")
    temp_list.pop(len(temp_list)-1)
    return temp_list


with open("file1.txt", "r") as file1:
    with open("file2.txt","r") as file2:
        list1=listing(file1)
        list2=listing(file2)

result=[element for element in list1 if element in list2]
print(result)