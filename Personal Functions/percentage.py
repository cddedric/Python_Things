'''
oct 2018
author: Casey

################
input:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
################

Takes in an integer to know the number of names that will be given the creates a list of names and their scores then a specific name. The average of the final name's scores will be printed 
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scorecount=0
    total=0
    for item in student_marks[query_name]:  #iterate through scores that student has
        scorecount+=1                       #keep track of number of scores
        total+=item                         #running total is increased
    if scorecount is not 0:                 #avoiding divide by zero error
        total = total/scorecount            #create total
    print("%.2f" % total)

