# part 1: find csv data 
#Part 2: analysis the data ---> summarize the past data as growth or recession based on the average.
import csv
import pandas as pd

def Read_Unemployment_rate():
  my_df = pd.read_csv('data/unemployment_rate .csv') # stores data in my_df, each column has a coressponding header

  
# step 1: create a new column that has the avg of all the columns in each row
  month_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

  my_df['Avg_Year'] = my_df[month_columns].mean(axis=1) # avg for each year
  print(my_df[['Year','Avg_Year']].to_string(index=False)) # returns a table of : year, avg_year, get ride of indexing

# step 2: find the avg of the 24 years, then we will compare each avg_year to total_avg
  total_avg = my_df['Avg_Year'].mean() # avg of 23 years is 5.663
  print('Avg in 24 years:', total_avg)


# determine if each year: recession, growth
Status_growth_recession = []
for avg in my_df['Avg_Year']:
    if avg < total_avg:
      Status_growth_recession.append('Recession')
    
    elif avg > total_avg:
      Status_growth_recession.append('Growth')

    else:
            Status_growth_recession.append('No Economic Change')





Read_Unemployment_rate()
