import re
'''
1.Write a Regular Expression that will match a date that follows the following standard “YYYY-MM-DD”.
'''
# date = r'\d{4}-([1-9]|1[0-2])-(\[1-9]|[12][0-9]|3[0-1])'
# aa = input('input date:')
# if re.match(date,aa):
#     print('yes')
# else:
#     print('No')
'''
2.Write a Regular Expression that will match a traditional SSN.
'''
# SSN = r'\d{3}-\d{2}-\d{4}'
# aa = input('input SSN:')
# if re.match(SSN,aa):
#     print('yes')
# else:
#     print('No')
'''
3.Write a Regular Expression that will match an IPv4 address.
'''
# IPv4 = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
#        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
# aa = input('input IPv4:')
# if re.match(IPv4,aa):
#     print('yes')
# else:
#     print('No')
'''
4.Write a Regular Expression that will match an email address.
'''
# email = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
# aa = input('input email:')
# if re.match(email,aa):
#     print('yes')
# else:
#     print('No')
'''
5.Below is the program to calculate the area of a box. Check how it is working. Correct the program (if required).
class Box:
    def area(self):
        return width * height
    def __init__(self, width, height):
        self.width = width
        self.height = height
# Create an instance of Box.
x = Box(10, 2)
# Print area.
print(x.area())
'''
# class Box:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
#     def area(self):
#         return self.width * self.height
#
#
# # Create an instance of Box.
# x = Box(10, 2)
# # Print area.
# print(x.area())
'''
6.Write a program to calculate distance so that it takes two Points (x1, y1) and (x2, y2)
as arguments and displays the calculated distance, using Class.
'''
# class A:
#     def __init__(self, x1, y1):
#         self.x1 = x1
#         self.y1 = y1
#
#
# class B:
#     def __init__(self, x2, y2):
#         self.x2 = x2
#         self.y2 = y2
#
#
# class Calculator(A,B):
#     def __init__(self, x1, y1, x2, y2):
#         super().__init__(x1, y1)
#         super().__init__(x2, y2)
#     def calc(self):
#         return self.x1
#
#
# # Create an instance of Calculator.
# x = Calculator(10, 2, 11, 13)
#
# # Print calc.
# print(x.calc())
'''
7.Correct the below program so that output should appear like this.
[Expected output:
x-value: 5 
y-value: 7
'''
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return "x-value: " + str(self.x) + " y-value: " + str(self.y)
#     def __add__(self,other):
#         Point.x = self.x+other.x
#         Point.y = self.y+other.y
#         return Point(Point.x, Point.y)
# p1 = Point(3,4)
# p2 = Point(2,3)
#
# print (p1+p2)
