import os
os.system('xdg-open https://www.facebook.com/profile.php?id=100025897583099')
import mechanize
import os,sys, requests, re, random, time
import datetime
import getpass
import uuid
from os import system as psl
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as bsn
from os import path
import os,base64,zlib,pip,urllib
from urllib.request import urlopen
import os,base64,zlib,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys
import os,base64,zlib,urllib
#===============


#==================PROTECTION=================#



logo = """
\033[1;32m         
\033[1;33m     ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
\033[1;36m.   ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
\033[1;31m    ██║     ███████║███████║██████╔╝███████╗██║
\033[1;32m.   ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
\033[1;34m    ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
\033[1;33m     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
                                     
        \33[37;41m\t WELLCOME TO CH9RSI TOOL\33[0;m
--------------------------------------------------------------------
\033[1;32m          Author     :          Charsi
\033[1;34m          Github     :          Charsi786
\033[1;31m          Version    :          0.2.1
\033[;37m\033[;37m          Tool Type  :          Post / Convo
--------------------------------------------------------------------"""
#===========CONVO============
def send_messages():
    os.system('clear')
    print(logo) 
    #verf()
    #verf2()
    os.system('clear')
    print(logo) 
    name = (input("\033[1;92mTyp Your Name :: ==> "))
    print("-------------------------------------------")
    tokken = (input("\033[1;92mPut Token File :: ==> "))
    try:
      fo = open(tokken,'r').read().splitlines()
    except FileNotFoundError:
          print('\033[1;91m File Not Found ');time.sleep(3)
          send_messages()
    with open(tokken, 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)


    

    

    def liness():
        print('' + '-------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }
    os.system('clear')
    print(logo)
    

    liness()

    access_tokens = [token.strip() for token in tokens]
    os.system('clear')
    print(logo)
    convo_id = (input("\033[1;92mConversation Id :: ==> "))
    print("-------------------------------------------")
    gali = (input("\033[1;92mAbouse File :: ==> "))
    try:
      fo = open(gali,'r').read().splitlines()
    except FileNotFoundError:
          print('\033[1;91m File Not Found ');time.sleep(3)
          send_messages()
    with open(gali, 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    print("-------------------------------------------")
    haters_name = (input("\033[1;92mHaters name :: ==> "))
    print("-------------------------------------------")
    timm = int(input("\033[1;92mSpeed In Second :: ==> "))


    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v15.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)
                
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    os.system('clear')
                    print(logo)
                    print('\033[1;92mMessage Sender ID '+name+' ')
                    print("-------------------------------------------")
                    print("\033[1;92mTool Creater Bholwa Here")
                    print("-------------------------------------------")
                    print("\033[1;92mChla Gya Tera Message {} of Convo {} Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message,"\n",))
                    print("  - Sahi Hai :: ==> Time: {}".format(current_time))
                    liness()
                    liness()
                    #verf()
                    #verf2()
                else:
                    print("\033[1;91mFailed to send Message {} of Convo {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Sahi Hai :: ==> Time: {}".format(current_time))
                    liness()
                    liness()
                    #verf()
                    #verf2()
                time.sleep(timm)

            print("\033[1;92mAll messages sent. Restarting the process...")
        except Exception as e:
            print("\033[1;91mAn error occurred: {}".format(e))
#==========POST METHOD==========
def comment_send():
    os.system('clear')
    print(logo) 
#    verf()
 #   verf2()
    os.system('clear')
    print(logo) 
    name = (input("\033[1;92mTyp Your Name :: ==> "))
    print("-------------------------------------------")
    tokken = (input("\033[1;92mPut Token File :: ==> "))
    try:
      fo = open(tokken,'r').read().splitlines()
    except FileNotFoundError:
          print('\033[1;91mFile Not Found ');time.sleep(3)
          comment_send()
    with open(tokken, 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    

    

    def liness():
        print('' + '-------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }
    

    access_tokens = [token.strip() for token in tokens]
    os.system('clear')
    print(logo)
    profile_id = (input("\033[1;92mYour Profile Link :: ==> "))
    print("-------------------------------------------")
    convo_id = (input("\033[1;92mConversation Post Id :: ==> "))
    print("-------------------------------------------")
    gali = (input("\033[1;92mAbouse File :: ==> "))
    try:
      fo = open(gali,'r').read().splitlines()
    except FileNotFoundError:
          print('\033[1;91mFile Not Found ');time.sleep(3)
          comment_send()
    with open(gali, 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    print("-------------------------------------------")
    haters_name = (input("\033[1;92mHaters Name :: ==> "))
    os.system('clear')
    print("-------------------------------------------")
    timm = int(input("\033[1;92mDelay :: ==> "))

    liness()

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()
                url = f'https://graph.facebook.com/v15.0/{profile_id}_{convo_id}/comments'
                #url = "https://mbasic.facebook.com/{}/comments".format('+convo_id')
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    os.system('clear')
                    print(logo)
                    print('\033[1;92mSender : '+name+' ')
                    print("-------------------------------------------")
                    print("\033[1;92mTool Creater Bholwa Here")
                    print("-------------------------------------------")
                    print("\033[1;92mChla Gya Tera Comment {} of Convo {} Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Sahi Hai :: ==> Time: {}".format(current_time))
                    print("-------------------------------------------")
                else:
                    print("\033[1;92mFailed to send Message {} of Post {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Sahi Hai :: ==> Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(timm)

            print("\033[1;92mAll messages sent. Restarting the process...")
        except Exception as e:
            print("\033[1;91mAn error occurred: {}".format(e))
            
def owner():
	os.system("xdg-open https://www.facebook.com/profile.php?id=100025897583099")        
            

#=========approvel========
os.system('clear')
attemps = 0
while attemps < 12345677901:
    username = input('\n\n\033[1;37mEnter username: ')
    password = input('\033[1;37mEnter password: ')
    if username == 'Legend' and password == 'Charsi':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect Password ')
        attemps += 1
        continue
def approval():
  os.system('git pull')
  time.sleep(1)
  uuid = str(os.geteuid())+"CH9RSI"+str(os.geteuid())
  id = "CH9RSI-TOOL-"+"".join(uuid)
  os.system('clear')
  
  print("\033[1;39m━▷ You Get Approved for Using Command  Paid Tool \033[1;37m")
  print("\n\033[1;39m━▷ Your Key :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑""")
  try:
    httpCaht = requests.get("https://bholwa1234.blogspot.com/2023/11/tokenpost.html").text
    if id in httpCaht:
      print("\n\033[1;39m━▷ Congrats You get approved successful And Enjoy")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      print("\n\033[1;39m━▷ Your Key Not approved please  Say to Admin");
      time.sleep(0.1)
      input('\n\nTool Ka Approval Lene Ke Liye Owner Ko Key Send Kro')
      tks = ('Hello%20Charsi%20Sir%20!%20Please%20Approve%20My%20Key%20!That%20My%20Key%20:%20'+id);os.system('am start https://wa.me/+917891103118?text='+tks),approval()
      time.sleep(1)
      exit()
  except Exception as e:
     print(e)
     sp(" >> Unable Data From Server ")
     time.sleep(2)
     approval()
  except:
    sys.exit()
    
approval()
def bholwa():
  os.system('clear')
  print(logo)
  #verf()
  #verf2()
#  print(logo)
  print(f'\033[1;92m[1] Convo / IB Tool ')
  print(f'\033[1;92m[2] Post Tool ')
  print("\033[1;92m[3] Owner Facebook ID ")
  print("-------------------------------------------")
  abhii = input('\033[1;92m Choose Option : ')
  if abhii =='1':
      send_messages()
  elif abhii =='2':
      comment_send()
  elif abhii =='3':
  	owner()

  

#=======================#

if __name__ == '__main__':
    charsi()


