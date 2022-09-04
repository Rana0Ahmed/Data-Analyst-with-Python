# Notes: 

## I.
## pandas 
 - Pandas is a module for working with tabular data, or data that has rows and columns. Common examples of tabular data are spreadsheets or database tables. 
 - What can pandas do for you : 
   - Loading tabular data from multiple sources (like spreadsheets or databases).
   - search for particular rows or columns in your loaded data. 
   - calculate aggregate statistics (like averages or standard deviations). 
   - combine data from multiple sources. 
   
 - Tabular data with pandas : 
   - Pandas introduces a new, more powerful data type: the DataFrame, which represents tabular data.
   - Loading data into a DataFrame is the first step in using Pandas.
   - 
 - CSV files (comma-separated values):
   - One of the easiest ways to create a DataFrame is by using a CSV file.
   - It is a common way of storing tabular data as a text-only file.
   - You can download a CSV version of data from an Excel spreadsheet, a SQL database, or a Google Sheet.
   _ Loading a CSV :
     - Before we can start using Pandas, we have to import the pandas module under the alias "pd".
     ```
     import pandas as pd
     ```
     
     - Next, we create our first DataFrame from a CSV, Turning a CSV into a DataFrame is easy. We use a function: `pd-dot-read_csv`, This function takes one argument, the name of a CSV file as a string.
     ```
     df = pd.read_csv("ransom.csv")
     ```
     
   - Displaying a DataFrame :
     ```
     print(df)
     ```
     
     - Usually, we don't want to print an entire DataFrame, we just want to view the first few lines. We can do this by using `head` .
       - head method just selects the first five rows of "df" .
       ```
       df.head()
       ```
       
    - Another way of learning about a DataFrame is using the `info` method.
       - We can see the names of the columns, the number of rows, and data types for each column.  
       - This method is useful for DataFrames with many columns that are difficult to display using head.
       ```
       df.info()
       ```
       
       

