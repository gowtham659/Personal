class Polygon:
    def __init__(self,side) -> None:
        self.sides = side
        self.no_of_sides = []
    def inputsides(self):
        self.no_of_sides = [float(input("Enter side "+str(i)+" : ")) for i in range(1,self.sides+1)]
    def display(self):
        print(self.no_of_sides)

class Triangle(Polygon):
    def __init__(self, side) -> None:
        Polygon.__init__(self,side)
    def findArea(self):
        a,b,c = self.no_of_sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("Area of tri :%0.2f"%(area))

T = Triangle(3)
T.inputsides()
T.display()
T.findArea()
