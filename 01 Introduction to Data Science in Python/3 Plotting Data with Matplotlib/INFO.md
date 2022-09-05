# Notes :
## I.
## Creating line plots using another Python module (matplotlib) :
- Introducing Matplotlib :
  - Import the module matplotlib, Data Scientists only load in the submodule pyplot and use the alias plt.
  ```
  from matplotlib import pyplot as plt
  ```
  - Once we've loaded our module, we can use the functions plt-dot-plot and plt-dot-show to create and display our line plot.
  
  ```
  plt.plot(x_values, y_values)
  
  plt.show()
  ```
  <img src ="https://tse3.mm.bing.net/th?id=OIP.V9Jery-6LudgGZUHPKDL0QHaFs&pid=Api&P=0" width="350">
  
  - plt.plot(ransom.letter, ransom.frequency) 
    - We begin with the name of the function: plt-dot-plot
    - first argument is the x-values we want to plot. In this case, we use the letter column from the DataFrame ransom.
    - We use the frequency column from the DataFrame ransom
  - Displaying the Results :
    - We use a second function :`plt.show`
    - This function takes no arguments. You just type it, and then your plot will pop open in a new window.
      
  - Multiple Lines :
    -  Just add a second plt-dot-plot command before adding plt-dot-show.
    ```
    plt.plot(data1.x_values, data1.y_values)
    ```
    ```
    plt.plot(data2.x_values, data2.y_values)
    ``` 
    ```
    plt.show()
    ```
  <img src ="https://matplotlib.org/1.4.1/pyplots/pyplot_three.hires.png" width="350">
  
     In this example, we plotted two different datasets: data1, which represents a straight line and data2, which represents a parabola.
       
     Matplotlib will automatically give the two lines different colors.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## II.
# Adding text to plots
- Axes and title labels :
  - We can label the horizontal (or "x") axis using the command plt-dot-xlabel. 
  ```
  plt.xlabel("Label")
  ```
  
  - we can label the vertical (or "y") axis using the command plt-dot-ylabel.
  ```
  plt.ylabel("Frequency")
  ```
  
  - We can give our plot a title by using plt-dot-title.
  ``` 
  plt.title("Ranson Note Letter")  
  
  ```
- Legends :
  - If we have multiple lines in the same plot, we'll want to add a legend. There are two steps for adding a legend :
    - First, we must add the keyword argument label to each instance of `plt.plot`.
    - We must add a final function: `plt.legend`. Like `plt.show`, plt.legend does not take any arguments.
    ```
    plt.plot(Aditya.days,aditya.cases,label="Aditya")
    plt.plot(deshaun.days,deshaun.cases,label="Deshaun")
    plt.plot(mengfei.days,mengfei.cases,label="Mengfei")
    
    plt.legand()
    ```
    
    
    
     
    