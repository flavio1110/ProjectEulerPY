#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def isMultipleOf(mutiplier, number):
    return (number % mutiplier) == 0
sum = 0

for number in range(1, 1000):
    if isMultipleOf(3, number) or isMultipleOf(5, number):
        sum = sum + number
        
print sum
