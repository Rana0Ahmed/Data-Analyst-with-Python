# Notes:
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