# FCFS OS Scheduling Algorithm

## Project Description

This project implements the First Come First Serve (FCFS) scheduling algorithm in Python. The program calculates various scheduling metrics such as Completion Time (CT), Turnaround Time (TAT), Waiting Time (WT), Average Completion Time (Avg. CT), Average Turnaround Time (Avg. TAT), and Average Waiting Time (Avg. WT) for `n` processes given their Arrival Time (AT) and Burst Time (BT).

## Features

- Calculate Completion Time (CT)
- Calculate Turnaround Time (TAT)
- Calculate Waiting Time (WT)
- Compute Average Completion Time (Avg. CT)
- Compute Average Turnaround Time (Avg. TAT)
- Compute Average Waiting Time (Avg. WT)
- Supports `n` number of processes

## Prerequisites

- Python 3.12.4

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/STiFLeR7/FCFS-OS.git
    ```

2. Change to the project directory:

    ```sh
    cd FCFS-OS
    ```

## Usage

1. Ensure you have Python 3 installed.
2. Run the script:

    ```sh
    python FCFS.py
    ```

3. Enter the number of processes, their Arrival Times (AT), and Burst Times (BT) as prompted.

## Example

Here's an example of how the program works:

Enter the number of processes: 3

Enter the Arrival Time for process 1: 0
Enter the Burst Time for process 1: 5

Enter the Arrival Time for process 2: 1
Enter the Burst Time for process 2: 3

Enter the Arrival Time for process 3: 2
Enter the Burst Time for process 3: 8

Process AT BT CT TAT WT
1        0 5  5  5   0
2        1 3  8  7   4
3        2 8 16 14   6

Average CT: 9.67
Average TAT: 8.67
Average WT: 3.33
