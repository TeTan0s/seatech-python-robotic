from time import sleep
import random

class Robot():
    __name = "<unnamed>"
    __power = False
    __movement = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']

    	
    def __init__(self, name=None):
      if name:
        self.__name = name
      self.__current_state = self.__states[0]
      self.__power = False
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """
    

    def boot(self):
        if self.__power == False :
            self.__current_state = self.__states[1]
            self.__power = True
        
        elif self.__power == True:
            print("error the robot is already on")
        

    def shutdown(self):
        if self.__power == True :
            self.__current_state = self.__states[0]
            self.__power = False
        elif self.__power == False :
            print("error the robot is already off")


    def charge(self, battery=0):
        battery_max = 100
        self.__battery_level = battery
        if battery < 100 :
            
            for i in range (100-battery):
                print("battery : ", battery+i)
                sleep(0.1)

            self.__battery_level = battery_max
            battery = battery_max
            print("the robot is 100 charged")
        else :
            print("the robot is already 100 charged")


    def movement_on(self, speed=0):
       
        if self.__power == True:  #Le robot doit être allumé
            if self.__battery_level>0: #Le robot doit avoir de la batterie

                #Coeur fonction mouvement
                if self.__movement == False :
                    self.__movement == True
                    self. __current_speed = speed
                    speed = random.randint(1,20)
                    print("the robot is moving")
                    print("speed of the robot :", speed)
                elif self.__movement == True :
                    print("the robot is already moving")

            else :
                print("you must have to charge on the robot")
        else :
            print("you must have to turn on the robot")

    
    def movement_off(self,speed = 0):
        #Le robot est à l'arrêt
        if self.__movement == True :
            self.__movement == False
            self. __current_speed = speed
            print("the robot is not moving")

        elif self.__movement == False :
            print("the robot isn't already moving")
        

            


    #define robot

r = Robot("walle")
r.boot()
r.charge(100)
r.movement_on()
    