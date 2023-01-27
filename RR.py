from process import *

def RR(inputProcess, tq):
    process = [[p.p_id,0,0,0] for p in inputProcess]

    totalTime = 0
    burstTime = calculateBurstTime(inputProcess)

    readyQueue = []

    io = []

    temp = inputProcess[:]

    isFinished = False
    timeQuantom = 0
    while not isFinished:
        for i in range(len(temp)):
            if totalTime == temp[i].arrival_time:
                readyQueue.append(i)

        for i in range(1,len(readyQueue)):
            process[readyQueue[i]][3] += 1 #increase waiting time


        cpuProcess = ""
        if len(readyQueue) >= 1:
            cpuProcess = readyQueue[0]

            if temp[cpuProcess].cpu_burst1 > 0:
                temp[cpuProcess].cpu_burst1 -= 1
                if process[cpuProcess][1] == 0:
                    process[cpuProcess][1] = process[cpuProcess][3]
            else:
                temp[cpuProcess].cpu_burst2 -= 1
            timeQuantom += 1

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
                        readyQueue = readyQueue[1:]
                        timeQuantom = 0
                else:
                    io.append(cpuProcess)
                    readyQueue = readyQueue[1:]
                    timeQuantom = 0

            if timeQuantom == tq:
                readyQueue = readyQueue[1:] + [readyQueue[0]]
                timeQuantom = 0

        isFinished = checkIsFinished(temp)

    return process, totalTime, burstTime