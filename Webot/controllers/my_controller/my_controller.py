"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

back_leftMotor = robot.getMotor("back left wheel")
front_leftMotor = robot.getMotor("front left wheel")
back_rightMotor = robot.getMotor("back right wheel")
front_rightMotor = robot.getMotor("front right wheel")

# Set the target speed of the motors
back_leftMotor.setPosition(float("inf"))
front_leftMotor.setPosition(float("inf"))
back_rightMotor.setPosition(float("inf"))
front_rightMotor.setPosition(float("inf"))

# Set the target speed of the motors
back_leftMotor.setVelocity(5.0)
front_leftMotor.setVelocity(5.0)
back_rightMotor.setVelocity(5.0)
front_rightMotor.setVelocity(5.0)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
