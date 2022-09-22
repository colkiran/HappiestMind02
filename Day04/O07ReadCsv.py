
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    # colnames = next(emp_details)
    # print(colnames)
    emptable = PrettyTable(next(emp_details))

    for rec in emp_details:
        # print(rec)
        emptable.add_row(rec)

print(emptable)
