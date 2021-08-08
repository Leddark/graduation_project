from django.shortcuts import render,redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests import get
from . import models



def Home (request):
    try:

        name1 = 'عبدالله مازن الحداد'
        User = 'leddark'
        email = 'abood.leddark@gmail.com'
        password = '123456789'
        return render (request , "temp/Home.html" , {'name1':name1 , 'User':User , 'email':email , 'password':password})
    
    

        
    except:

        return Login(request)

def Assess (request):


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
            msg['Subject'] = 'تقيم مشروع التخرج'
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


            name1 = 'عبدالله مازن الحداد'

            return render (request , "temp/Assess.html" , {'name1':name1})

        except:


            name1 = 'عبدالله مازن الحداد'

            return render (request , "temp/Assess.html" , {'name1':name1} )
    except:

        return Login(request)


def massage (request):
    try:
        try:
            name1 = request.POST.get('contact_name')
            Massage1 = request.POST.get('contact_email')
            Assess1 = request.POST.get('contact_message')

            ########################
            From = "lidark.tool@gmail.com"
            password = 'mmoohhaa12345'
            To = 'adrelaft@outlook.com'
            msg = MIMEMultipart()
            msg['From'] = From
            msg['To'] = To
            msg['Subject'] = 'رسالة خاصة'
            body = "اسم الشخص : \n" + name1 + '\n\n' + 'البريد الإلكتروني : \n' + Massage1 + '\n\n' + "الرسالة : \n" + Assess1
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(From, password)
            text = msg.as_string()
            server.sendmail(From, To, text)
            print(f'Send Done To {To}')

            server.quit()
            ########################


            name1 = 'عبدالله مازن الحداد'

            return render (request , "temp/massage.html" , {'name1':name1} )

        except:


            name1 = 'عبدالله مازن الحداد'

            return render (request , "temp/massage.html" ,{'name1':name1})
    except:

        return Login(request)


def path_security (request):

    try:

        name1 = 'عبدالله مازن الحداد'

        return render (request , "temp/path_security.html" ,{'name1':name1} )
    except:

        return Login(request)


def CV_Ahmed (request):
    return render (request , "temp/cvahmed.html" )


def Login (request):

  
    try:

        global user22
        user22 = request.POST.get('user22')
        pass22 = request.POST.get('pass22')


        if user22 == "12345" and pass22 == "12345":
            name1 = 'عبدالله مازن الحداد'
            User = 'leddark'
            email = 'abood.leddark@gmail.com'
            password = '123456789'
            return render (request , "temp/Home.html" , {'name1':name1 , 'User':User , 'email':email , 'password':password})
        
        




        else:
            
            return render (request , "temp/login.html")

    except:
        return render (request , "temp/login.html" , {'user22':user22 , 'pass22':pass22})


def nameuser ():
 


    
    name1 = 'عبدالله مازن الحداد'
    
    return name1



# الدالة التي تظهر الفورم للمستخدم
def Sign_Up (request):
    
    return render (request , "temp/Sign_Up.html" )

# الدالة التي ترسل بيانات الفورم الى قاعدة البيانات
def Sign_Up_Send (request):


    return render(request,'temp/Sign_Up.html')




