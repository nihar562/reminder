def Reminder(D,N):
    wr = D*(90/100)
    disk_used = 0
    n =0
    while(n < N):
        du = int(input())
        disk_used = disk_used+du
        if disk_used >= wr:
            return 'Warning'
        n = n+1
    if disk_used < wr:   
        return 'safe'
DiskSize = int(input())
No_of_days= int(input())
print(Reminder(DiskSize,No_of_days))
