#global variable is a value of a variable which is defined or declared outside the function 
#local variable is a value which is defined or decalred inside the function

def students_average(marks, number_of_student):
    sum_of_marks= sum(marks)
    total_sub=len(marks)
    average=sum_of_marks / total_sub
    print(f"Average of the student is:{number_of_student} of {average}")
s1=students_average([50,60,200],1)


