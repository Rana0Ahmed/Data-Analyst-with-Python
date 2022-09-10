# Notes

## Basic plots with Matplotlib :
 - Data visualization :
   - explore your dataset.
   - extract insights.
##  Matplotlib :
 - You will need its subpackage pyplot
 - To plot data as a line chart, we call plt-dot-plot and use our two lists as arguments. 
 - he first argument corresponds to the horizontal axis, and the second one to the vertical axis. 
 ```
 import matplotlib.pyplot as plt
 year = [1950, 1970, 1990, 2010]
 pop = [2.517, 3.692, 5.263, 6.974]
 plt.plot(year, pop)
 plt.show()
 ```
 
## Histogram :
  - Explore your data. 
  - Get an idea about the distribution.
  - start by importing the pyplot package that's inside matplotlib.
  - Next, you can use the `hist` function (plt.hist(x, y))
  - x should be a list of values you want to build a histogram for. You can use the second argument, bins, to tell Python into how many bins the data should be divided. 
  ```
  import matplotlib.pyplot as plt
  values = (0, 1, 5, .05, 9, .03, .2, .4, 2, .7, 8, 9)
  plt.hist = (values, bins=3)
  plt.show()
  ```
## Customization :
  - Many options :
   - Different plot types
   - Many customizations
  - Choise depenson :
   - Data
   - Story you want to tell
   ```
  import matplotlib.pyplot as plt
  year = [1950, 1970, 1990, 2010]
  pop = [2.517, 3.692, 5.263, 6.974]
  plt.plot(year, pop)
  #add more data
  year = [1800, 1850, 1900]+year
  pop = [1.0, 1.26, 1.65]+pop
  #to add names to labels
  #to add title
  plt.title=('World population')
  plt.xlabel=('year')
  plt.xlabel=('Population')
  #the curve shifts up
  plt.yticks=[0, 2, 4, 6, 8, 10]
             ['0', '2B', '4B', '6B', '8B', '10B']
  plt.show()
  ```
   
  
  