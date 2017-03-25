'''
Convert:
Roman and Arabic numerals are different enough that a program to convert back and forth between the two systems
would be useful assuming, of course, that you are a Roman trader living sometime in the Middle Ages with access
to a computer with a Python interpreter.
'''

#define the function CalculateValue
def CalculateValue(roman):
#check value
   if (roman == 'I'):
       return 1
   #check value
   if (roman == 'V'):
       return 5
   #check value
   if (roman == 'X'):
       return 10
   #check value
   if (roman == 'L'):
       return 50
   #check value
   if (roman == 'C'):
       return 100
   #check value
   if (roman == 'D'):
       return 500
   #check value
   if (roman == 'M'):
       return 1000
   return -1
#defines the function romanToDecimalConverter
def romanToDecimalConverter(strngs):
#declare the variables
   result = 0
   it = 0
#check the length
   while (it < len(strngs)):
   #calculate s1
       s1 = CalculateValue(strngs[it])
#check the length
       if (it+1 < len(strngs)):

           #calculate s2
           s2 = CalculateValue(strngs[it+1])

           #check s1 dn s2
           if (s1 >= s2):

               #assign the result vaue
               result = result + s1
               it = it + 1
           else:

               #assign the results
               result = result + s2 - s1
               it = it + 2
       else:
       #assign the results
           result = result + s1
           it = it + 1
#teturns the final result
   return result

#Statement to print
print("Roman to Integer"),
#call the romanToDecimalConverter
print(romanToDecimalConverter("XMV"))