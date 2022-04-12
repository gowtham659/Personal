class student:
    def __init__(self,name,age) -> None:
        self.n = name
        self.a = age
    def display(self):
        print("name:%s and age:%d"%(self.n,self.a))
s = student("gowtham",22)
s1 = student("harsha",90)
s2 = student("harish",39)
s3 = student("sahith",88)

s.display()
s1.display()

