from django.shortcuts import render
from . ListDomin import Domin
from Home.views import nameuser
from Home.views import Login


def sub_domains (request):
    try:

        try:
            domin55 = request.POST.get('domin55')
            print(domin55)
            print(type(domin55))

            import requests
        
                
            host = domin55

            if host == "None":

                xuser = nameuser()
                print(xuser)
                return render(request , 'temp/sub_domains.html' , {'xuser':xuser})

            else:
                domain = host

                

                subdomains = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test', 'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3', 'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx', 'static', 'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img', 'www1', 'intranet', 'portal', 'video', 'sip', 'dns2', 'api', 'cdn', 'stats', 'dns1', 'ns4', 'www3', 'dns', 'search', 'staging', 'server', 'mx1', 'chat', 'wap', 'my', 'svn', 'mail1', 'sites', 'proxy', 'ads', 'host', 'crm', 'cms', 'backup', 'mx2', 'lyncdiscover', 'info', 'apps', 'download', 'remote', 'db', 'forums', 'store', 'relay', 'files', 'newsletter', 'app', 'live', 'owa', 'en', 'start', 'sms', 'office', 'exchange', 'ipv4']


                
                listdata = []
                for subdomain in subdomains:

                    try:

                        url1 = f"http://{subdomain}.{domain}"
                        url2 = f"https://{subdomain}.{domain}"

                        try:

                            domin00 = url1
                            import socket 
                            domin = domin00
                            dominzz = domin.replace("http://","")
                            dominyy = dominzz.replace("/","")
                            dominx = socket.gethostbyname(dominyy)
                            mm = str(dominx)
                            x = mm

                            requests.get(url1)
                            print(f"Discovered URL: {url1}")
                            listdata.append(url1 + " : " +x)
                            


                            domin00 = url2
                            import socket 
                            domin = domin00
                            dominzz = domin.replace("https://","")
                            dominyy = dominzz.replace("/","")
                            dominx = socket.gethostbyname(dominyy)
                            mm = str(dominx)
                            x = mm
                            requests.get(url2)
                            print(f"Discovered URL: {url2}" )
                            listdata.append(url2 + " : "+ x)
                        except requests.ConnectionError:
                            pass
                    except:
                        pass     


                numdata = len(listdata)

                xuser = nameuser()
                print(xuser)
                context = {
                        'list55':listdata,
                        'host':host,
                        'numdata':numdata,
                        'xuser':xuser
                    

                }


                return render(request , 'temp/sub_domains.html' ,context)
        except:
            
            xuser = nameuser()
            print(xuser)
            return render(request , 'temp/sub_domains.html' , {'xuser':xuser})
    except:

        return Login(request)











