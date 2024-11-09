'''
Python has several built-in data types, including:
int (integer)
float (floating-point number)
str (string)
bool (boolean)
list (a collection of items)
tuple (immutable collection of items)
dict (key-value pairs)
set (unordered collection of unique items)
'''




castomerName='Rohik' #string data type
print(castomerName)

castomerId=123456 #Integer data type
print(castomerId)

ratting=4.7
print(ratting)

creditcardAccess=True #boolean
print(creditcardAccess)

productlist=['mango','banana'] #list example
print(productlist)

username=('user_id','password') #trupple
print(username)

#type casting
#type casting
a=10 #int
b=3.14 #float
print(type(a))
print(type(b))

#type casting int to float
a_float = float(a)
print(a_float) #output 10.0

#type casting float to int 
b_int = int(b)
print(b_int) #output 3

#type casting float to string 
a_str = str(a)
print(a_str) #output 10

#type casting string to int 
num_str = 123



#3. String Operations

'''Slicing
Syntax: string[start:stop:step]
Used to extract parts of a string.

'''
text= 'Python progaming'
distrct= 'khulna city'
# Slicing from index to 6 (exclusive)
print(text[0:6]) # Output: "Python" 
print(distrct[0:5])
print(distrct[0:4])
print(distrct[0:3])

# Slicing from index 7 to the end 
print(text[7:]) # Output: "Programming"

# Slicing with a step
print(text[0:16:2]) # Output: "Pto rgamn"

#
Str = 'string'
print(Str[::-1])



#input a word
text =input("Enter a string: ")
print(f"Original String: {text}")
print("Reverse String")
print(text[::-1])

