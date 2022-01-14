D = int(input())
N = int(input())
wr = D*(90/100)
disk_used = 0
n =0
while(n < N):
    du = int(input())
    disk_used = disk_used+du
    if disk_used >= wr:
        print('Warning')
        break
    n = n+1
if disk_used < wr:   
    print('safe')
