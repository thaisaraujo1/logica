for contador in range (1, 1001):
 
    if contador % 15 == 0:
        print (contador, "Fizz")
   
    elif contador % 3 == 0:
        print(contador, "Buzz")
   
    elif contador % 5 == 0:
        print(contador, "FizzBuzz")
   
    else:
        print (contador)