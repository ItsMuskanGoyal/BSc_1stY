#Write a program to evaluate a polynomial function ( For example store f(x)= 4n^2 + 2n + 9 in an array and for a given value of n say n = 5, compute the value of f(n)).



def evaluate_polynomial(coefficients, x):
    result = 0
    for power, coefficient in enumerate(coefficients):
        result += coefficient * (x ** power)
    return result

# Example polynomial coefficients: f(x) = 4n^2 + 2n + 9
polynomial_coefficients = [9, 2, 4]

n = 5
result = evaluate_polynomial(polynomial_coefficients, n)
print(f"f({n}) =", result)

