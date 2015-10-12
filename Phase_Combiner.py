"""
This is a tutorial program that will enable merging of multiple excel files
by a primary key, and saves as a csv.

"""

#imports
import pandas as pd
import numpy as np
import glob

#Finds all files with sales and .xls from the specified directory

path = r"z:\Integration 2014"
glob.glob(path + r"\Sheet*.xlsx")

#creates variable "all_data" and reads sales*.xls files into the pandas
#dataframe from the specified directory

all_data = pd.DataFrame()
for f in glob.glob(path + r"\*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

#print description of dataframe to prove it works
print all_data.describe()

#normalizes date to date/time format
#all_data['date'] = pd.to_datetime(all_data['date'])

#reads the customer status file and puts it into the dataframe
#status = pd.read_excel(path + r"\customer-status.xlsx")
#print status


#merges status to all_data as new variable "all_data_st"
#all_data_st = pd.merge(all_data, status, how='left')
#all_data_st.head()


#fills all status fields that are "NaN" fields with "bronze"
#all_data_st['status'].fillna('bronze',inplace=True)
#all_data_st.head()

#writes the all_data_st dataframe to a .csv file in the working directory
all_data.to_csv("Combined_PhaseSheet.csv")