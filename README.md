# CPU-Scheduling-Algorithms

The project goal was to implement following CPU scheduling algorithms:
+ **First Come, First Serve (FCFS)**
+ **Round Robin (RR)**, with time quantum: 5ms.
+ **Shortest Job First (SJF)**
+ **MultiLevel Feedback Queue (MLFQ)** : 
  - First queue: RR Time Quantum 8 ms
  - Second queue: RR with time Quantum 16 ms
  - Third queue: FCFS
  
## Input
The input is a CSV file, consist of **process_id**, **arrival_time**, **cpu_time1**, **io_time**, **cpu_time2** for each process.

## Output
Output shows **Response time**, **Waiting Time**, **Turnaround time** and **Start and End time** of each process. and also:
+ **Total Time and Idle Time**
+ **Average Waiting Time**
+ **Average Response Time**
+ **Average Turnaround Time**
+ **CPU Utilization**
+ **Throughput**
