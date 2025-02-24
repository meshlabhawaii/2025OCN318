# A series of examples that cover Python basics for OCN318.
#
# I'd like you to know how to do these by the end of the course:
#   Use computer to collect data at fixed interval
#   Get data/script in and out from a "headless" computer
#   Visualize collected data
#   Not freak out when a sensor comes with an "I2C/RS232" interface
#
# I will be very sad if by the end of the class you still reach for your TI "graphing" calculator for labs and homework.
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318


# Basic Data Types: int, float, bool, string...


# this defines a variable called "url" pointing to a STRING (more about this later):
url = 'http://knowyourmeme.com/memes/x-x-everywhere'

# This is a comment and is ignored by Python, but you alread know that.

# Primitive typess: boolean, integer, and float
a = True
print(a)
print(type(a))
a = 42
print(a)
print(type(a))
# any time you want to know what something is, type() it.
# type() is a built-in function, so it shows as purple in IDLE.

a = 42.1314008
print(a)
print(type(a))

# operations on int and float, just like everything you'd expect
a = 3 + 4
print(a)
a = 0.3 + 0.3 + 0.3
print(a)
# "What?!" https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html


# boolean (True/False)
false = True
true = False
print(true and true)
print(false and false)
print(false and true)
print(false or true)



# TEST
# What would these print?
a = 3
b = 4
a = 5 + b
print(a)

a = 3.0
b = 4
print(type(a + b))



# At this point you should know
#   how to assign numberic values to a variable
#   how to find out the type of a variable
#   int, float and bool basic operations




# Don't worry too much about not getting everything in the first class. This stuff is hard.
# https://www.explainxkcd.com/wiki/index.php/1168:_tar
#
# But everything covered here is only the basics. You should master them before the end of the course.
#
# Python has excellent documentation and tutorial:
# https://docs.python.org/3/tutorial
#
# And if you want challenges:
# https://github.com/norvig/pytudes/tree/master/ipynb
# (Open it on your own laptop. The Pi is probably too slow for it.)
#
# Meta:
# "Teach Yourself Programming in Ten Years"
# http://norvig.com/21-days.html
#
# Undergraduation
# http://www.paulgraham.com/college.html
# "The programs you write in classes differ in three critical ways from the ones you'll write in the real world: they're small; you get to start from scratch; and the problem is usually artificial and predetermined. In the real world, programs are bigger, tend to involve existing code, and often require you to figure out what the problem is before you can solve it."
