class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']

    	
    def __init__(self, name=None):
      if name:
        self.name = name
      self.current_state = self.states[0]
      self.power = False
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """

    def boot(self):
        if self.power == False :
            self.current_state = self.states[1]
            self.power = True
        
        else:
            print("error the robot is already on")
        pass

    def shutdown(self):
        if self.power == True :
            self.current_state = self.states[0]
            self.power = False
        else:
            print("error the robot is already off")
        pass

    def charge(self):
        pass

    #define robot

r = Robot()
r.name = "walle"
    