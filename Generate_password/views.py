from django.shortcuts import render
from Home.views import nameuser
# Create your views here.
from Home.views import Login

def Generate_password (request):

    try:
        try:


            usro11 = request.POST.get('usro1')
            usro22 = request.POST.get('usro2')
            usro1 = int(usro11)
            usro2 = int(usro22)

            
            if usro1 >= 8 and usro1 <= 32 :
                if usro2 >= 1 and usro2 <= 500 :

                    im = 0
                    datalisty = []
                    while im < usro2 :
                        numli = usro1 - 1

                        import random

                        listCode1 = []
                        listCode2 = []
                        listCode3 = []
                        # رموز و ارقام
                        for i in range(33,65):
                            x = chr(i)
                            listCode1.append(x)

                        # حروف كابتل
                        for i in range(65,91):
                            x = chr(i)
                            listCode2.append(x)

                        # حروف سمول
                        for i in range(97,123):
                            x = chr(i)
                            listCode3.append(x)

                        while True:
                            randomNum = random.randint(65,91) 
                            xgg = chr(randomNum)
                            if xgg in listCode2:
                                break
                            else:
                                pass

                        g = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 
                        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                        list33 = []
                        e = 0
                        while e < numli :
                            hh = random.choice(g)
                            list33.append(hh)
                            e = e + 1

                        total = ''
                        for x in list33:
                            total += x

                        data = xgg + total

                        
                        if data[0] in listCode2 :
                            datalisty.append(data)
                            print(data)
                            im = im + 1
                    xuser = nameuser()
                    print(xuser)
                    return render(request , 'temp/Generate_password.html',{'datalisty':datalisty , 'xuser':xuser})

                else:
                    rrr = "اقصى حد 500 واقل حد 1"
                    xuser = nameuser()
                    print(xuser)
                    return render(request , 'temp/Generate_password.html',{'rrr':rrr , 'xuser':xuser})

            else:
                kk = "يجب ان يكون عدد الحروف من 8 الى 32"
                xuser = nameuser()
                print(xuser)
                return render(request , 'temp/Generate_password.html',{'kk':kk , 'xuser':xuser})
                    

        except:

            xuser = nameuser()
            print(xuser)
            return render(request , 'temp/Generate_password.html' , {'xuser':xuser})
    except:

        return Login(request)