# 5. Whatis my score?
# The scores obtained by the students for every subject is input into a score engine that takes a list
# of values for every subject and the indices of the list represent the student roll number. As a bright
# student yourself, please write a logic to print the average marks scored (correct up to 2 places) of
# every student in the input subjects.
# Example:
# Input: Sub1: [90,80,70,60,70]
# Sub2: [95,90,75,70,80]
# Sub3: [100,100,80,70,80]
# Output:
# Student - 1 : 95
# Student - 2 : 90
# Student - 3 : 75 and so on... until the index of the lists end.

sub1=[90,80,70,60,70]
sub2= [95,90,75,70,80]
sub3 = [100,100,80,70,80]

students = []

length = len(sub1)

for i in range(length):
    avg = "%.2f" % round(((sub1[i]+sub2[i]+sub3[i])/3),2)
    students.append(avg)

i=1
for student in students:
    print(f"Student - {i} : {student}")
    i+=1
    
