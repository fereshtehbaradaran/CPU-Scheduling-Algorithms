from process import *

def MLFQ(inputProcess, tq1, tq2):
    process = [[p.p_id,0,0,0] for p in inputProcess]

    totalTime = 0
    burstTime = calculateBurstTime(inputProcess)

    queue1 = []
    queue2 = []
    queue3 = []

    io = []

    temp = inputProcess[:]

    isFinished = False
    timeQuantomQ1 = 0
    timeQuantomQ2 = 0

    while not isFinished:
        for i in range(len(temp)):
            if totalTime == temp[i].arrival_time:
                queue1.append(i)

        cpuProcess = ""
        cpuIsFull = False
        if len(queue1) >= 1:
            cpuProcess = queue1[0]
            timeQuantomQ1 += 1
            cpuIsFull = True
        elif len(queue2) >= 1:
            cpuProcess = queue2[0]
            timeQuantomQ2 += 1
            cpuIsFull = True
        elif len(queue3) >= 1:
            cpuProcess = queue3[0]
            cpuIsFull = True

        if cpuIsFull:
            if temp[cpuProcess].cpu_burst1 > 0:
                temp[cpuProcess].cpu_burst1 -= 1
                if process[cpuProcess][1] == 0:
                    process[cpuProcess][1] = process[cpuProcess][3]
            else:
                temp[cpuProcess].cpu_burst2 -= 1


        for i in queue1 + queue2 + queue3:
            if i != cpuProcess:
                process[i][3] += 1 #increase waiting time

        for i in io[:]:
            temp[i].io_time -= 1
            if temp[i].io_time == 0:
                queue1.append(i)
                io.remove(i)

        totalTime += 1

        if cpuIsFull:
            if temp[cpuProcess].cpu_burst1 == 0:
                if temp[cpuProcess].io_time == 0:
                    if temp[cpuProcess].cpu_burst2 == 0:
                        process[cpuProcess][2] = totalTime - temp[cpuProcess].arrival_time
                        if cpuProcess in queue1:
                            queue1.remove(cpuProcess)
                            timeQuantomQ1 = 0
                        elif cpuProcess in queue2:
                            queue2.remove(cpuProcess)
                            timeQuantomQ2 = 0
                        elif cpuProcess in queue3:
                            queue3.remove(cpuProcess)
                else:
                    io.append(cpuProcess)
                    if cpuProcess in queue1:
                        queue1.remove(cpuProcess)
                        timeQuantomQ1 = 0
                    if cpuProcess in queue2:
                        queue2.remove(cpuProcess)
                        timeQuantomQ2 = 0
                    elif cpuProcess in queue3:
                        queue3.remove(cpuProcess)

            if timeQuantomQ1 == tq1:
                queue1.remove(cpuProcess)
                queue2.append(cpuProcess)
                timeQuantomQ1 = 0
            elif timeQuantomQ2 == tq2:
                queue2.remove(cpuProcess)
                queue3.append(cpuProcess)

        isFinished = checkIsFinished(temp)

    return process, totalTime, burstTime