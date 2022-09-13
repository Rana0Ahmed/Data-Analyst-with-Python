# Notes
## I
## Dictionaries :
 - To create the dictionary, you need curly brackets.
 - Dictionaries consists of key and values :
 ```
 dict = {key:'value', .......}
 ```
 
 
### Recap
 - keys in a dictionary should be so-called immutable objects.
 - To remove from dict use `del []`
 ```
 del(world['saeland'])
 #world is the name of dict
 ```
 ## List vs. Dictionary
 
|List                                                                  |Dictionary               |
|-------------------------------------------------|-------------------------                     |
|select, update and remove with [ ]                |      select, update and remove with [ ]       |
|indexed by range of numbers                      |indexed by unique key                         |
|collection of values __order matters, for selecting entire subset |lookup table with unique keys|


## II
- Pandas
 - Index and select data
   - square brackets
   - advanced data access methods
     - loc
     - iloc
     
 - Column Access [ ]
 ```
 data['column_anme']
 ```
  - Python prints out the entire column, together with the row labels. 
  - If you want to select the column but keep the data in a DataFrame, you'll need double square brackets
  ```
  data[['column_anme']]
  ```
  - If you want to select many columns, you can write:
  ```
   data[['column_anme1'], ['column_anme2']]
   or
   date[1:2]
   ```
   - Discussion [ ]
     - square brackets work, but it only offers limited functionality.
     - ideally
       - 2D NumPy arrays.
       - my_arr['rows', 'columns']
     - panads
       - `loc` label based
       - `iloc` integer position based
       
   - Row Access loc
     - You put the label of the row of interest in square brackets after loc
     ```
     data.loc('row_name')
     ```
     - you can extend your selection with a comma and a specification of the columns of interest.
       _ We add a comma, and a list of column labels we want to keep
       - you can also use loc to select all rows but only a specific number of columns.
       ```
       data.loc['row1', 'row2', ...]['column1', 'column2', ....]
       ```
       
     - Simply replace the first list that specifies the row labels with a colon, a slice going from beginning to end. This time, the intersection spans all rows, but only two columns.
    
      ```
      data.loc[:, ['column1', 'column2']]
      ```
  - iloc
    - using iloc is similer to using loc but we use position in iloc.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## III

 - Comparison Operators
  - Loop Data Structures
    - Dictionary : 
  ```
  for k, v in dict.items()
  print(k + " is" + str(v))
  ```
   - NumPy array :
   ```
   for val in np.nditer(my_arr) :
        print(val)
   ```    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## IV
- Random Numbers
  - Random generators
    - we called the `rand` function
    ```
    import numpy as np
    np.random.rand()
    ```
    
  - seed(): sets the random seed, so that your results are reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
  - rand(): if you don't specify any arguments, it generates a random float between zero and one.
  