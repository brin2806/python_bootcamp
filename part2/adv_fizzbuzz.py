# asks for a number and then makes it the upper limit

user_upperlimit = int(input("What is the upper limit: "))
upper_limit = user_upperlimit

def fizzbuzz(upper_limit):
    for num in range(1, upper_limit+1):

        if (num % 3 == 0 and num % 5 == 0):
            return "FizzBuzz"

        elif num % 5 == 0:
            return "Buzz"

        elif num % 3 == 0:
            return "Fizz"
        else:
            return num 

print(fizzbuzz(upper_limit))          

#  if __name__ == '__main__':
#    upper_limit
#    fizzbuzz(upper_limit)