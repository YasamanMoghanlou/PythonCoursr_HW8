print("--unit 12--")
print("12.")
print("a.")
try:
    print ("Begin")
    x = int (input())
    print (x)
    print ("End")
except ValueError:
    print ("Invalid Value")
print("_____________________")

print("b.")
print ("Begin")
try:
    x = int(input())
    print(x)
except ValueError:
    print ("Wrong!")
print("end")
print("_____________________")


print("c.")
print ("Begin")
try:
    x = int(input())
    print(x)
except ValueError:
    print("Invalid Value")
except IndexError:
    print ("Wrong!")
print("End")
print("_____________________")


print("d.")
print ("Begin")
try:
    x = int(input())
    print(x)
except Exception:
    print ("Wrong!")
print ("End")
print("_____________________")


print ("e.")
print ("Begin")
try:
    x = int(input())
    print (x)
except ValueError:
    print ("Wrong!")
else:
    print ("Wow")
print ("End")
print("_____________________")


print ("f.")
print ("Begin")
try:
    x = int(input())
    print (x)
except ValueError:
    print ("Wrong!")
finally:
    print ("Done")
print ("End")
print("_____________________")


print ("g.")
print ("Begin")
try:
    x = int(input())
    print (x)
except ValueError:
    print ("Wrong!")
else:
    print ("Wow")
finally:
    print("Done")
print ("End")
print("_____________________")

print("13.")
print("the problem is that except exception has written before except ValueError ")

print("_____________________")
print("14.")
print("the problem is that except exception shouldn't have been first!!")
print()
print()

print("__unit13__")
print("9. ")
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return 2*self.radius*3.14

r = int(input("please enter the radius: "))
NewCircle = Circle(r)
print("Area of the circle: ", NewCircle.area())
print("Perimeter of circle: " ,NewCircle.perimeter())
print("_____________________")


print("11. ")
class Widget:
    def __init__(self, v = 40):
        if v >= 40:
            self.value = v
        else:
            self.value = 0
    def get(self):
        return self.value
    def bump(self):
        if self.value < 50:
            self.value += 1
def main ():
    w1 = Widget()
    w2 = Widget(5)
    print(w1.get())
    print(w2.get())
    w1.bump()
    w2.bump()
    print(w1.get())
    print(w2.get())
    for i in range (20):
        w1.bump()
        w2.bump()
    print(w1.get())
    print(w2.get())
if __name__ == '__main__':
    main()
    
print("a. the program will print 40, 0, 41, 1, 50, 21 respectively")

