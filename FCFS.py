def fcfs(n):
    
    at = [int(input(f"Enter arrival time for process P{i}: ")) for i in range(n)]
    bt = [int(input(f"Enter burst time for process P{i}: ")) for i in range(n)]

    
    ct = [0] * n
    tat = [0] * n
    wt = [0] * n

    
    ct[0] = at[0] + bt[0]
    for i in range(1, n):
        ct[i] = max(at[i], ct[i-1]) + bt[i]

    
    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]

    
    avg_ct = sum(ct) / n
    avg_tat = sum(tat) / n
    avg_wt = sum(wt) / n

    
    return at, bt, ct, tat, wt, avg_ct, avg_tat, avg_wt


n = int(input("Enter the number of processes: "))


at, bt, ct, tat, wt, avg_ct, avg_tat, avg_wt = fcfs(n)


print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
print(f"Average CT: {avg_ct:.2f}")
print(f"Average TAT: {avg_tat:.2f}")
print(f"Average WT: {avg_wt:.2f}")