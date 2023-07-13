Library
1. Viewa at pypi:  https://pypi.org/project/graph-cordinates/
2. Install using cmd: PIP install graph_cordinates
3. Import in a python file: from graph_cordinates.graph_cordinates import get_graphcordinates
4. To use the function: get_graphcordinates(image_path,x_range,y_range,background_value)
5. It is used to extract graph points from a graph Image.
6. Anyone can access it by installing through: PIP install gpoints

How to pass arguments-
1. image_path ==path to a graph image
2. x_range    ==[Value of left most point on graph's x-axis, Value of right most point on graph's x-axis]
3. y_range    ==[Value of bottom most point on graph's y-axis, Value of top most point on graph's y-axis]
4. background_value ==0 or 1
     0: When the graph's background color is relatively darker than the curve
     1: Otherwise

Caution- 
  Try to pass the Image by erasing the axes
  
Return value-
  Will return a numpy array of structure-
    array = [[x1,y1], [x2,y2], .......n-points]  ; n=pixel width of Image
  

  
