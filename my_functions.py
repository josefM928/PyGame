#part a
#Function to returns pattern to generate a single
#horizontal line of desired width.
#Function accepts a width value and a single character as parameter.
def horizontal_line(width,ch):
    pattern=""
    for i in range(width):
        pattern += ch

    return pattern


#Function to returns pattern to generate a single vertical line.
#of desired height.The line is offset from the left side of the
#screen using shift value.
#Function accepts a shift value and a height value and
#a single character as parameter.
def vertical_line(shift,height,ch):
    pattern=""
    for i in range(height):
        for j in range(shift):
            pattern += " "

        pattern += ch+"\n"

    return pattern


# Function to returns pattern to generate two vertical
#lines of the desired height. The first line is along the left
#side of the screen. The second line is offset using the "width" value.
#Function accepts a width value and a height value and
#a single character as parameter.
def two_vertical_lines(width,height,ch):
    pattern=""
    for i in range(height):
        pattern += ch
        for j in range(width-2):
            pattern += " "
        pattern += ch+"\n"

    return pattern


#Testing the functions by calling with different sets of value
#Testing horizontal_line() function
print("Horizontal line, width = 5:")
temp = horizontal_line(5,'*')
print(temp)
print()

print("Horizontal line, width = 10:")
temp = horizontal_line(10,'+')
print(temp)
print()

print("Horizontal line, width = 15:")
temp = horizontal_line(15, 'z')
print(temp)
print()

#Testing vertical_line() function
print ("Vertical Line, shift=0; height=3:")
temp = vertical_line(0, 3,'!')
print(temp)
print()

print ("Vertical Line, shift=3; height=3:")
temp = vertical_line(3, 3,'&')
print (temp)
print()

print ("Vertical line, shift=6; height=5:")
temp = vertical_line(6, 5,'$')
print (temp)
print()

#Testing two_vertical_line() function
print ("Two Vertical Lines, widht=3; height=3:")
temp = two_vertical_lines(3, 3,'^')
print (temp)
print()

print ("Two Vertical Lines, widht=4; height=5:")
temp = two_vertical_lines(4, 5,'@')
print (temp)
print()

print ("Two Vertical Lines, widht=5; height=2:")
temp = two_vertical_lines(5, 2,'#')
print (temp)
print()

#0-9 digital display function part b
# Method to draw n vertical lines of length 'size'
# columns given in list l 
def n_vertical_line(l, size):
    s = ''
    for i in range(5):
        if i in l:
            s += '*'
        else:
            s += ' '

    for i in range(size):
        print(s)

# method to draw single vertical line of length 'size'
# at vertical position
def vertical_line(position, size):
    s = ""
    for i in range(position):
        s += ' '
    s += '*'

    for i in range(size):
        print(s)
def horizontical_line(width):
    for i in range(width):
        print('*', end='')
    print()

"""
Here are the 10 methods to generate 0-9 numbers
"""
def number_1(width):
    vertical_line(width - 1, 5)


def number_2(width):
    horizontical_line(width)
    vertical_line(width - 1, 1)
    horizontical_line(width)
    vertical_line(0, 1)
    horizontical_line(width)


def number_3(width):
    horizontical_line(width)
    vertical_line(width - 1, 1)
    horizontical_line(width)
    vertical_line(width - 1, 1)
    horizontical_line(width)


def number_4(width):
    n_vertical_line([0, width - 1], 2)
    horizontical_line(width)
    vertical_line(width - 1, 2)


def number_5(width):
    horizontical_line(width)
    vertical_line(0, 1)
    horizontical_line(width)
    vertical_line(width - 1, 1)
    horizontical_line(width)


def number_6(width):
    horizontical_line(width)
    vertical_line(0, 1)
    horizontical_line(width)
    n_vertical_line([0, width - 1], 1)
    horizontical_line(width)


def number_7(width):
    horizontical_line(width)
    vertical_line(width - 1, 4)


def number_8(width):
    horizontical_line(width)
    n_vertical_line([0, width - 1], 1)
    horizontical_line(width)
    n_vertical_line([0, width - 1], 1)
    horizontical_line(width)


def number_9(width):
    horizontical_line(width)
    n_vertical_line([0, width - 1], 1)
    horizontical_line(width)
    vertical_line(width - 1, 1)
    horizontical_line(width)


def number_0(width):
    horizontical_line(width)
    n_vertical_line([0, width - 1], 3)
    horizontical_line(width)

number_0(5)
print()
number_1(5)
print()
number_2(5)
print()
number_3(5)
print()
number_4(5)
print()
number_5(5)
print()
number_6(5)
print()
number_7(5)
print()
number_8(5)
print()
number_9(5)
print()


##print_number part c

"""
I
P
O
"""
def print_number(a,w,s):
    if a==0: #check for the conditions
        for i in range(5):
            if i==0 or i==4:
                for j in range(w):
                    print(s,end="") #loop for printing 0
                print()
            else:
                for j in range(w):
                    if j==0 or j==w-1:
                        print(s,end="")
                    else:
                        print(" ",end="")
                print()
        print()
    if a==1: #condition for 1
        for i in range(5):
            for j in range(w-1):
                print(" ",end="")
            print(s)
        print()
    if a==2: #condition for 2
        for i in range(5):
            if i%2==0:
                for j in range(w):
                    print(s,end="")
                print()
            if i==1:
                for j in range(w-1):
                    print(" ",end="")
                print(s)
            if i==3:
                print(s)
        print()
    if a==3: #condition for 3
        for i in range(5):
            if i%2==0:
                for j in range(w):
                    print(s,end="")
                print()
            else:
                for j in range(w-1):
                    print(" ",end="")
                print(s)
        print()
if a==4: #condition for 4
    for i in range(5):
        if i<2:
            for j in range(w):
                if j==0:
                    print(s,end="")
                if j==w-1:
                    print(s)
                if w-1>j>0:
                    print(" ",end="")
                if i>2: 
                    for j in range(w-1):
                        print(" ",end="")
                    print(s)
                if i==2:
                    for j in range(w):
                        print(s,end="")
                    print()
    print()
if a==5: #condition for 5
    for i in range(5):
        if i%2==0:
            for j in range(w):
                print(s,end="")
            print()
        if i==3:
            for j in range(w-1):
                print(" ",end="")
            print(s)
        if i==1:
            print(s)
    print()
if a==6: #condition for 6
    for i in range(5):
        if i%2==0:
            for j in range(w):
                print(s,end="")
            print()
        if i==3:
            print(s,end="")
            for j in range(1,w-1):
                print(" ",end="")
            print(s)
        if i==1:
            print(s)
    print()
if a==7: #condition for 7
    for i in range(5):
        if i==0:
            for j in range(w):
                print(s,end="")
            print()
        else:
            for j in range(w-1):
                print(" ",end="")
        print(s)
    print()
if a==8: #condition for 8
    for i in range(5):
        if i%2==0:
            for j in range(w):
                print(s,end="")
            print()
        else:
            print(s,end="")
            for j in range(1,w-1):
                print(" ",end="")
            print(s)
  
        print()
if a==9: #condition for 9
    for i in range(5):
        if i%2==0:
            for j in range(w):
                print(s,end="")
            print()
        if i==1:
            print(s,end="")
            for j in range(1,w-1):
                print(" ",end="")
            print(s)
        if i==3:
            for j in range(w-1):
                print(" ",end="")
            print(s)
        print()

# driver code
print_number(0,5,'*')
print_number(1,6,'*')
print_number(2,7,'*') # functions calling
print_number(3,8,'*')
print_number(4,9,'*')
print_number(5,10,'*')
print_number(6,11,'*')
print_number(7,12,'*')
print_number(8,13,'*')
print_number(9,14,'*')

##part d

"""
I
P
O
"""

def plus(num,str):
   pattern = '' #Empty String
   if num%2==1: #if it is odd number
       for i in range(5): #As height is always 5 range is fixed
           if i!=2:
               pattern += (' %s \n' %str) #Adding the str pattern into pattern variable
           else:
               pattern += (str*num + '\n') #Generating str pattern of length of given num value
   else: #if it is even number
       for i in range(5):
           if i!=2:
               pattern += (' %s%s \n' %(str,str)) #Adding the str pattern for even length into pattern variable
           else:
               pattern += (str*num + '\n') #Generating str pattern of length of given num value
   return pattern.rstrip() #rstrip() is used to remove the new line at the end

def minus(num,str):
   return str*num #returning the str pattern multiplied by its num value

temp = plus(5,'*') #Calling the function and storing its returned value into temp var
print(temp) #Printing pattern
print()

temp = minus(5,'*')
print(temp)

##part e
# function: check_answer
# input: two numbers (number1 & number2, both integers); an answer (an integer)
# and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct. for example, if the operator
# is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
# (1 + 2 = 3).
# output: returns True if the expression is correct, False if it is not correct
def check_answer(a,b,c,d):
    if d=="+":
        if (a+b)==c:
            return True
        else:
            return False
    elif d=="-":
        if (a-b) == c:
            return True
        else:
            return False
    else:
        return False

a=int(input("enter first integer : "))
b=int(input("enter second integer : "))
c=int(input("Enter the answer: "))
d=input("enter sign : ")
print(check_answer(a,b,c,d))



