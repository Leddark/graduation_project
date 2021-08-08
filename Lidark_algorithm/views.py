from django.shortcuts import render

# Create your views here.

import time
import random
from django.shortcuts import render,redirect


from Home.views import nameuser
from Home.views import Login
from Home import models

def encrypt (request):

    

    try:

        try:

            
            
            username1 = request.POST.get('floatingTextarea2')
            
            import random
            list1 = []
            list2 = []

            # ازالة الفراغات واستبدال كل فراغ ب نجمتين
            dataUser = username1
          
            x = dataUser.replace("\n","**")
            y = x.replace(" ","++")
            #lines = x.split("\n")
            #print(y)

            for item1 in y:

                while True:
                    randomNum = random.randint(33,122) 
                    resu1 = format(ord(item1))
                    resu2 = int(resu1)

                    
                    resu3 = resu2 - randomNum 
                    resu4 = abs(resu3)    
                    resu5 = resu4 + 33

                    xxxx = resu5+randomNum
                    xxx2 = xxxx - 33
                    xxx3 = abs(xxx2)

                    if int(resu1) == xxx3:
                        resu6 = chr(resu5) 
                        resu7 = chr(randomNum) 
                        result = resu6 + resu7 
                        list1.append(result)  
                        list2.append(resu5)
                        list2.append(randomNum)
                        
                        break
                    if int(resu1) != xxx3:
                        pass

            total1 = 0
            for item2 in list2:
                total1 = total1 + item2
            total2 = total1 + 150

            strTotal1 = str(total2)

            total3 = strTotal1 + str(list2[0]) + str(list2[1] )

            print(xxx3 , resu1)

            print(list2)

            total4 = ''
            for item2 in list1: 
                total4 = total4 + item2
            print("has :",total4)
            print("kay :",total3)
                    
            xuser = nameuser()
            print(xuser)
            return render (request , "htmlpost/home.html" , {'usersc':dataUser , 'total':total4 , 'ooqq':total3 , 'xuser':xuser })
     
        except:
            xuser = nameuser()
            print(xuser)
            return render (request , "htmlpost/home.html" ,{'xuser':xuser})
    except:

        return Login(request)

def decrypt (request):
    try:
        try:
            username = request.POST.get('floatingTextarea1')
            userkay = request.POST.get('kayuser')

            
            list11 = []
            list22 = []


            dataUser1 = username

            for item11 in dataUser1:
                resu11 = format(ord(item11))
                resu22 = int(resu11)
                list11.append(resu22)
            print(list11)

            total1 = 0
            for item2 in list11:
                total1 = total1 + item2
            total2 = total1 + 150
            strTotal1 = str(total2)
            total3 = strTotal1 + str(list11[0]) + str(list11[1] )


            op = 0
            cp = 1 
            lenlist11 = len(list11) - 1
            while cp <= lenlist11:
                lm = list11[op] + list11[cp] - 33 # بعد جمع كل عددين نطرحه من 39
                chrlm = chr(lm)
                list22.append(chrlm)
                op = op + 2;cp = cp + 2
            total4 = ''
            for item2 in list22: # جمع الاعداد التي تم تحويلها سابقا 
                total4 = total4 + item2

            x = total4.replace("**","\n")
            y = x.replace("++"," ")

            #print(list22)
            print("has :",y)
            print("kay :",total3)
            vvv = 'عزيزي المستخدم المفتاح أو النص المشفر الذي أدخلته خاطئ '
            if userkay == total3:

                xuser = nameuser()
                print(xuser)
                return render (request , "htmlpost/hom2.html" , {'xuser':xuser ,'user55':dataUser1 , 'total1':y , 'ooqq':total3 ,'userkay':userkay})
            else:

                xuser = nameuser()
                print(xuser)
                return render (request , "htmlpost/hom2.html",{"vvv":vvv , 'xuser':xuser})
        except:
            xuser = nameuser()
            print(xuser)
            return render (request , "htmlpost/hom2.html" , {'xuser':xuser})
    except:

        return Login(request)




def index (request):

    
    try:
        xuser = nameuser()
        print(xuser)
    
        return render (request , "htmlpost/index.html" ,{'xuser':xuser})
    except:

        return Login(request)






from django.shortcuts import render,redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests import get

def message (request):

    try:
        try:
            name1 = request.POST.get('name111')
            Massage1 = request.POST.get('Massage111')
            Assess1 = request.POST.get('rating1')
            Assess1 = str(Assess1)

            ########################
            From = "lidark.tool@gmail.com"
            password = 'mmoohhaa12345'
            To = 'adrelaft@outlook.com'
            msg = MIMEMultipart()
            msg['From'] = From
            msg['To'] = To
            msg['Subject'] = 'تقيم خوارزمية ليدارك'
            body = "اسم الشخص : \n" + name1 + '\n\n' + 'التقيم : \n' + Massage1 + '\n\n' + "نسبة التقيم : \n" + Assess1 +"/5"
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(From, password)
            text = msg.as_string()
            server.sendmail(From, To, text)
            print(f'Send Done To {To}')

            server.quit()
            ########################

            xuser = nameuser()
            print(xuser)

            return render (request , "htmlpost/message.html" ,{'xuser':xuser})

        except:

            xuser = nameuser()
            print(xuser)

            return render (request , "htmlpost/message.html" ,{'xuser':xuser})

    except:

        return Login(request)











