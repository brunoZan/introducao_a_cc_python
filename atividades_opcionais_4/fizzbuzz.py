def fizzbuzz(b):
    if((b % 3) == 0 and not b % 5 == 0):
        return "Fizz"
    if((b % 5) == 0 and not b % 3 == 0):
        return "Buzz"
    if(b % 3 == 0 and b % 5 == 0):
        return "FizzBuzz"
    else:
        return b
