# my_thermo_stat()
## Function Purpose
The 'my_thermo_stat()' function handles the status of a thermostat. It is designed to recognize when the temperature fluctutates too far (+ or - 5 degrees) in either direction from an established set point, and react accordingly. 

## Function Inputs & Outputs
'my_thermo_stat()' takes in two inputs, both as type **integer**. The first input is the measured or current temperature, and the second input is the desired temperature. The output is of type **string**, and simply states the status of the thermostat (**Heat**, **AC**, or **off**).
## Automatic API
:::example_functions.my_thermo_stat