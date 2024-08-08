class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid  
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time  
        self.completion_time = 0
        self.turn_around_time = 0
        self.waiting_time = 0

def calculate_metrics(processes):
    total_tat = 0
    total_wt = 0
    for p in processes:
        p.turn_around_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turn_around_time - p.burst_time
        total_tat += p.turn_around_time
        total_wt += p.waiting_time
    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)
    return avg_tat, avg_wt

def print_metrics(processes, avg_tat, avg_wt, idle_time):
    print(f"{'Process':>8} {'Arrival Time':>12} {'Burst Time':>10} {'Completion Time':>15} {'Turnaround Time':>15} {'Waiting Time':>12}")
    for p in processes:
        print(f"{p.pid:>8} {p.arrival_time:>12} {p.burst_time:>10} {p.completion_time:>15} {p.turn_around_time:>15} {p.waiting_time:>12}")
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"CPU Idle Time: {idle_time}")

def round_robin(processes, quantum):
    time = 0
    queue = processes[:]
    idle_time = 0
    while queue:
        p = queue.pop(0)
        if p.arrival_time > time:
            idle_time += p.arrival_time - time
            time = p.arrival_time
        if p.remaining_time > quantum:
            time += quantum
            p.remaining_time -= quantum
            queue.extend([p] + [x for x in processes if x.arrival_time <= time and x not in queue])
        else:
            time += p.remaining_time
            p.completion_time = time
            p.remaining_time = 0
    avg_tat, avg_wt = calculate_metrics(processes)
    print_metrics(processes, avg_tat, avg_wt, idle_time)

def shortest_job_first(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    time = 0
    idle_time = 0
    for p in processes:
        if time < p.arrival_time:
            idle_time += p.arrival_time - time
            time = p.arrival_time
        time += p.burst_time
        p.completion_time = time
    avg_tat, avg_wt = calculate_metrics(processes)
    print_metrics(processes, avg_tat, avg_wt, idle_time)

def shortest_remaining_time_first(processes):
    time = 0
    idle_time = 0
    while any(p.remaining_time > 0 for p in processes):
        ready_queue = [p for p in processes if p.arrival_time <= time and p.remaining_time > 0]
        if not ready_queue:
            idle_time += 1
            time += 1
            continue
        p = min(ready_queue, key=lambda x: x.remaining_time)
        p.remaining_time -= 1
        time += 1
        if p.remaining_time == 0:
            p.completion_time = time
    avg_tat, avg_wt = calculate_metrics(processes)
    print_metrics(processes, avg_tat, avg_wt, idle_time)

def longest_job_first(processes):
    processes.sort(key=lambda x: (x.arrival_time, -x.burst_time))
    time = 0
    idle_time = 0
    for p in processes:
        if time < p.arrival_time:
            idle_time += p.arrival_time - time
            time = p.arrival_time
        time += p.burst_time
        p.completion_time = time
    avg_tat, avg_wt = calculate_metrics(processes)
    print_metrics(processes, avg_tat, avg_wt, idle_time)

def longest_remaining_time_first(processes):
    time = 0
    idle_time = 0
    while any(p.remaining_time > 0 for p in processes):
        ready_queue = [p for p in processes if p.arrival_time <= time and p.remaining_time > 0]
        if not ready_queue:
            idle_time += 1
            time += 1
            continue
        p = max(ready_queue, key=lambda x: x.remaining_time)
        p.remaining_time -= 1
        time += 1
        if p.remaining_time == 0:
            p.completion_time = time
    avg_tat, avg_wt = calculate_metrics(processes)
    print_metrics(processes, avg_tat, avg_wt, idle_time)

def main():
    num_processes = int(input("Enter number of processes: "))
    processes = []
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process P{i}: "))
        burst_time = int(input(f"Enter burst time for process P{i}: "))
        processes.append(Process(f"P{i}", burst_time, arrival_time))

    print("\nSelect Scheduling Algorithm:")
    print("1. Round Robin (RR)")
    print("2. Shortest Job First (SJF)")
    print("3. Shortest Remaining Time First (SRTF)")
    print("4. Longest Job First (LJF)")
    print("5. Longest Remaining Time First (LRTF)")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        quantum = int(input("Enter time quantum for Round Robin: "))
        round_robin(processes, quantum)
    elif choice == 2:
        shortest_job_first(processes)
    elif choice == 3:
        shortest_remaining_time_first(processes)
    elif choice == 4:
        longest_job_first(processes)
    elif choice == 5:
        longest_remaining_time_first(processes)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
