import time

def ten_list():                         #10의 배수를 생성자로하는 리스트 [,,,d(n),,,]
    for i in range(0, 998):
        str_i = str(i * 10)
        sum = 0
        for k in range(len(str_i)):
            sum += int(str_i[k])        #각 자리의 합
        tenlist.append(sum + i * 10)    #sum 과 원래 수를 더해서 append

def selfnum_check(n):
    if n in all_list:
        pass
    else:
        print(n)


def create_num():
    for i in range(0, 10001):
        str_i = str(i)
        sum = 0
        for k in range(len(str_i)):
            sum += int(str_i[k])
        all_list.append(sum + i)

#tenlist = []
#ten_list()
tic = time.time()

all_list = []
create_num()
all_list = list(set(all_list))          #리스트 중복제거
all_list = all_list[:-29]               #9999 전 까지 slice
#all_list[-1]                           #9999확인

for i in range(10000):
    if i in all_list:
        pass
    else:
        print(i)
    #selfnum_check(i)

toc = time.time()
print('%0.3f' %(toc - tic))             #시간확인
