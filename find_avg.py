# part 1: find csv data 
#Part 2: analysis the data ---> summarize the past data as growth or recession based on the average.
import csv
import pandas as pd

def Read_Unemployment_rate():
  my_df = pd.read_csv('data/unemployment_rate .csv') # stores data in my_df, each column has a coressponding header

# so now create a new column that has the avg of all the columns in each row\
  my_df['Avg_year'] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  my_df.mean(axis=1) # find the mean of all 12 columns 
  print( my_df)

Read_Unemployment_rate()
