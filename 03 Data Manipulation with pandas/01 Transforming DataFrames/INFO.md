# Notes
## II
- DataFrame
  - `.head()` returns the first few rows (the “head” of the DataFrame).
  - `.info()` shows information on each of the columns, such as the data type and number of missing values.
  - `.shape` returns the number of rows and columns of the DataFrame.
  - `.describe()` calculates a few summary statistics for each column.
  - `.values`: A two-dimensional NumPy array of values.
  - `.columns`: An index of columns: the column names.
  - `.index`: An index for the rows: either row numbers or row names
 - Sorting and subsetting
   - You can sort rows using the sort_values method, passing in a column name that you want to sort by.
   ```
   dogs.sort_values("weight")
   ```
   
   - Setting the ascending argument to False will sort the data the other way around, from heaviest dog to lightest dog.
   ```
   dogs.sort_values("weight", assending=False)
   ```
   - We can sort by multiple variables by passing a list of column names to sort_values.
   ```
   dogs.sort_values(["weight", "height"])
   ```
   - To change the direction values are sorted in, pass a list to the ascending argument to specify which direction sorting should be done for each variable.
   ```
   dogs.sort_values(["weight", "height"] accending=[True, False])
   ```
   - We may want to zoom in on just one column
   ```
   dogs["name"]
   ```
   
   - To select multiple columns, you need two pairs of square brackets.
   ```
   dogs[["name", "bleed"]]
   ```
   
   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
   