'''
For each number between 1 and 100
if it is divisible by 3 then print Fizz
if it is divisible by 5 then print Buzz
if it is divisible by both 4 and 5 print FizzBuzz
'''

counter = 1
for i in range(1,100):
    if i%3 == 0:
        print("Fizz")
    if i%5 == 0:
        print("Buzz")
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    if i %3 != 0 and i %5 != 0:
        print(counter)

    counter += 1
