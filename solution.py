# -*- coding: utf-8 -*-

import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from subprocess import Popen, PIPE
from datetime import datetime
import time
import base64

giver = ["손다미", "권희정", "박도연", "심영보", "권영재", "이상훈", "박예림", "황희재"] # 선물 주는 사람
recipient = ["손다미","권희정", "박도연", "심영보", "권영재", "이상훈", "박예림", "황희재"] # 선물 받는 사람
email = {
    "권희정" : "gmlwjd9405@gmail.com",
    "박도연" : "ehdus5958@naver.com",
    "심영보" : "sim4858@naver.com",
    "권영재" : "kyoje11@gmail.com",
    "이상훈" : "ttjs2008@gmail.com",
    "박예림" : "park_yel@naver.com",
    "황희재" : "ghkdrm123@naver.com",
    "손다미" : "son.dami80@gmail.com"
    }

trigger = 1

while (trigger): # 주는사람과 받는사람이 같을 경우 셔플
    #print("shuffle")
    for i in range(len(giver)):
        if (giver[i] == recipient[i]):
            random.shuffle(recipient)
            break
        elif (i == len(giver)-1) :
            trigger = 0


for i in range(len(giver)):
    now = datetime.now() # 현재 시간

    print(giver[i] + "에게 보낸시간 = " + str(now))

    bodyTXT = "당신의 선물을 받을 사람은 '" + recipient[i] + "' 입니다.\n" + "발송시간 : " + str(now)
    #print(bodyTXT)
    msg = MIMEText(bodyTXT)
    msg['Subject'] = '당신의 선물을 받을 사람은!?'
    msg['From'] = email.get("황희재")
    msg['To'] = email.get(giver[i])

    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())

    #print(giver[i] +"       "+email.get(giver[i])+"       "+str(now) +"       "+ recipient[i])
    time.sleep(2)
