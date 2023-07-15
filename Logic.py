""" Firstly we convert the Image to grayscale.
    Now a grayscale Image is a 2D matrix, whose each element has pixel intensity of range (0,255). O== Darkest pixel and 255==Brightest pixel.
    This function analyses all the pixels in a column(vertical) and records the height of the one corresponding to maximum or minimum intensity,
    ...depending on the background color is relatively dark or white as compared to the curve respectively.
    Since we are passing the range of x and y axis too, the function proportionately measures the y(x) at all the points.
"""

def get_graphcordinates(image_path,x_range,y_range,background_value):
    import matplotlib.pyplot as plt
    import numpy as np
    from PIL import Image

    image=Image.open(image_path)

    grayscale_image = image.convert('L')
    grayscale_image_arr=np.array(grayscale_image)
    length=grayscale_image_arr.shape[0]
    width=grayscale_image_arr.shape[1]
    
    if background_value==0: # If background is dark and plot is dark, we do the reverse
        grayscale_image_arr=255-grayscale_image_arr

    y_axis=[]
    for j in range(width):
        column=grayscale_image_arr[:,j]
        y=length-np.argmin(column)
        y_axis.append(y)
    y_axis=np.array(y_axis)
    x_axis=np.linspace(0,width,width)


    y_axis=y_range[0]+ ( y_axis*( y_range[1]-y_range[0] ) )/ length
    x_axis=x_range[0]+ ( x_axis*( x_range[1]-x_range[0] ) )/ width
    
    array=np.zeros((width,2))
    array[:,0]=x_axis
    array[:,1]=y_axis
    
    return array
