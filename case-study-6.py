'''
1.Read FairDealCustomerData.csv
2.Name field contains full name –use regular expression to separate title, first name, last name
3.Store the data in Customer Class
4.Create Custom Exception –CustomerNotAllowedException
'''
'''
I wanted to import a file with a class. But since the class name was the same as the file name, I got an error
'''
import re


class CustomerNotAllowedException(Exception):
    def __init__(self, text):
        self.txt = text


class Customer():
    title = ""
    fname = ""
    lname = ""
    isblacklisted = 0;

    def __init__(self):
        self.title = ""

    def __str__(self):
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + self.isblacklisted

    def setIsblacklisted(self,isblacklisted):
        self.isblacklisted = isblacklisted

    def isblacklisted(self):
        return self.isblacklisted

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setFname(self,fname):
        self.fname = fname

    def getFname(self):
        return self.fname

    def setLname(self,lname):
        self.lname = lname

    def getLname(self):
        return self.lname

    def createOrder(self):
        try:
            if self.isblacklisted == 1:
                raise CustomerNotAllowedException('CustomerNotAllowedException')
        except CustomerNotAllowedException as mr:
            print(mr)
        else:
            productname = input('input productname: ')
            productcode = input('input product code: ')
            self = OrderReturn()


class OrderReturn(Customer):
    type = 'Order'


Customers = ['customer'+str(i) for i in range(532)]
list = []
with open('FairDealCustomerData.csv', 'r') as f:
    for i in Customers:
        for line in f:
            i = Customer()
            i.title = re.findall('\w+', line)[1]
            i.fname = re.findall('\w+', line)[2]
            i.lname = re.findall('\w+', line)[0]
            i.isblacklisted = re.findall('\w+', line)[3]
            list.append(i)



costumer1 = Customer()
costumer1.isblacklisted = 0
costumer1.createOrder()