from sympy import divisors

def find_number_with_factor_sum_threshold(threshold):
    number = 2
    while True:
        factor_sum = sum([i for i in divisors(number)])

        # Check if the sum of factors meets the threshold
        if factor_sum >= threshold:
            return number

        number += 1

# Finding the first number with sum of all factors >= 3310000
result_with_sum = find_number_with_factor_sum_threshold(3310000)
print(result_with_sum)

def find_number_with_factor_sum_threshold(threshold):
    number = 2
    while True:
        factor_sum = sum([i for i in divisors(number) if number/i <= 50])*11

        if factor_sum >= threshold:
            return number

        number += 1

result_with_sum = find_number_with_factor_sum_threshold(33100000)
print(result_with_sum)
