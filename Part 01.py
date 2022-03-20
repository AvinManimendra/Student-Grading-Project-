

# Part 1 - Student Version


# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID:-20200582

# Date:-30.04.2021

print()
print()

print('----------------------------------------------------------')

# USER INPUTS
pass_mark=int(input("Please Enter Your Credits At Pass = "))
print()
defer_mark=int(input("Please Enter Your Credits At Defer = "))
print()
fail_mark=int(input("Please Enter Your Credits At Fail = "))
print()

# PROGRESSION OUTCOME SELECTION
if pass_mark == 120 :
    print("Progress")
elif pass_mark == 100:
    print("Progress (module trailer)")
elif pass_mark in (80, 60):
    print("Do not Progress – module retriever")
elif pass_mark == 40: 
    if defer_mark == 0: 
        print("Exclude")
    else:
        print("Do not Progress – module retriever")
elif pass_mark == 20:
    if defer_mark in (20, 00):
        print("Exclude")
    else:
        print("Do not Progress – module retriever")
elif pass_mark == 0:
    if defer_mark in (40, 20, 00):
        print("Exclude")
    else:
        print("Do not Progress – module retriever    ")

print('----------------------------------------------------------')