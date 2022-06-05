print(11)

print("1.11")
print("first of all we use () in tuples, then we cannot mutate or change items in tuples because tuples are immutable")
print("_____________________")

print("2.11")
print("Because list has a variable size while a tuple has a fixed size")
print("_____________________")


print("3.11")
print("tuples are immutable")
print("_____________________")


print("4.11")
print("it is not ordered")
print("_____________________")


print("5.11")
a = (1, 2, 3, 4, 5, 6, 7, 8)
A, B, C, D, E, F, G, H = a
s = C, D, E, F
print (s)
print("_____________________")

print("6.11")
a = (1, 2, 3, 4, 5, 6, 7, 8)
s = a [3:7]
print (s)
print("_____________________")


print("7.11")
tpl = (7, 10, -3, 18, 6, 10)
x, a, b, c, d, y = tpl
print (x, y)
print("_____________________")


print("8.11")
def product_number(tpl):
    a = 1
    for i in tpl:
        a = a*i

    return a

tpl =input ("Enter floating numbers : ")
if tpl =="" or tpl ==None:
    answer = product_number(tpl)
    print(answer)
else:
    tpl = tuple(float(x) for x in tpl.split(","))
    answer = product_number(tpl)
    print(answer)
print("_____________________")



print("9.11")
def zero_sum(tpl):
    a = 0
    for i in tpl:
        a = a+i
    if a ==0:
        return True
    elif a!=0:
        return False
    else:
        return True

    
#tpl = (2, 3, -5)
tpl =input ("please enter integers: ")
if tpl =="" or tpl ==None:
    answer = zero_sum(tpl)
    print(answer)
else:
    tpl = tuple(int(x) for x in tpl.split(","))
    answer = zero_sum(tpl)
    print(answer)
print("_____________________")


print("10.11")
print("because it permits access based on a key")
print("_____________________")


print("11.11")
print("the statement adds the key and pairs it with the value on the right of the assignment operator")
print("_____________________")


print("12.11")
print(" print(d[Fred]) ")
print("_____________________")


print("13.11")
print("A python KeyError exception is what is raised when you try to access a key that isn't in a dictionary")
print("_____________________")


print("14.11")
print("A python KeyError exception is what is raised when you try to access a key that isn't in a dictionary Python's official documentation says that the KeyError is raised when a mapping key is accessed and isn't found in the mapping")
print("_____________________")


print("15.11")
print("Dictionaries are mutable")
print("_____________________")


print("16.11")
d = {
    3 : 0,
    5 : 1,
    10: 1,
    8 : 2,
    15: 4
}

print (d)   #it prints: {3: 0, 5: 1, 10: 1, 8: 2, 15: 4}


for x in d:
    print (x)   # it prints: 3
                           # 5
                           # 10
                           # 8
                           # 15
        
for x in d.keys():
    print (x)   # it prints: 3
                           # 5
                           # 10
                           # 8
                           # 15
for x in d.values():
    print (x)   #it prints: 0
                          # 1
                          # 1
                          # 2
                          # 4
                          
                          
print("_____________________") 


print ("17.11")
print("elements in dictionaries are ordered")
print("_____________________")


print ("18.11")
print("light on/off")
from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
def do_button_press():
    global color
    if color == 'black':
        color = 'yellow'
        canvas.itemconfigure(yellow_lamp, fill='yellow') #turn yellow on

    elif color == 'yellow':
        color = 'black'
        canvas.itemconfigure(yellow_lamp, fill='black') #turn off


color = 'black'     
root = Tk ()        


root.title("light")

frame = Frame(root)    
frame.pack()           


canvas = Canvas(frame, width=150, height=200)

#set up the visual aspects of the light

#yellow lamp
yellow_lamp = canvas.create_oval(70, 150, 130, 80, fill='black')


#create a graphical button and ensure it calls the do_button_press function when the user presses it
button = Button(frame, text='turn on/ turn off', command=do_button_press)

button.grid(row=0, column=0)
canvas.grid(row=0, column=1)


root.mainloop()
print("_____________________")



print ("19.11")
print("TicTacToe")
print("_____________________")


print ("20.11")
print ("because if you want to use {} you must contain at least one element")
print ("if not you can use () it will produce a set with no elements")
print("_____________________")



print ("21.11")

a = list()

print("Values of a:", a)
print("_____________________")


print ("22.11")
print ("sets are immutable")
print("_____________________")


print ("23.11")
a = {20, 19, 2, 10, 7}
b = {4, 10, 5, 6, 9, 7}
c = {10, 19}

print (a)             # the answer {2, 19, 20, 7, 10}
print (20 in a)       # True
print (20 not in a)   # False
print (a & b)         # {10, 7} 
print (a | b)         # {2, 4, 5, 6, 7, 9, 10, 19, 20}
print (c < a)         # True
print (c <= a)        # True
print (c <= b)        # False
print (a <= a)        # True
print (a < a)         # False
print (len(a))                       # 5
print ({x+2 for x in range(10)})     # {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print ({x-2 for x in a})             #{0, 5, 8, 17, 18}
print ({x-2 for x in a if x<10 })    #{0,5}
