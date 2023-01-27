class Process:
    def __init__(self, p_id, arrival_time, cpu_burst1, io_time, cpu_burst2):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.cpu_burst1 = cpu_burst1
        self.io_time = io_time
        self.cpu_burst2 = cpu_burst2


def printResult(algoName, processes, totalTime, burstTime):
    print("="*100 + "\n" + " "* 45 + algoName + "\n" + "="*100)
    print("\t"*3 + "Response Time" + "\t"*4 + "Turn Around Time" + "\t"*4 + "Waiting Time")

    avgResponseTime = 0
    avgTurnAroundTime = 0
    avgWaitingTime = 0

    for p in processes:
        print(p[0] + "\t"*3 + str(p[1]) + "\t"*7 + str(p[2]) + "\t"*8 + str(p[3]))
        avgResponseTime += p[1]
        avgTurnAroundTime += p[2]
        avgWaitingTime += p[3]
    avgResponseTime /= len(processes)
    avgTurnAroundTime /= len(processes)
    avgWaitingTime /= len(processes)

    print("_"*100)

    print("AVG" + "\t"*3 + str(avgResponseTime) + "\t"*7 + str(avgTurnAroundTime) + "\t"*7 + str(avgWaitingTime) + "\n")

    print("Total Time:", totalTime)
    print("Idle Time:", totalTime - burstTime)
    print("Burst Time:", burstTime)
    print("CPU Utilization: %.2f" %((burstTime/totalTime)*100), "%")
    print("Throughput: %.2f" %(len(processes)*1000/totalTime))
    print("\n\n")


def calculateBurstTime(inputProcess):
    burstTime = 0
    for p in inputProcess: # calculate burst time
        burstTime += p.cpu_burst1 + p.cpu_burst2

    return burstTime

def checkIsFinished(inputProcess):
    isFinished = True
    for p in inputProcess:
        if p.cpu_burst1 != 0 or p.io_time != 0 or p.cpu_burst2 != 0:
            isFinished = False
            break
    return isFinished
