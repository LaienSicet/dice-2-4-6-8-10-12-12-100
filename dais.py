from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from random import randint
From, Window = uic.loadUiType("inter.ui")

stroka = ""
kybi = ""

def brosok(d, skolko=1):
    kybi1 = []
    for i in range(skolko):
        br = randint(1, d)
        kybi1.append(br)

    return kybi1

def itog(stroka):
    if len(stroka) <= 2:
        return "   " + stroka
    elif len(stroka) == 3:
        return "  " + stroka
    elif len(stroka) == 4:
        return " " + stroka
    elif len(stroka) == 5:
        return stroka
    else:
        return "ОЙ!!!"

def fy_2():
    br_ky(2)

def fy_4():
    br_ky(4)

def fy_6():
    br_ky(6)

def fy_8():
    br_ky(8)

def fy_10():
    br_ky(10)

def fy_12():
    br_ky(12)

def fy_20():
    br_ky(20)

def fy_100():
    br_ky(100)

def br_ky(d):
    s = form.plainTextEdit.toPlainText()
    kybi = ""
    if not(s.isdigit()):
        kybi1 = brosok(d)
    else:
        kybi1 = brosok(d, int(s))
    stroka = str(sum(kybi1))
    stroka = itog(stroka)
    kybi1 = map(str, kybi1)
    for i, n in enumerate(kybi1):
        kybi += "  " + n
        if (i+1) % 13 == 0 and d <= 8:
            kybi += "\n"
        elif (i+1) % 9 == 0 and 8 < d <= 100:
            kybi += "\n"

    form.label.setText(kybi)
    form.label_2.setText(stroka)

app = QApplication([])
window = Window()
form = From()
form.setupUi(window)
window.show()

form.label.setText(kybi)
form.label_2.setText(stroka)

form.pushButton.clicked.connect(fy_2)
form.pushButton_2.clicked.connect(fy_4)
form.pushButton_7.clicked.connect(fy_6)
form.pushButton_4.clicked.connect(fy_8)
form.pushButton_6.clicked.connect(fy_10)
form.pushButton_3.clicked.connect(fy_12)
form.pushButton_8.clicked.connect(fy_20)
form.pushButton_5.clicked.connect(fy_100)

app.exec_()

