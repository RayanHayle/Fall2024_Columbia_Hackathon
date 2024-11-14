# part 1: find csv data 
#Part 2: analysis the data ---> summarize the past data as growth or recession based on the average.
import csv
import pandas as pd

def Read_Unemployment_rate():
  my_df = pd.read_csv('data/unemployment_rate .csv') # stores data in my_df, each column has a coressponding header
  
# step 1: create a new column that has the avg of all the columns in each row
  month_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

  my_df['Average Yearly'] = my_df[month_columns].mean(axis=1) # avg for each year
  #print(my_df[['Year','Average Yearly']].to_string(index=False)) # returns a table of : year, avg_year, get ride of indexing

# step 2: find the avg of the 24 years, then we will compare each avg_year to total_avg
  total_avg = my_df['Average Yearly'].mean() # avg of 23 years is 5.663
  #print('Average Unemployment Rate in 24 years:', total_avg)

# step 3: determine if each year: recession, growth
  Status_growth_recession = []

  for avg in my_df['Average Yearly']:
      if avg < total_avg:
        Status_growth_recession.append('Growth')
      
      elif avg > total_avg:
        Status_growth_recession.append('Recession')

      else:
              Status_growth_recession.append('No Economic Change')

  my_df['Economic Status'] = Status_growth_recession

  # add status to the table
  status_table = my_df[['Year', 'Average Yearly', 'Economic Status']].to_string(index=False) # one table
  #print(status_table)

  # my df, create table, search for growth in year and Average Yearly
  growth_df = my_df[my_df['Economic Status'] == 'Growth'][['Year', 'Average Yearly']]
  recession_df = my_df[my_df['Economic Status'] == 'Recession'][['Year','Average Yearly']] # add 'Average Yearly' to see avg ununemployment
  print('Based on Unemployment Rates')
  print('Growth: \n',  growth_df.to_string(index=False))
  print('Recession: \n', recession_df.to_string(index=False))

Read_Unemployment_rate()


