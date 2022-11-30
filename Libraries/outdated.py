monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def checkday(day):
    if int(d)<=31:
        return True

def checkmonth(month):
    if month.isnumeric():
        if int(month)<=12:
            return True
    
    return month in monthes

while True:
    date = input('Date: ')

    if '/' in date:
        m,d,y = date.split('/')
    else:
        m,d,y = date.split(' ')

    if checkday(d) and checkmonth(m):
        if m.isalpha():
            print(f'{y}' +
            f'-{(int(monthes.index(m))+1):02}-{int(d[0]):02}')
        else:
            print(f'{y}-{int(m):02}-{int(d):02}')

        break






