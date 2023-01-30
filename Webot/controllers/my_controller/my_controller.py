"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from time import sleep

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

back_leftMotor = robot.getMotor("back left wheel")
front_leftMotor = robot.getMotor("front left wheel")
back_rightMotor = robot.getMotor("back right wheel")
front_rightMotor = robot.getMotor("front right wheel")

back_leftSensor = robot.getPositionSensor("back left wheel sensor")
front_leftSensor = robot.getPositionSensor("front left wheel sensor")
back_rightSensor = robot.getPositionSensor("back right wheel sensor")
front_rightSensor = robot.getPositionSensor("front right wheel sensor")

# Set the target speed of the motors
back_leftMotor.setPosition(float("inf"))
front_leftMotor.setPosition(float("inf"))
back_rightMotor.setPosition(float("inf"))
front_rightMotor.setPosition(float("inf"))

# Set the target speed of the motors

#back_leftMotor.setVelocity(5.0)
#front_leftMotor.setVelocity(5.0)
#back_rightMotor.setVelocity(0.0)
#front_rightMotor.setVelocity(0.0)


# Set the distance Sensor
frontSensor1 = robot.getDistanceSensor("so1")
frontSensor1.enable(timestep)

frontSensor2 = robot.getDistanceSensor("so2")
frontSensor2.enable(timestep)

frontSensor3 = robot.getDistanceSensor("so3")
frontSensor3.enable(timestep)

frontSensor4 = robot.getDistanceSensor("so4")
frontSensor4.enable(timestep)

frontSensor5 = robot.getDistanceSensor("so5")
frontSensor5.enable(timestep)

frontSensor6 = robot.getDistanceSensor("so6")
frontSensor6.enable(timestep)

#Get the gps
gpsSensor = robot.getGPS("gps")
gpsSensor.enable(timestep)
# Main loop:

while robot.step(timestep) != -1:

    gpsSensorValue = gpsSensor.getValues()
    #print(gpsSensorValue)

    # Obstacle detector
    frontSensorValue1 = frontSensor1.getValue()
    frontSensorValue2 = frontSensor2.getValue()
    frontSensorValue3 = frontSensor3.getValue()
    frontSensorValue4 = frontSensor4.getValue()
    frontSensorValue5 = frontSensor5.getValue()
    frontSensorValue6 = frontSensor6.getValue()

    sum_distanceSensor = frontSensorValue1 + frontSensorValue2+frontSensorValue3+frontSensorValue4+frontSensorValue5+frontSensorValue6


  
    # If the front sensor value is less than a certain threshold
    if sum_distanceSensor > 200:
        # Change the direction of the robot
        
        back_leftMotor.setVelocity(6.4)
        front_leftMotor.setVelocity(6.4)
        back_rightMotor.setVelocity(-5.0)
        front_rightMotor.setVelocity(-5.0)

    else:
        # Keep moving forward
        back_leftMotor.setVelocity(5.0)
        front_leftMotor.setVelocity(5.0)
        back_rightMotor.setVelocity(5.0)
        front_rightMotor.setVelocity(5.0)

   
# Enter here exit cleanup code.
