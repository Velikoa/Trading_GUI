
class Employee(object):
    def __init__(self, name):
        self.name = name

    def greeting(self, other):
        print "Hello, %s" % other

class CEO(Employee):
    def greeting(self, other):
        print "Get back to work, %s" % other.name

ceo = CEO("John")
employee = Employee("Mr H")
employee.greeting(employee.name)
ceo.greeting(ceo)

# from Tkinter import *
#
# bye = 'Goodbye'
#
#
# def update_text():
#     label.config(text=bye)
#
#
#
# if want to select only specific elements of a list
# j = [1,5,18,25,-5,-10,4]
#
# j2 = [i for i in j if i >= 0]
#
# print j2
#
#
# root = Tk()
# root.title("My Title")
# label = Label(root, text="Hello")
# label.pack()
# button = Button(root, text="Click Me", width=30, command=update_text)
# button.pack()
# root.mainloop()

import matplotlib.pyplot as plt
import pandas as pd


#Our x-axis
a = [1,2,5,13,17,21]
#Our y-axis
b = [2,4,9,3,7,5]
#Our second y-axis
c = [14,18,36,21,27,41]

ax1 = plt.subplot(111)
plt.xlabel("Random X Axis")
plt.ylabel("First Y Axis")

ax1.plot(a,b)
ax1.set_label("Random graph")

ax2 = plt.twinx(ax1)

ax2.bar(a,c, color="red")

plt.show()

