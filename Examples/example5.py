#5 Prime numbers between two ranges using functions
lower_value = int(input ("Enter the Lowest Range Value: "))  
upper_value = int(input ("Enter the Upper Range Value: "))  
def prime_numbers(lower_value, upper_value):
    for num in range(lower_value, upper_value + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
prime_number=prime_numbers(lower_value, upper_value)