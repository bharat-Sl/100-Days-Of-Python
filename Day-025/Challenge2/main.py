#challenge 2
import os
os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-025\Challenge2")

import pandas as pd
file_data=pd.read_csv("squirrel_data.csv")

all_fur=file_data['Primary Fur Color'].to_list()
gray=all_fur.count('Gray')
red=all_fur.count('Cinnamon')
black=all_fur.count('Black')

numbers_of_colour=[gray,red,black]
fur_colour=["gray","red","black"]


data_dict={
    "Fur Color":fur_colour,
    "Count":numbers_of_colour
}
final_data=pd.DataFrame(data_dict)
final_data.to_csv("squirrel_count.csv")