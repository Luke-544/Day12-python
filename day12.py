#return statement- send python value/objects back to the caller
#def multiply(number1, number2):
  #  result = number1 * number2
 #   return result

#x = multiply(4,5)

#print(x)
#or
#print(multiply(4,5))

#you can reduce the amount of code by:
#def multiply(number1, number2):
 #   return number1 * number2

#x = multiply(4,5)

#print(x)
#or
#print(multiply(4,5))

#Keyword Arguments- The order of the arguments does not matter

def hello(first, middle, last):
    print("Hello "+first+ " "+middle+" "+last)

#hello(first="Samuel", last="Mwaura", middle="Nduati")
hello("Samuel","Mwaura","Nduati") #this uses positional arguments where the order matters



