print('Lesson 1_2')

while True:
    allseconds = int(input("Enter day time in seconds (0 - 86400): "))
    if allseconds < 0 or allseconds > 86400:
        print('Invalid input. Retype')
        continue
    else:
        break

hours = allseconds // 3600
minutes = allseconds // 60 - hours * 60
seconds = allseconds % 60

print("Clock: ", f"{hours:02}:{minutes:02}:{seconds:02}")
