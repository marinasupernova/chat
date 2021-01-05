import csv
from datetime import datetime


def add_msg(name, msg):
    file_pointer = open("Chat.csv", "a")
    writer = csv.writer(file_pointer)
    writer.writerow([name, msg, datetime.now()])
    file_pointer.close()

def display_msgs():
    file_pointer = open("Chat.csv", "r")
    rows = list(csv.reader(file_pointer))
    length = len(rows)
    i = 0
    while i < length:
        name = rows[i][0]
        message = rows[i][1]
        date = rows[i][2][11:-7]
        output = name + "[ " + date + "]" + ": " + message
        print(output)
        i += 1





name = input("What is your name? ")
display_msgs()


while True:
    msg1 = input("Please add your message: ")
    add_msg(name, msg1)
    print("\n\n\n\n\n")
    display_msgs()







