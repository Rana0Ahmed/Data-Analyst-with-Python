# Notes
## I
## Making a scatter plot :
  - A scatter plot allows us to show where each data point sits on a grid.
  - Line plots let us visualize ordered data points, but scatter plots are a great way of viewing un-ordered points.
  - In matplotlib, we create scatter plots by using the command `plt.scatter`.
  ```
  plt.scatter(df.age, df.height)
  ```
  - Changing marker transparency :
    - To plot many points on the same scatter plot, things can get chaotic. We can't see if we've plotted many layers of points or just a single layer.
    - We can make it easier to read by using a new keyword: `alpha`. Alpha accepts a number between (0 and 1) and makes each marker transparent.
    ```
    plt.scatter=(df.x_data, df.y_data, alpha=.01)
    ```
    <img src="https://i0.wp.com/cmdlinetips.com/wp-content/uploads/2019/04/Scatter_Plot_transparent_with_log_scale_Seaborn_Python.jpeg?resize=600%2C400" width="350">
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## II
## Making a bar chart :
  - To visualize a comparison of categorical data function `plt.bar` .
  - We provide two arguments to the function, the labels for each bar, and the height of each bar.
  - The x-axis is labeled for us, we only need to add a label for the y-axis using plt-dot-ylabel.
  ```
  plt.bar(df.precinct, df.pets_abducted)
  
  plt.y_label('Pet Abductions')
  plt.show()
  ```
  <img src="https://www.readingrockets.org/images/articles/43814-graph.jpg" width="350">
  
  - Horizontal bar charts :
    - We simply use the function `plt.barh` instead of `plt.bar`
    
    <img src="https://datasciencemadesimple.com/wp-content/uploads/2017/02/R-Horizontal-bar-chart.png" width="350">
    
  - Adding error bars :
    - To show some sort of error associate with our average, such as the standard deviation or standard error of the mean
    - By using the keyword argument `yerr` after our the first two positional arguments in `plt.bar`.
    ```
    plt.bar(df.precinct, df.pets_abducted, yerr=df.error)
    ```
    <img src="https://www.statology.org/wp-content/uploads/2021/08/errorbarR2.png" width="350">
    
  - Stacked bar charts :
    - We stack the ()bars on top of the ()bars by using the keyword `"bottom"`
    - Normally, a bar chart will start each bar at 0, but we can add the keyword `"bottom"` to `plt.bar` and feed in the heights
    - Also added the keyword argument `"label"` for each bar plot to create our legend.
    
    ```
    plt.par(df.precinct, df.dog, label="Dog")
    plt.par(df.precinct, df.cat, bottom=df.dog, label="Cat")
    
    plt.legend()
    plt.show()
    ```
    
    <img src="https://tse4.mm.bing.net/th?id=OIP.5nV3Jggs0ah5De3FJmfCXwHaFR&pid=Api&P=0" width="350">
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    
    
    
    