grades=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    grades.append([name,score])
sorted_scores=sorted(list(set([X[1] for X in grades])))
second_lowest=sorted_scores[1]
lowest_grades_final=[]
for i in grades:
    if second_lowest==i[1]:
        lowest_grades_final.append(i[0])
for i in sorted(lowest_grades_final):
            print(i)