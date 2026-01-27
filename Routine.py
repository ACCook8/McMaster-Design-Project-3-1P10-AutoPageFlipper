from Sensors import *
from gpiozero import LED
import sys
import time 

orientation_sensor = Orientation_Sensor()
led = LED(num)

def sensor_data():
    euler_angles = orientation_sensor.euler_angles()
    time.sleep(0.5)
    print("x:\t", euler_angles[0], "y:\t", euler_angles[1], "z:\t", euler_angles[2]) #prints sensor data for orientation sensor
    return euler_angles #returns orientation sensor data in form x,y,z

##double head nod initializes the page flipping sequence
def double_head_nod(list): ##checks to see if double head nod was performed in the last 5 seconds
    if (list[2] - list[0]) < -30:
        if (list[5] - list[3]) > 30:
            if (list[8] - list[6]) < -30:
                return True
    else: 
        return False

##currently there is a problem here. This will not do anything unless all conditions are met
##user has to perfectly time everything right now 

def left_or_right(list): ##left = false right = true
    x = 1 
    for i in list: 
        if list[x] - list[x-1] > 30:
            return True 
        elif list[x] - list[x-1] < 330:
            return False
        x +=1

                    
def rolling_avg(data):
    avg1 = sum(data[0])/10
    avg2 = sum(data[1])/10
    avg3 = sum(data[2])/10

    print("Avg X:", avg1, "Avg Y:", avg2, "Avg X:", avg3)
##Rolling average calculated for last 5 seconds

def led_blink(): ##blinks an led (must be used in a loop to have continuous blinking)
    led.on()
    time.sleep(0.5)
    led.off()

                    
def main():
    
    while True:

        data = [[],[],[]] 
        while len(data[0]) < 10: ## initializing ten values for sensor (last 5 seconds)
            values = sensor_data()
            data[0].append(values[0])
            data[1].append(values[1])
            data[2].append(values[2])
        
        rolling_avg(data) ##prints out rolling average for values in the last 5 seconds of sensor data

        var = double_head_nod(data[1])
        if var == True: 
            new_data = [[],[],[]] 
            while len(data[0]) < 10: ## initializing ten values for sensor (last 5 seconds)
                new_values = sensor_data()
                new_data[0].append(new_values[0])
                new_data[1].append(new_values[1])
                new_data[2].append(new_values[2])
                led.blink()## tells user system needs input left or head nod

        else: 
            continue
        
        valuenew = left_or_right(new_values[1])
    

                   
     
    

