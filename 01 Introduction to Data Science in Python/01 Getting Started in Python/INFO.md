# Notes:
## I
 - What is a module.
   - Groups related tools together
   - Make it easy to know where to look for a particular tool
   - Modules (sometimes called packages or libraries) 
   - Common examples:
     - `matplotlib` (which creates charts)  
     - `pandas` (which loads tabular data)
     - `scikit-learn` (which performs machine learning) usually aliased as 'sm'
     - `scipy` (which contains statistics functions) 
     - `nltk` (which works with text data)
     - `seaborn` (a visualization library) usually aliased as 'sns'
     - `numpy` (for performing mathematical operations on lists of data) aliased as 'np'
     
     
    
 - We must import any modules that we plan on using before we can write any other code, If we don't import modules, we can't use the tools that they contain.
 - To import a module, simply typet `import` followed by a space and then the "module name".
 - To give your module an alias, just add `as` and a shorter name to your original import statement.
  - Imprting a Module :
    ```
      import pandas
    ```
  - Imprting a Module with an alias :
    ```
       import pandas as pb
     ```
## II

- Rules for variable names :

  - Must start with a letter (usually use lowercase). 
  - After first name can use :letters\numbers\underscores.
  - No space or special characters.
  - Case sensetive ('my_var' is different from 'MY_VAR').
    ```
    #Valid variables                     #Invalid variables
    bayes_weight                         bayes-weight  
    b                                    bayes!
    bayes24                              24bayes
    ```
    
    
- Variables come in many "flavors", two important flavors are floats and strings. 
  - Floats represent either integers or decimals.
  
  ```
      height = 24
      width = 24.5
      
  ```
      
 - Strings represent text and can contain letters, numbers, spaces, and special characters.
    - We define a string by putting either 'single quotes' or "double quotes" around a piece of text.
    
    ``` 
        name = 'bayes'
        name = "bayes"
        
    ```
- Displaying variables :
  - We simply type the word`print` and put our variable name inside of the parentheses.
  
    ```
        name = "Bayes"
        height = 24
        width = 25.5
      
        print(height)
    ```
    
    ```
        24
    ```
## III

- Functions perfotm actions

  ```
   import pandas as pd
   from matplotlib import pylot as plt

   df = pd.read_cvs('letter frequency.cvs)

   plt.plot(df.letter_inbex, df.frequency, label = 'Ransom')
   plt.show()

  ```
  -`pd.read_cvs()` turnes a cvs files into a table in python
  
  -`plt.plot()` turnes daa into a line plot
  
  -`plt.show()` display plot in a new window
  
  
|     Letter index   |   Letter   |   Frequency    |
|------------        |------      |--------        |
|1                   |A           |7.38            |
|2                   |B           |1.09            |
|3                   |C           |2.46            |
