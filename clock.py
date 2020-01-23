# N - the number of minutes to convert to the day - hour - minute format
N = input()
hours = int(N) // 60
minutes = int(N) % 60
if hours > 24:
    days = hours // 24
    hours = hours % 24
    print(days, hours, minutes)
else:
    print(hours, minutes)
