
# Part 5 - Alternative Staff Version (optional extension) 


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

# progression_outcome FUNCTION TO GET THE PRODRESSION OUTCOMES
def progression_outcome (pass_mark,defer_mark):
    
    global progress_count
    global trailer_count
    global retriever_count
    global exclude_count
    
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

# histogram FUNCTION TO CONSTRUCT AND DISPLAY THE HISTOGRAM
def histogram (progress_count,trailer_count,retriever_count,exclude_count):
    print()
    print("Progress  ",progress_count,"   :  ","*"*progress_count)
    print("Trailer   ",trailer_count,"   :  ","*"*trailer_count)
    print("Retriever ",retriever_count,"   :  ","*"*retriever_count)
    print("Excluded  ",exclude_count,"   :  ","*"*exclude_count)
    print()
    print()    

# DREATING THE DATA LIST
data_list=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

# CHECKING THE PROGRESSION OUTCOME FOR THE DATA IN THE LIST (data_list) BY USIGG THE FUNCTIONS
for count in range(len(data_list)):
    pass_mark=data_list[count][0]
    defer_mark=data_list[count][1]
    fail_mark=data_list[count][2]
    
    value=progression_outcome (pass_mark,defer_mark)
    
    outcomes_total=outcomes_total+1
    
histogram (progress_count,trailer_count,retriever_count,exclude_count)

# DISPLAYING THE TOTAL NUMBER OF OUTCOMES
print(outcomes_total," outcomes in total.")

































