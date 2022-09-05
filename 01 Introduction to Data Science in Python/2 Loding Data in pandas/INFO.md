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
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  # II.
  ## To access that data
  - By selecting columns :
    - This means we'll be getting all values from a particular column in a DataFrame.
    - this code selects the column "price" and then calls the method "sum" on that column to get the total amount of money.
    ```
    credit_records.price.sum()
    ```
    
    - Columns names are strings,(strings can have spaces or special characters. That means that columns in DataFrames can also have spaces or special characters).
      - Selecting with brackets and string :
      ```
      suspect = credit_records['suspect']
      ```
      
      -  Selecting with a dot :
      ```
      price = credit_records.price
      ```
      
    - Common mistakes in column selection :
      - when your column name contains spaces or special characters, you need to use bracket and string notation, and not dot notation.
      
      ```
      police_report["Is golden retriever?"] 
      
      Not
      
      police_report.Is golden retriever?
      ```
      
      - forgetting to put quotation marks around the column string when using brackets and string notation.
      - If you forget the quotation marks, then Python thinks that the column name is actually a variable that hasn't been defined yet.
      
      ```
      credit_records['Location']
      
      Not
      
      credit_records[Location]
      ```
      
      - Remember that square brackets `[]` are not the same at parentheses `()`.
       

