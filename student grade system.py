#student grade system

print("============student grade system===========")


name=input("please enter your name:")
batch_no=int(input("please enter your batch_no:"))


science_marks=int(input("enter your science_marks:"))
maths_marks=int(input("enter your maths_marks:"))
english_marks=int(input("enter your science_marks:"))


average=science_marks+maths_marks+english_marks/3
total=science_marks+maths_marks+english_marks

if average >=90:
    grade = "A"
elif average>=75:
    grade ="B"
elif average>=50:
    grade="C"
else:
    grade="F"

    
print("=====result=====")
print("name:",name)
print("batch_no:",batch_no)

print("science_marks:",science_marks)
print("maths_marks:",maths_marks)
print("english_marks:",english_marks)

print("average:",average)
print("total:",total)
print("grade:",grade)
    








