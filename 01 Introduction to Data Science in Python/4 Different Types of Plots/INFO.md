# Notes
## I
- Making a scatter plot :
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
    
