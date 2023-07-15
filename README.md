Library
1. Used to extract cordinates from a graph Image.
1. Published at pypi:  https://pypi.org/project/graph-cordinates/
2. Install using: pip install graph-cordinates or pip install graph_cordinates
3. How to use:
   a. import graph_cordinates.graph_cordinates as gc \n
   b. gc.get_graphcordinates(image_path,x_range,y_range,background_value)
   c. Will return an array of 2D cordinates: [[x1,y1], [x2,y2], .......n-points]  ; n=pixel width of Image

How to pass arguments-
1. image_path == path to a graph image
2. x_range    == [Value of left most point on graph's x-axis, Value of right most point on graph's x-axis]
3. y_range    == [Value of bottom most point on graph's y-axis, Value of top most point on graph's y-axis]
4. background_value ==0 or 1
     0: When the graph's background color is relatively darker than the curve
     1: Otherwise

Caution- 
  Try to pass the Image by erasing the axes
  

  
