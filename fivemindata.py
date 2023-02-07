

import csv


def fiveMin(data):
    print("hello")
    f = open("5min.csv", "w")

    cw = csv.writer(f)
    cw.writerow(["TIME", "O", "H", "L", "C", 'Cm.V',
                 'AllVolume',])
    # for g in data:
    #     a: list = g
    #     print(a)
    #     if (a[2]-a[3] < 100&&):
    #         a.append("0")
    #         print(a)
    # cw.writerow(a)
    datalist: list = data
    finded: int = 1
    for x in range(0, len(datalist)):
        a: list = data[x]
        a1: list = data[x-1]
        a2: list = data[x-2]

        if a[2]-a[3] < 100 and a[5] < a1[5] and a1[2] - a1[3] < 100 and a1[2] > a[1] and a1[3] < a[4] and a[1] < a[4]:
            print(a)
            finded += 1

    print(finded)
