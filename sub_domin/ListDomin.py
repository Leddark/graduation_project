



class Domin ():

    def domin_s (name_domin):
        import requests
        import sys
        host = name_domin
        with open("list.txt",mode="r")as f:
            r = f.read()
            subdomains = r.splitlines()
            global list55
            list55 = []
            for sub in subdomains:
                domain = "http://"+ sub + "." + host
                print(domain)
                try:
                    req =  requests.get(domain,"html.parser")
                    if req.status_code == 200:
                        list55.append(domain)
                        print("[+] Discovered subdomain: "+domain)
                
                except requests.ConnectionError:
                    pass
                
                except KeyboardInterrupt:
                    print(list55)
                    print("\nEXIT..")
                    sys.exit()
                



