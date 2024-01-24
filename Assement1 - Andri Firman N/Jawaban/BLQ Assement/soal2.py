from datetime import datetime

#* Count Days For each borrowing session
book_borrowing_date_session1 = datetime.strptime('28-2-2016', '%d-%m-%Y').date()
book_return_date_session1 = datetime.strptime('7-3-2016', '%d-%m-%Y').date()
total_days_session1 = (book_return_date_session1 - book_borrowing_date_session1).days

book_borrowing_date_session2 = datetime.strptime('29-4-2018', '%d-%m-%Y').date()
book_return_date_session2 = datetime.strptime('30-5-2018', '%d-%m-%Y').date()
total_days_session2 = (book_return_date_session2 - book_borrowing_date_session2).days

#* Count Delays of borrowing book and count the charge (100Rp/Day)
books = {
    "book A":14,
    "book B":3,
    "book C":7,
    "book D":7,
}

print("total days for 1st session is " + str(total_days_session1))
print("total days for 2nd session is " + str(total_days_session2))
print()

#* count the charge based the duration of loan and the charge each days
for i, j in books.items():
    print("---------------------------------------------------------")
    if total_days_session1 > j:
        charge = (total_days_session1 - j)*100
        print("charge for session1 " + i + " is Rp" + str(charge) + " with " + str(total_days_session1 - j) + " Late Days")
    else:
        charge = 0
        print("charge for session1 " + i + " is Rp" + str(charge))

    if total_days_session2 > j:
        charge2 = (total_days_session2 - j)*100
        print("charge for session2 " + i + " is Rp" + str(charge2) + " with " + str(total_days_session2 - j) + " Late Days")
    else:
        charge2 = 0
        print("charge for session2 " + i + " is Rp" + str(charge2))
    print("---------------------------------------------------------")
