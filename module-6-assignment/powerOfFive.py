def powerOfFive(n):
    if n == 1:
        return True
    elif n <=0 or n % 5 != 0:
        return False
    return powerOfFive(n/5)
    
print(powerOfFive(1))