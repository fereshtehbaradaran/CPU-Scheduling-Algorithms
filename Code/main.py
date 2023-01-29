import csv
from process import *
from FCFS import FCFS
from RR import RR
from SJF import SJF
from MLFQ import MLFQ


def getData(fileName):
    processes = []

    rows = []
    with open(fileName, 'r') as df:
        dfreader = csv.reader(df)
        fields = next(dfreader)

        for row in dfreader:
            rows.append(row)

    for row in rows:
        processes.append(Process(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))

    return processes


def copy(lst):
    newLst = []
    for p in lst:
        newLst.append(Process(p.p_id,p.arrival_time,p.cpu_burst1,p.io_time,p.cpu_burst2))
    return newLst



if __name__ == '__main__':
    while True:
        try:
            fileName = input("Data File: ")
            processes = getData(fileName)
        except:
            print("There is a problem Please try again!")
            continue

        fcfsProcess = copy(processes)
        rrProcess = copy(processes)
        sjfProcess = copy(processes)
        mlfqProcess = copy(processes)

        printResult("FCFS", *FCFS(fcfsProcess))
        printResult("RR", *RR(rrProcess,5))
        printResult("SJF", *SJF(sjfProcess))
        printResult("MLFQ", *MLFQ(mlfqProcess,16,8))
        break