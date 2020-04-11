def is_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if(num%i == 0):
                return False;
    return True;

num = int(input())

if(is_prime(num)):
    print("El numero es primo")
else:
    print("el numero no es primo")
