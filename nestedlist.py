from operator import itemgetter 
if __name__ == '__main__':
    student_recort = []
    temp_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_recort.append([name,score]) 
    temp_list = sorted(student_recort, key=itemgetter(1), reverse=False)
    lowest = temp_list[0][1]
    second_lower = None
    student_name= []
    for i in temp_list:
        if i[1] > lowest:
            second_lower = i[1]
            break
    for i in temp_list:
        if i[1] == second_lower:
            student_name.append(i[0])
    student_name.sort()
    print(*student_name,sep = "\n")
             
            
