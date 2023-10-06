# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

from typing import Union


def my_adder(a: Union[float, int], b: Union[float, int], c: Union[float, int]):
    # this is the summation
    out = a + b + c
    return out
    """ Calculates the sum of three numbers

    Function takes in three variables: a, b, and c. Each can be either a float
    or an integer. These variables and then added together to produce the resulting sum.

    Args:
        a: User defined number, represented as either an integer or float.
        b: User defined number, represented as either an integer or float.
        c: User defined number, represented as either an integer or float.

    Returns:
        area: The resulting area determined by multiplying rectangle height by width. 

    Raises:
        error raised if input are not numbers. 
    """

def my_thermo_stat(temp: int, desired_temp: int):
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status
    """ Changes the status of the thermostat based on temperature and desired temperature

    Function takes in two variables: temp & desired_temp. These values are both integers, and used by the 
    function as a means of comparison to dictate the status of the thermostat. If it registers that the temperature 
    it more than 5 degrees less or greater than the desired temp than it changes the thermostat status to 
    'Heat' and 'AC', respectively. If the temperature is not outside of the 10 degree window, thermostat is set to 'off'.

    Args:
        temp: The current temperature reading by the thermostat, as an integer.
        desired_temp: The user defined desired temperature, as an integer.

    Returns:
        status: represents the status of the thermostat, either as 'Heat', 'AC', or 'off', all as a string. 

    Raises:
        error raised if input are not numbers, and furthermore integers. 
    """


def have_digits(s: str):
    out = 0
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
    return out
    """ Checks if a string has digits in it

    Function takes in one variable: s, which is a string of any length. The function takes the string and iterates
    though it character by character to determine wether each character is a digit or not. If a single digit is identified,
    the function returns the value of 1, otherwise the output value is 0.

    Args:
        s: a string of any length.

    Returns:
        the function returns binary answers identifying the presence of a digit. If a single digit is identified,
        the function returns the value of 1, otherwise the output value is 0.
   
    Raises:
        error raised if input is not a string.
    """
