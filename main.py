# This is a sample Python script.
import datetime
import time
from random import random
import telebot
from threading import Timer

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

angelina_telegram_id = 256844493
timur_telegram_id = 673084189
toSend = timur_telegram_id
countMessageDays = 0


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def sendMem():
    count = 0
    x = open('diction.txt', 'r').readlines()
    for i in x:
        count = count + 1
    initBot().send_photo(toSend, x[int(random() * count)])


def days():
    delta = datetime.datetime(2022, 12, 8) - datetime.datetime.now()
    message = "До сдачи пред дипломки осталось: {days} дней(ня)"
    initBot().send_message(toSend, message.format(days=delta.days))


def hello():
    initBot().send_message(toSend, "Пора делать ДИПЛОМ!")


def initBot():
    bot = telebot.TeleBot('5648063800:AAGl8GHVDeeWJmrEI0McVRgAecygxi8rGXk')
    return bot


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
        if (10 <= time.localtime()[3] <= 23 and countMessageDays == 0
                and time.localtime()[4] == 00 and time.localtime()[5] == 00
                and (time.localtime()[3] % 3 == 0 or time.localtime()[3] == 10)):
            hello()
            days()
            sendMem()
            countMessageDays = 1
        elif (10 <= time.localtime()[3] <= 23 and time.localtime()[4] == 00 and
              time.localtime()[5] == 00 and
              (time.localtime()[3] % 3 == 0 or time.localtime()[3] == 10)):
            hello()
            sendMem()
        elif (time.localtime()[3] < 10) and (time.localtime()[3] > 23):
            countMessageDays = 0
        time.sleep(1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
