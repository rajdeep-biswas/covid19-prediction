[curmon, curdate] = map(int, dates[-1][5::].split("-"))
mon30 = [4, 6, 9, 11]

for i in range(20):
    if curmon == 2 and curdate == 28:
        curdate = 0
        curmon = curmon + 1
    elif curmon in mon30 and curdate == 30:
        curdate = 0
        curmon = curmon + 1
    elif curdate == 31:
        curdate = 0
        curmon = curmon + 1
    curdate = curdate + 1
    dates.append("2020-" + str(curmon) + "-" + str(curdate))
