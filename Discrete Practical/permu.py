#Write a program that generates all permutations of a given set of digits with or without repetition

import itertools

def generate_permutations(digits, repetition=False):
    if repetition:
        return list(itertools.product(digits, repeat=len(digits)))
    else:
        return list(itertools.permutations(digits))

# Example usage
digits = [1, 2, 3]
print("Permutations without repetition:")
permutations_without_repetition = generate_permutations(digits)
for perm in permutations_without_repetition:
    print(perm)

print("\nPermutations with repetition:")
permutations_with_repetition = generate_permutations(digits, repetition=True)
for perm in permutations_with_repetition:
    print(perm)










def generate_permutations(digits, repetition=False):
    def backtrack(start):
        if start == len(digits):
            result.append(tuple(current_perm))
            return
        
        for i in range(len(digits)):
            if not repetition and used[i]:
                continue
            
            current_perm[start] = digits[i]
            
            if not repetition:
                used[i] = True
            
            backtrack(start + 1)
            
            if not repetition:
                used[i] = False
    
    result = []
    current_perm = [0] * len(digits)
    used = [False] * len(digits)
    backtrack(0)
    return result

# Example usage
digits = [1, 2, 3]
print("Permutations without repetition:")
permutations_without_repetition = generate_permutations(digits)
for perm in permutations_without_repetition:
    print(perm)

print("\nPermutations with repetition:")
permutations_with_repetition = generate_permutations(digits, repetition=True)
for perm in permutations_with_repetition:
    print(perm)
