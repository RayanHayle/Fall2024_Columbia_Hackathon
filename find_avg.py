# part 1: find csv data 
#Part 2: analysis the data ---> summarize the past data as growth or recession based on the average.
import csv
import pandad as pd


def Read_Unemployment_rate():
  my_df = pd.read_csv('data/unemployment_rate .csv') # unemployment_rate .css is in data path
  print(my_df.head()) # top 5 lines

Read_Unemployment_rate()
