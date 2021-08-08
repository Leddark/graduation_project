from django.shortcuts import render
from Home.views import nameuser
# Create your views here.
from Home.views import Login

def port_scan (request):

    try:
        try:


                

                    domin00 = request.POST.get('domin00')
                    import socket 
                    domin = domin00
                    dominzz = domin.replace("https://","")
                    dominyy = dominzz.replace("/","")
                    dominx = socket.gethostbyname(dominyy)
                    mm = str(dominx)
                    x = mm

                    xuser = nameuser()
                    print(xuser)
                    return render (request , "temp/port_scan.html" , {"mm":mm , 'xuser':xuser} )
        

                    


        except:


            try:
                num1 = request.POST.get('num1')
                num2 = request.POST.get('num2')
                domin = request.POST.get('domin')


                num11 = int(num1)
                num22 = int(num2)

                if num11 >= 1 and num22 <= 65535 :
                    
                    try:

                        x = domin
                        y = x.split('.')
                        lest22 = []
                        for i in y:
                            m = int(i)
                            lest22.append(m)
                        z1 = lest22[0]
                        z2 = lest22[1]
                        z3 = lest22[2]
                        z4 = lest22[3]

                        if z1 >= 0 and  z1 <= 255 :
                            if z2 >= 0 and  z2 <= 255 :
                                if z3 >= 0 and  z3 <= 255 :
                                    if z4 >= 0 and  z4 <= 255 :
                                        print("ssssssssssssssss")

                                    
                                        import socket
                                        list00 = []
                                        list11 = []
                                        for i in range(num11,num22+1):
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            try:
                                                s.connect((domin, i))
                                                s.shutdown(2)
                                                print('T',i)
                                                xy = 'port '+ str(i) +' open'
                                                list00.append(xy)
                                            except:
                                                print('F',i)
                                                xy = 'port '+ str(i) +' closed'
                                                list11.append(xy)
                                        print(list00)

                                        xuser = nameuser()
                                        print(xuser)
                                        return render (request , "temp/port_scan.html" , {'list00':list00 , 'list11':list11 ,'domin':domin , 'num11':num11 , 'num22':num22 , 'xuser':xuser})
                    except:
                        xo = 'الرجاء ادخال دومين صالح'

                        xuser = nameuser()
                        print(xuser)
                        return render (request , "temp/port_scan.html" , {'xo':xo , 'xuser':xuser})

                else:

                    xuser = nameuser()
                    print(xuser)
                    return render (request , "temp/port_scan.html" , { 'num11':num11 , 'num22':num22 , 'xuser':xuser})

                
            except:
                xuser = nameuser()
                print(xuser)
                return render (request , "temp/port_scan.html" , {'xuser':xuser})

    except:

        return Login(request)
