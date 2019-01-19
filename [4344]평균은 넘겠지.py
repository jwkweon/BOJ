def averg(list, num_student):
    total_score = 0
    num = 0

    for i in list:
        total_score += i
    average = total_score / num_student

    for i in list:
        if i > average:
            num += 1
        else:
            pass

    return num / num_student * 100

num_c = int(input())

for i in range(num_c):
    list = input().split()

    num_student = int(list[0])
    score = []
    for k in range(num_student):
        score.append(int(list[k + 1]))

    print("%0.3f%%" % averg(score, num_student))
