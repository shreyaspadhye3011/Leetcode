# https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    roundedGrades = []
    for grade in grades:
        # no need to round failing grades
        # bug in Q: it says below 40 is failing but solution is for 38
        if grade < 38:
            roundedGrades.append(grade)
        else:
            nextMultiple = findNextMultiple(grade)
            if nextMultiple - grade < 3:
                roundedGrades.append(nextMultiple)
            else:
                roundedGrades.append(grade)
    return  roundedGrades   

# find next multiple of 5 
def findNextMultiple(num):
    return 5 * (int(num/5)+1)