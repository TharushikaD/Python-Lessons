# from util.bmi import BMI

# the_height = float(input("enter the height in cm: "))
# the_weight = float(input("enter the weight in kg: "))
# print(BMI.bmi_calculator(height=the_height , weight= the_weight))

# from traffic_light.traffic import Traffic

# colorr = input("What's the Color: ")
# print(Traffic.action(color =colorr))

class vehicle:

    # create a constructor
    def __init__(self,_tyres,_headlight,_seats) -> None:
        self.tyres = _tyres
        self.headlight = _headlight
        self.seats = _seats

    def drive_mode(self):
            return "mode"
        
    def speed(self):
            return "speed"
        
    def condition(self):
            return "condition"
        
    def upgrade(self):
            return self.headlight + ""+ self.seats + "" + self.tyres
    
vehicle = vehicle(" big "," recaro "," dsi")
print(vehicle.upgrade())
    