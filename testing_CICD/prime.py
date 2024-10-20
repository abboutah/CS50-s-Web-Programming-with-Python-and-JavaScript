import math
def is_prime(n):

    # number less than 2 is not prime
    if n < 2:
        return False

    # checking factor up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):

        # If i is a factor, reurn false
        if n % i == 0:
            return False

    #If no factors were found, return True
    return True

# list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
# for i in list:
#     print(i)
#     assert is_prime(i) == True