from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

textkey = []
def Autobot():
    for sendtxt in textkey:
        time.sleep(0.3)
        keyboard.type(sendtxt)
        time.sleep(0.3)
        keyboard.press(Key.tab)
        time.sleep(0.3)
        # print(sendtxt)


while 1:
    n = int(input("จำนวนที่จะแก้ชื่อ:"))
    for i in range(0, n):
        sum = (n-i)
        print("เหลืออีก",sum)
        in_ck = textkey.append(input("ใส่ชื่อที่จะแก้:"))
        
    if i == n-1:
        print("รออีก 10วินาทีโปรแกรมจะทำงาน เตรียมกดแก้ชื่อรอไว้ได้เลย!")
        time.sleep(10)
        Autobot()
        break