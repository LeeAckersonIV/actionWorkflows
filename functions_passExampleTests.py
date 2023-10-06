from typing import Union

def area_of_rectangle(width: Union[float, int], height: Union[float, int]):
    area = width * height
    return area
    """ Calculates the area of a rectangle

    Function takes in two variables from a rectangle of intereset: width & height. Each can be either a float
    or an integer. These variables and then multiplied by eachother to produce the area.

    Args:
        width: The width of the rectangle of interest, represented as a number in either float or integer form.
        height: The height of the rectangle of interest, represented as a number in either float or integer form.

    Returns:
        area: The resulting area determined by multiplying rectangle height by width. 

    Raises:
        error raised if input are not numbers. 
    """

def perimeter_of_rectangle(width: Union[float, int], height: Union[float, int]):
    perimeter = (2 * width) + (2 * height)
    return perimeter
    """ Calculates the perimeter of a rectangle

    Function takes in two variables from a rectangle of intereset: width & height. Each can be either a float
    or an integer. These variables and then doubled and summed to produce the perimeter of the rectangle.

    Args:
        width: The width of the rectangle of interest, represented as a number in either float or integer form.
        height: The height of the rectangle of interest, represented as a number in either float or integer form.

    Returns:
        area: The resulting perimeter determined by doubling the width and height and the summing the resulting values. 

    Raises:
        error raised if input are not numbers. 
    """
