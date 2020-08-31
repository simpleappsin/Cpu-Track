import platform
import psutil
import cpuinfo
import time, os

path = "C:/"
x = 0
while x < 1:
    cpuP = psutil.cpu_percent()
    cpuS = psutil.cpu_stats()
    cpuF = psutil.cpu_freq()

    a = int(cpuP)
    b = str(cpuS)
    c = str(cpuF)

    b1 = cpuS[0]
    b2 = cpuS[1]
    b3 = cpuS[2]
    b4 = cpuS[3]

    c1 = cpuF[0]
    c2 = cpuF[1]
    c3 = cpuF[2]
    s = "#" * int(a)

    memory = psutil.virtual_memory()[-3]
    ss = int(memory)

    g = "#" * int(ss)

    disk = psutil.disk_usage(path)[-1]
    r = int(disk)

    f = "#" * int(r)
    print("              ---------------------------------------------------------------------- ")
    print("             {'If you see nothing on your screen after clicking please press enter!'}")
    print("              ---------------------------------------------------------------------- ")
    print("")
    print("                               [  CPU Percentage: " + str(cpuP) + "%")
    print("                               |-----------------------------------")
    print("                               |  CPU Stats: ")
    print("                               |      ~ CTX_Switches: " + str(b1))
    print("                               |      ~ Interrupts: " + str(b2))
    print("                               |      ~ Soft Interrupts=0: " + str(b3))
    print("                               |      ~ Syscalls: " + str(b4))
    print("                               |-----------------------------------")
    print("                               |  CPU frequency: ")
    print("                               |      ~ Current=3101.0: " + str(c1))
    print("                               |      ~ Max: " + str(c3))
    print("                               |      ~ Min: " + str(c2))
    print("                               |-----------------------------------")
    print("                               |  Virtual Memory: " + str(memory) + "%")
    print("                               |-----------------------------------")
    print("                               [  Disk Usage: " + str(disk) + "%")
    print("")
    print("              ---------------------------------------------------------------------- ")
    print("             {'             © All Rights Reserved by Simple Apps INC.              '}")
    print("              ---------------------------------------------------------------------- ")
    print("               {'            Visit us: https://www.simpleappsinc.com             '}")
    print("                ------------------------------------------------------------------   ")
    print("                 {'                Maden by: Ata Yigit Ustundag                '}")
    print("                  --------------------------------------------------------------     ")
    time.sleep(1)
    os.system("cls")