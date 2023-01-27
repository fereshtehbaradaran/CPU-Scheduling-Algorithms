from process import *

def SJF(inputProcess):
    process = [[p.p_id, 0, 0, 0] for p in inputProcess]

    totalTime = 0
    burstTime = calculateBurstTime(inputProcess)

    readyQueue = []

    io = []

    temp = inputProcess[:]

    isFinished = False

    while not isFinished:
        for i in range(len(temp)):
            if totalTime == temp[i].arrival_time:
                readyQueue.append(i)

        cpuProcess = ""
        if len(readyQueue) >= 1:
            remainingTime = []
            for i in readyQueue:
                if temp[i].cpu_burst1 == 0:
                    remainingTime.append(temp[i].cpu_burst2)
                else:
                    remainingTime.append(temp[i].cpu_burst1)

            cpuProcess = readyQueue[remainingTime.index(min(remainingTime))]

            if temp[cpuProcess].cpu_burst1 > 0:
                temp[cpuProcess].cpu_burst1 -= 1
                if process[cpuProcess][1] == 0:
                    process[cpuProcess][1] = process[cpuProcess][3]
            else:
                temp[cpuProcess].cpu_burst2 -= 1

        for i in readyQueue:
            if i != cpuProcess:
                process[i][3] += 1  # increase waiting time

        for i in io[:]:
            temp[i].io_time -= 1
            if temp[i].io_time == 0:
                readyQueue.append(i)
                io.remove(i)

        totalTime += 1

        if cpuProcess != "":
            if temp[cpuProcess].cpu_burst1 == 0:
                if temp[cpuProcess].io_time == 0:
                    if temp[cpuProcess].cpu_burst2 == 0:
                        process[cpuProcess][2] = totalTime - temp[cpuProcess].arrival_time
                        readyQueue.remove(cpuProcess)
                else:
                    io.append(cpuProcess)
                    readyQueue.remove(cpuProcess)

        isFinished = checkIsFinished(temp)


    return process, totalTime, burstTime