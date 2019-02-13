"""
class rectangle:
	l=12;
	b=10;
	a=l*b;
class circumference:
	l=10;
	b=15;
	c=2*(l+b);
r1=rectangle()
r2=circumference()
print("Length = ",r1.l)
print("Breadth = ",r1.b)
print("Area Of rectangle = ",r1.a)
print("Circumference of Rectangle = ",r2.c)
"""
"""
class rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
		self.a=l*b
p1=rectangle(10,15)
print("Area of Rectangle = ",p1.a)
"""
"""
import math
class circle:
	def __init__(self,r):
		self.r=r
		self.a=math.pi*r**2
c1=circle(2)
print("Area of Circle = ",c1.a)
"""
"""
import math
class circle:
	def areaofcircle(self,r):
		self.r=r
		return math.pi*r**2
c1=circle()
print("Area of Circle = ",c1.areaofcircle(10))
"""
"""
Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.
"""
"""
import math
class circle:
	def getArea(self,radius):
		self.radius=radius
		return math.pi*radius**2
	def getCircumference(self,radius):
		self.radius=radius
		return 2*math.pi*radius
c1=circle()
print("Area Of Circle = ",c1.getArea(2))
print("Circumference Of Circle = ",c1.getCircumference(4))
"""
"""
class Temperature:
	def __init__(self,c,f):
		self.c=c
		self.f=f
	def convertFahrenheit(self):
		return (9/5)*self.c+32
	def convertCelsius(self):
		return (self.f-32)*(5/9)
t1=Temperature(5, 100)
print("Fahrenheit = ",t1.convertFahrenheit())
print("Celsius = ",t1.convertCelsius())
"""
