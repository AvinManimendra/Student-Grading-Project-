
# Part 3 - Staff Version with Histogram 


# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID:-20200582

# Date:-30.04.2021


print()

# SETTING VARIABLES
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0

outcomes_total=0

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

# MAKE A LOOP TO REPEAT THE PROGRESSION OUTCOME PROCESS AGAIN AND AGAIN
while True:
    
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
    
    # CHECK WHETHER THE TOTAL IS CORRECT OR NOT
    if total != 120:
        print("Total incorrect")
        continue
    
    # PROGRESSION OUTCOME SELECTION    
    else:
        
        # CALCULATING THE TOTAL NUMBER OF OUTCOMES
        outcomes_total=outcomes_total+1   
        
        if pass_mark == 120 :
            print("Progress")
            progress_count=progress_count+1
        elif pass_mark == 100:
            print("Progress (module trailer)")
            trailer_count=trailer_count+1
        elif pass_mark in (80, 60):
            print("Do not Progress – module retriever")
            retriever_count=retriever_count+1
        elif pass_mark == 40: 
            if defer_mark == 0: 
                print("Exclude")
                exclude_count=exclude_count+1
            else:
                print("Do not Progress – module retriever")
                retriever_count=retriever_count+1
        elif pass_mark == 20:
            if defer_mark in (20, 00):
                print("Exclude")
                exclude_count=exclude_count+1
            else:
                print("Do not Progress – module retriever")
                retriever_count=retriever_count+1
        elif pass_mark == 0:
            if defer_mark in (40, 20, 00):
                print("Exclude")
                exclude_count=exclude_count+1
            else:
                print("Do not Progress – module retriever    ")
                retriever_count=retriever_count+1
        
    print('----------------------------------------------------------')    
    
    # ASKING FOR THE USER INPUT TO REPEAT THE PROGRESSION OUTCOME PROCESS
    print()
    print("Would you like to enter another set of data?")
    print("Enter 'y' for yes or 'q' to quit and view results: y")
    print()
    command=input("Enter your choice = ")
    print()
    if command == "q":
        break
    elif command == "y":
        continue

# CONSTRUCTING AND DISPLAYING THE HORIZONTAL HISTOGRAM
print()
print("-----------------------------------------------")
print("Horizontal Histogram")
print("Progress  ",progress_count,"   :  ","*"*progress_count)
print("Trailer   ",trailer_count,"   :  ","*"*trailer_count)
print("Retriever ",retriever_count,"   :  ","*"*retriever_count)
print("Excluded  ",exclude_count,"   :  ","*"*exclude_count)
print()

# DISPLAYING THE TOTAL NUMBER OF OUTCOMES
print(outcomes_total," outcomes in total.")

print("-----------------------------------------------")
































