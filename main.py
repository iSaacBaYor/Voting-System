import time
import os
# Lists are used to store the names of aspirants registered
President_list = []
gen_secretary_list = []
fin_secretary_list = []
wocom_list = []

def P_registration(): #the main part of the code that is doing the registrtion as used by thr admin only
  
   os.system("cls")
   print("\nREGISTRATION FOR SRC PRESIDENT")
   no_president = input("\nEnter Number of people for SRC President : ")
   if no_president.isdigit():
    no_president_int=int(no_president)
    for i in range(1,no_president_int+1):
        p_name = input(f"ENTER NAME OF CANDIDATE {i}: ")
        President_list.append(p_name)
   else:
      os.system("cls") #this clears the screen
      print("\033[31m""\nEnter Numbers only!""\033[0m")
      time.sleep(2)
      os.system("cls")
      P_registration()

   os.system('cls')
   print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m") # a green colour is applied 
   time.sleep(2)
   os.system('cls')

def Gen_secretary():
    
    os.system("cls")
    print("\nREGISTRATION FOR SRC GENERAL SECRETARY")
    no_secretary = (input("Enter Number of people for SRC General Secretary: "))
    if no_secretary.isdigit():
     no_secretary_int=int(no_secretary)
     for i in range(1, no_secretary_int + 1):
        s_name = input(f"ENTER NAME OF CANDIDATE {i}: ") # a loop for the number of positions
        gen_secretary_list.append(s_name)

    else:
      os.system("cls")
      print("\nEnter Numbers only!") 
      time.sleep(2)
      os.system("cls")
      Gen_secretary()

    os.system('cls')
    print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m")
    time.sleep(2)
    os.system('cls')


def Fin_secretary():
    
    os.system("cls")
    print("\nREGISTRATION FOR SRC FINANCIAL SECRETARY")
    no_fin_secretary = (input("Enter Number of people for SRC Financial Secratary: "))
    if no_fin_secretary.isdigit():
     no_fin_secretary_int=int(no_fin_secretary)
     for i in range(1, no_fin_secretary_int + 1):
        f_name = input(f"ENTER NAME OF CANDIDATE {i}: ")
        fin_secretary_list.append(f_name)

    else:
      os.system("cls")
      print("\nEnter Numbers only!") 
      time.sleep(2)
      os.system("cls")
      Fin_secretary()

    os.system('cls')
    print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m")
    time.sleep(2)
    os.system('cls')

def Wocom():
    
    os.system("cls")
    print("\nREGISTRATION FOR SRC/NUGS Wocom")
    no_wocom = (input("Enter Number of people for SRC/NUGS wocom: "))
    if no_wocom.isdigit():
     no_wocom_int=int(no_wocom)
     for i in range(1, no_wocom_int + 1):
        w_name = input(f"ENTER NAME OF CANDIDATE {i}: ")
        wocom_list.append(w_name) # the append keyword adds to the list

    else:
      os.system("cls")
      print("\nEnter Numbers only!") 
      time.sleep(2)
      os.system("cls")
      Wocom()    

    os.system('cls')
    print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m")
    time.sleep(2)
    os.system('cls')

def Administrator():
   #os.system('cls')
   print("\033[32m""\nWELCOME TO THE ADMIN PAGE""\033[0m")
   print("\n1. REGISTRATION")
   print("2. VIEW RESULTS")
   print("3. BACK")
   
   admin_option=input("\nPlease enter an option: ")
   
   
   if (admin_option=="1"):
      os.system("cls")
      P_registration()
      Gen_secretary()
      Fin_secretary()
      Wocom()
      os.system('cls')
      
      print(f"Candidates Registered for SRC President" )
      for p in President_list:
         print(p)
      print (f"\nCandidates Registered for SRC General Secretary ")
      for g in gen_secretary_list:
         print(g)
      print (f"\nCandidates Registered for SRC Financial Secretary")
      for f in fin_secretary_list:
         print(f)
      print (f"\nCandidates Registered for SRC Wocom")
      for w in wocom_list:
         print(w)

      time.sleep(5)
     
      while True:
        back=input("\n\n\nDo you want to go Back? Yes / No: ")
        if back=="Yes"  or back=="Y" or back=="YES" or back=="y" or back=="yes":
         Administrator()
        else:
          pass
        time.sleep(5)

   elif(admin_option=="2"):
      Results()  
      
      while True:
         back=input("\n\n\nDo you want to go Back? Yes / No: ")
         if back=="Yes"  or back=="Y" or back=="YES" or back=="y" or back=="yes":
            os.system('cls')
            Administrator()
         else:
            pass  
       
   elif(admin_option=="3"): 
      os.system('cls')
      Welcome()  
         
   else:
      os.system('cls')
      print("\033[31m""\nEnter a correct option""\033[0m")
      
      time.sleep(1)
      os.system('cls')
      Administrator()


def Password():
   os.system('cls')
   N_passW=input("\nENTER A NEW PASSWORD TO CONTINUE: ")
   NN_pass=input("CONFIRM PASSWORD: ") 
   if N_passW==NN_pass:
    os.system('cls')
    print ("\n\033[32m""Successful!""\033[0m")
    time.sleep(2)
    os.system('cls')
    Administrator()
   else:
      os.system('cls')
      print("\033[31m""\nPassword do not match""\033[0m")
      time.sleep(2)
      Password()
      

def vote_Process():
   os.system('cls')
   print("\033[32m""WELCOME TO THE 2024 GENERAL ELECTION""\033[0m") # this is for changing the color

   vote=input("\nENTER YOUR VOTE: ")
   

def Results():
    os.system('cls')
    print("Results not available ")   

def Welcome():
    os.system('cls')
    wlc= "\033[32m""WELCOME TO THE THE 2024 GENERAL ELECTION""\033[0m"
    wlc=wlc.center(100,'_')
    print(wlc)

    
    ADMIN = ("src2024").upper()

    student_id=input("\n Enter your ID Number: ").upper()


    if len(student_id)==9 and ((student_id[:2])=="UG" or (student_id[:2])=="UD") and student_id[2:7].isdigit() and student_id[-2:] in ["20","21", "22", "23"]:
        os.system('cls')
        vote_Process()
    

    elif student_id==ADMIN:
        Password()
    else:
        print("\033[31m""\nENTER A VALID ID NUMBER""\033[0m")
        time.sleep(1)
        os.system('cls')
        Welcome()
     
Welcome()



































































