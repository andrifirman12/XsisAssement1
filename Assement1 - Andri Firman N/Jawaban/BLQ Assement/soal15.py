from datetime import datetime

def convert24(time):

    jam = datetime.strptime(time, '%I:%M:%S %p')

    div = "-------------------------------------------------------------"
    print(div)
    print("Input : " + time)
    print("Output : " + jam.strftime('%H:%M:%S'))
    print(div)

convert24('03:40:44 PM')
convert24('12:12:20 AM')