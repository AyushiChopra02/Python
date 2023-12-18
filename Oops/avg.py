class Student :
    school = 'snsps'
    def __init__(self , m1 , m2 , m3):
        self.m1  = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 +self.m3 )/3
    def getm1(self):
        return self.m1
    
    def setm1(self,value):
        self.m1= value
s1 = Student(34,45,22)
s2 = Student(88,4,33)

print(s1.avg())