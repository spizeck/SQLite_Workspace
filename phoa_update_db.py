import csv
import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

MY_FILE = "C:\\Users\\mike33_3\\PycharmProjects\\SQLite\\2015_PHOA.csv"
con = sqlite3.connect('phoa_2015.db')
cur = con.cursor()


def parse(raw_file):
    parsed_data = []
    with open(raw_file) as opened_file:
        csv_data = csv.reader(opened_file)
        csv_data.__next__()
        for row in csv_data:
            parsed_data.append([int(row[0]), row[1], float(row[2])])
    return parsed_data


def create_table():
    parsed_file = parse(MY_FILE)
    cur.executescript('DROP TABLE IF EXISTS phoa;'
                      'CREATE TABLE phoa(Month INTEGER, Descript TEXT, Amount REAL)'
                      )
    for x in parsed_file:
        month = x[0]
        descript = x[1]
        amount = x[2]
        cur.execute("INSERT INTO phoa (Month, Descript, Amount) VALUES (?, ?, ?)",
                    (month, descript, amount))
        con.commit()


def graph_data():
    cur.execute('SELECT * FROM phoa ORDER BY Month')
    month = []
    descript = []
    amount = []
    for row in cur.fetchall():
        month.append(row[0])
        descript.append(row[1])
        amount.append(row[2])





def main():
    create_table()
    graph_data()
    con.close()

if __name__ == '__main__':
    main()
