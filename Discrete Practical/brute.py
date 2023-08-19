# For any number n, write a program to list all the solutions of the equation x1 + x2 + x3 +... + xn = C wher C is a constant (C<=10) and x1, x2, x3, ..., xn are non negative integers, using brute force strategy


def find_solutions(n, target_sum):
    solutions = []
    
    def backtrack(curr_sum, curr_sol, index):
        if index == n:
            if curr_sum == target_sum:
                solutions.append(curr_sol[:])
            return
        
        for num in range(target_sum - curr_sum + 1):
            curr_sol[index] = num
            backtrack(curr_sum + num, curr_sol, index + 1)
    
    backtrack(0, [0] * n, 0)
    return solutions

# Example values
n = 3  # Number of variables
C = 5  # Constant

solutions = find_solutions(n, C)

for solution in solutions:
    print(solution)
