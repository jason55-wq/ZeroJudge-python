import sys

# ZeroJudge a004：判斷每一個輸入年份是否為閏年。
for line in sys.stdin:
    # 讀取一行年份，去除換行與多餘空白後轉成整數。
    year = int(line.strip())

    # 閏年規則：
    # 1. 可以被 400 整除，一定是閏年。
    # 2. 可以被 4 整除但不能被 100 整除，也是閏年。
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("閏年")
    else:
        print("平年")




