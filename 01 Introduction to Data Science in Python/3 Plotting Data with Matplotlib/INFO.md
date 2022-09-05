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
    
    plt.legend()
    ```
- Arbitrary text :
  - To add a quick note directly onto our plot. We can do this by using the function `plt.text`.
  - This function takes three arguments: the x-coordinate where we want to put the text, the y-coordinate where we want to put the text, and the text we want to display as a string.
  ```
  plt.text(xcoord,ycoord,"Text Message")
  plt.text(5,9,"Unusually low h frequency")
  ```
- Modifying text :
  - If we want to change the size of `font`, we can use the keyword argument `fontsize` and pass in a float.
  ```
  plt.title("plot title", fontsize=20)
  ```
  - If we want to change the `color of font`, we can use the keyword argument `color` and pass in a string.
  ```
  plt.legand(color="green")
  ```
  
-  Changing line color :
```
plt.plot(x, y1, color="orange")
```
- Changing line width :
```
plt.plot(x, y1, linewidth=3)
```
-  Changing line style :
```
plt.plot(x, y1, linestyle="--")
```
- Adding markers :
```
plt.plot(x, y1, marker='x')
```
- Setting a style :
  - To make more drastic change to our graph. We can change the background, colors, and fonts for our entire graph by setting a style
  - The function `plt.style.use` accepts several different strings which correspond to different plotting styles
  ```
  plt.style.use('ggplot')
  ```


    
    
     
    