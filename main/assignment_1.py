# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:55:45 2023

Assignment 1

@author: Jacob Romero
course: Numerical Calculus
date: 1/23/2023
"""
# 1. Use double precision, calculate the resulting values (format to 5 decimal places)
#   a) 010000000111111010111001
def double_precision():
    s = 0
    
    exponent = 10000000111
    c, i = 0, 0
    while(exponent !=0):
        exp = exponent % 10
        c = c + exp * pow(2,i)
        exponent = exponent//10
        i += 1
        
    fraction = str(1110101110010000000000000000000000000000000000000000)
    f = 0
    i = 1
    for item in fraction:
        f = f + int(item) * (0.5**i)
        i += 1
    
    n_true = ((-1)**s) * (2**(c - 1023)) * ((1+f))
    print(n_true)
    
    return

double_precision()


# 2. Repeat exercise 1 using three-digit chopping arithmetic

def three_digit_chopping():
    s = 0
    
    exponent = 10000000111
    c, i = 0, 0
    while(exponent !=0):
        exp = exponent % 10
        c = c + exp * pow(2,i)
        exponent = exponent//10
        i += 1
        
    fraction = str(1110101110010000000000000000000000000000000000000000)
    f = 0
    i = 1
    for item in fraction:
        f = f + int(item) * (0.5**i)
        i += 1
    
    n = ((-1)**s) * (2**(c - 1023)) * ((1+f))
    
    n_chopped = int(str(n)[:3])
    
    print("\n")
    print(n_chopped)
    
    return

three_digit_chopping()

# 3. Repeat exercise 1 using three-digit rounding arithmetic

def three_digit_rounding():
    s = 0
    
    exponent = 10000000111
    c, i = 0, 0
    while(exponent !=0):
        exp = exponent % 10
        c = c + exp * pow(2,i)
        exponent = exponent//10
        i += 1
        
    fraction = str(1110101110010000000000000000000000000000000000000000)
    f = 0
    i = 1
    for item in fraction:
        f = f + int(item) * (0.5**i)
        i += 1
    
    n = ((-1)**s) * (2**(c - 1023)) * ((1+f))
    n_rounded = round(n)
    
    print("\n")
    print(n_rounded)
    
    return

three_digit_rounding()

# 4. Compute the absolute and relative error with the exact value from question 1 and its 3 digit rounding

def absolute_error(precise:float, approximate: float):
    
    sub_operation = precise - approximate

    return abs(sub_operation)

def relative_error(precise:float, approximate: float):
    
    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise

    return div_operation

print("\n")
print("Absolute Error:", absolute_error(491.5625, 492))
print("Relative Error:", relative_error(491.5625, 492), "\n")

# 5. What is the minimum number of terms needed to computer f(1) with error < 10-4?

def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)

    return term_check

def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, 100):
        result = abs(eval(function_we_got))

        #print(result)
        if starting_val <= result:
            decreasing_check = False

    return decreasing_check


def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True

    return False

def minimum_term(function:str, x:int, error_term:float):
    n = 0
    k = 1
    
    while(abs(eval(function)) > error_term):
        n += 1
        k += 1
    print("Minimum number of terms:", n)

if __name__ == "__main__":

    function_a: str = "(-1**k) * (x**k) / (k**3)"
    x: int = 1
    check1: bool = check_for_alternating(function_a)
    check2: bool = check_for_decreasing(function_a, x)

    print(check1 and check2)
    minimum_term(function_a, x, 1e-4)

    #if check1 and check2:
     #   use_minimum_term_function(function_a)
        # if both ckecks pass , print the actual number
        
# 6. Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 – 10 = 0 with 
# accuracy 10^-4 using a = -4 and b = 7.
# a) Using the bisection method

def func(x):
    return x*x*x - x*x + 2

def bisection_method(left: float, right: float, given_function: str):
    # pre requisites
    # 1. we must have the two ranges be on opposite ends of the function (such that
    # function(left) and function(right) changes signs )
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = .0001
    diff: float = right - left

    # we can only specify a max iteration counter (this is ideal when we dont have all
    # the time in the world to find an exact solution. after 10 iterations, lets say, we
    # can approximate the root to be ###)
    max_iterations = 20
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1

        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break
        
        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)
        
        # this section basically checks if we have crossed the origin point (another way
        # to describe this is if f(midpoint) * f(left_point) changed signs)
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

        #print(mid_point)
    print("\n")
    print("Number of iterations using Bisection method:", iteration_counter)

if __name__ == "__main__":

    # bisection gives us the first zero of any function to a certain error threshold
    left = -4
    right = 7
    function_string = "x**3 + (4*(x**2)) - 10"
    bisection_method(left, right, function_string)

# b) Using the newton Raphson method

def custom_derivative(value):
    return (3 * value* value) + (8 * value)


def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)

    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)

        # finds f' 
        f_prime = custom_derivative(initial_approximation)

        # division operation
        approximation = f / f_prime

        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1
    print("\n")
    print("Number of iterations using Newton Raphson method:", iteration_counter)

if __name__ == "__main__":
    # newton_raphson method
    initial_approximation: float = -4
    tolerance: float = .0001
    sequence: str = "(x**3) + (4*(x**2)) - 10"

    newton_raphson(initial_approximation, tolerance, sequence)
