from datetime import datetime, timedelta

in1 = "27 January 2019 | 05:00:01"
out1 = "27 January 2019 | 17:45:03"

in2 = "27 January 2019 | 07:03:59"
out2 = "27 January 2019 | 15:30:06"

in3 = "27 January 2019 | 07:05:00"
out3 = "28 January 2019 | 00:20:21"

in4 = "27 January 2019 | 11:14:23"
out4 = "29 January 2019 | 13:20:00"

div = "--------------------------------------------------------------------------------"

def soal3(time_in, time_out):
    time_in = datetime.strptime(time_in, '%d %B %Y  | %H:%M:%S')
    time_out = datetime.strptime(time_out, '%d %B %Y | %H:%M:%S')

    park_time = int((time_out - time_in).total_seconds() / 3600)

    # * Price Terms and Condition
    if park_time <= 8:
        charge = park_time * 1000
    elif 8 < park_time <= 24:
        charge = 8000
    elif 24 < park_time:
        charge = 15000 + (park_time - 24) * 1000
    print(div)

    return park_time, charge

park, nominal = soal3(in1, out1)
print(f"For Parking {park} Hours [{in1} - {out1}], \nTotal Charge is Rp{nominal}")
park, nominal = soal3(in2, out2)
print(f"For Parking {park} Hours [{in2} - {out2}], \nTotal Charge is Rp{nominal}")
park, nominal = soal3(in3, out3)
print(f"For Parking {park} Hours [{in3} - {out3}], \nTotal Charge is Rp{nominal}")
park, nominal = soal3(in4, out4)
print(f"For Parking {park} Hours [{in4} - {out4}], \nTotal Charge is Rp{nominal}")
print(div)
