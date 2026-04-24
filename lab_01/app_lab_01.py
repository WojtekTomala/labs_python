import time
from functools import lru_cache

# COLLATZ SEQUENCE:
# n = 5
# if n is even -> n = n / 2
# if n is odd -> n = 3 * n + 1

# We repeat the process until we reach n = 1

# Collatz conjecture says that for every starting point n
# this sequence will be finite - it will terminate at some point
# this is the conjecture.

# 1.1 Generating sequence based on number:
# example for n = 5:
# 5 -> 16 -> 8 -> 4 -> 2 -> 1

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2 # NO FLOATING POINT NUMBERS
        else:
            n = 3 * n + 1

        sequence.append(n)

    return sequence

user_input_n = (input("Enter a 'n' number: "))

print(collatz_sequence(int(user_input_n)))

# 2.2 Chcecking which input produces the longest sequence (extra):

def collatz_sequence_length(n):
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2 # NO FLOATING POINT NUMBERS
        else:
            n = 3 * n + 1

        counter += 1
    return counter

print(collatz_sequence_length(int(user_input_n)))

# 2.3 Checking in range (extra):
longest = 0
longest_i = 0
start = time.time()
for i in range(1, int(user_input_n) + 1):
    current_length = collatz_sequence_length(i)
    if current_length > longest:
        longest = current_length
        longest_i = i

end = time.time()
print("For number n: " + str(longest_i) + " The longest length is " + str(longest) + " It took: " + str(end - start) + " seconds.")

# 2.4 Implementing collatz sequence fn with recursive approach (extra):

def collatz_sequence_length_recursive(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + collatz_sequence_length_recursive(n // 2)
        else:
            return 1 + collatz_sequence_length_recursive(3 * n + 1)

longest = 0
longest_i = 0
start = time.time()
for i in range(1, int(user_input_n) + 1):
    current_length = collatz_sequence_length_recursive(i)
    if current_length > longest:
        longest = current_length
        longest_i = i


end = time.time()
print("For number n: " + str(longest_i) + " The longest length is " + str(longest) + " It took: " + str(end - start) + " seconds.")

# 2.5 Cacheing:

@lru_cache(maxsize=None)
def collatz_sequence_length_recursive_cached(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + collatz_sequence_length_recursive_cached(n // 2)
        else:
            return 1 + collatz_sequence_length_recursive_cached(3 * n + 1)

longest = 0
longest_i = 0
start = time.time()
for i in range(1, int(user_input_n) + 1):
    current_length = collatz_sequence_length_recursive_cached(i)
    if current_length > longest:
        longest = current_length
        longest_i = i


end = time.time()
print("For number n: " + str(longest_i) + " The longest length is " + str(longest) + " It took: " + str(end - start) + " seconds.")