# refactor to generate output to a list

user_upperlimit = int(input("What is the upper limit: "))
upper_limit = user_upperlimit

def fizzbuzz(upper_limit):
    output_list = []
    for num in range(1, upper_limit+1):

        if (num % 3 == 0 and num % 5 == 0):
            output_list.append("FizzBuzz")

        elif num % 5 == 0:
            output_list.append("Buzz")

        elif num % 3 == 0:
            output_list.append("Fizz")
        else:
            output_list.append(num)
    print(output_list)        


fizzbuzz(upper_limit)

if __name__ == '__main__':
    upper_limit
    fizzbuzz(upper_limit)