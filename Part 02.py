

# Part 2 - Student Version (Validation)


# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID:-20200582

# Date:-30.04.2021


print()
print()

# type_selector FUNCTION TO CHECK THE TYPE OF THE USER INPUT
def type_selector (mark):
    try:
        answer=int(mark)
        sign="true"
        return sign        
    except:
        print()
        print("----------Integer required----------")           

# range_check FUNCTION TO CHECK THE USER INPUT IN THE VALID RANGE
def range_check (value):
    if value not in ('0','00','20','40','60','80','100','120'):
        print()
        print("----------Out of range----------")
        
    else:
        sign="true"
        return sign

print('----------------------------------------------------------')

# PASS CREDIT INPUT 
while True:
    pass_mark=input("Please Enter Your Credits At Pass = ")
    if type_selector (pass_mark) == "true" and range_check (pass_mark) == "true":
        break
    
    
    print() 
    
print()

# DEFER CREDIT INPUT
while True:
    defer_mark=input("Please Enter Your Credits At Defer = ")
    if type_selector (defer_mark) == "true" and range_check (defer_mark) == "true":
        break
        
    print()  
print()

# FAIL CREDIT INPUT
while True:
    fail_mark=input("Please Enter Your Credits At Fail = ")
    if type_selector (fail_mark) == "true" and range_check (fail_mark) == "true":
        break
            
    print()
print()
      
# CHANGE THE TYPE OF THE VARIABLES INTO INTEGER
pass_mark=int(pass_mark)
defer_mark=int(defer_mark)
fail_mark=int(fail_mark)

# CALCULATING THE TOTAL CREDITS TO CHECK THE TOTAL
total=pass_mark+defer_mark+fail_mark

# CHECK WHETHER the total is correct or not
if total != 120:
    print("Total incorrect")

# PROGRESSION OUTCOME SELECTION
else:
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