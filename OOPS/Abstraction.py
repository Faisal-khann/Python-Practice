# Abstraction is the hidding the implementation details of a class
# and only showing the essential features to the user
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False
        self.spd = False

    def start(self):
        self.cluch = True
        self.acc = True
        print("Car start....")

    def run(self):
        self.cluch = True
        self.acc = True
        self.spd = True
        print("Car runnig.....")

    def applyBreak(self):
        self.acc = False
        self.brk = True
        self.spd = False
        print("Apply Break....")

c1 = Car() # object
c1.start()
c1.run()
c1.applyBreak()
