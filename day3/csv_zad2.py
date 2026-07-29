import csv

# filename = 'records.csv'
# filename = 'records_discount.csv'
filename = 'records_discount_semicolon.csv'

columns = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "

    # StopIteration - skończyły się dane
    csv_f.seek(0)  # powrót na początek pliku

    csvreader = csv.reader(csv_f, delimiter=";")

    print(csvreader)  # <_csv.reader object at 0x0000017E5AF6C7C0>

    columns = next(csvreader)  # odczyt bieżacego wiersza, odczyt na następny

    for row in csvreader:
        rows.append(row)

print("Columns:", columns)
print("Rows:", rows)
