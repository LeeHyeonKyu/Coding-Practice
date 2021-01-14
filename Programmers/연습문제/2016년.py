import calendar

def solution(a, b):
    return calendar.weekheader(3).split()[calendar.weekday(2016,a,b)].upper()
