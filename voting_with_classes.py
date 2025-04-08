import time
import os

President_list = []
gen_secretary_list = []
fin_secretary_list = []
wocom_list = []

class Registration:
    def __init__(self):
        pass

    def P_registration(self):
        os.system("cls")
        print("\nREGISTRATION FOR SRC PRESIDENT")
        no_president = input("\nEnter Number of people for SRC President : ")
        if no_president.isdigit():
            no_president_int = int(no_president)
            for i in range(1, no_president_int + 1):
                p_name = input(f"ENTER NAME OF CANDIDATE {i}: ")
                President_list.append(p_name)
        else:
            os.system("cls") 
            print("\033[31m""\nEnter Numbers only!""\033[0m")
            time.sleep(2)
            os.system("cls")
            self.P_registration()

        os.system('cls')
        print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m")
        time.sleep(2)
        os.system('cls')

    def Gen_secretary(self):
        os.system("cls")
        print("\nREGISTRATION FOR SRC GENERAL SECRETARY")
        no_secretary = input("Enter Number of people for SRC General Secretary: ")
        if no_secretary.isdigit():
            no_secretary_int = int(no_secretary)
            for i in range(1, no_secretary_int + 1):
                s_name = input(f"ENTER NAME OF CANDIDATE {i}: ")
                gen_secretary_list.append(s_name)
        else:
            os.system("cls")
            print("\033[31m""\nEnter Numbers only!""\033[0m")
            time.sleep(2)
            os.system("cls")
            self.Gen_secretary()

        os.system('cls')
        print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m")
        time.sleep(2)
        os.system('cls')

    def Fin_secretary(self):
        os.system("cls")
        print("\nREGISTRATION FOR SRC FINANCIAL SECRETARY")
        no_fin_secretary = input("Enter Number of people for SRC Financial Secretary: ")
        if no_fin_secretary.isdigit():
            no_fin_secretary_int = int(no_fin_secretary)
            for i in range(1, no_fin_secretary_int + 1):
                f_name = input(f"ENTER NAME OF CANDIDATE {i}: ")
                fin_secretary_list.append(f_name)
        else:
            os.system("cls")
            print("\033[31m""\nEnter Numbers only!""\033[0m")
            time.sleep(2)
            os.system("cls")
            self.Fin_secretary()

        os.system('cls')
        print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m")
        time.sleep(2)
        os.system('cls')

    def Wocom(self):
        os.system("cls")
        print("\nREGISTRATION FOR SRC/NUGS Wocom")
        no_wocom = input("Enter Number of people for SRC/NUGS wocom: ")
        if no_wocom.isdigit():
            no_wocom_int = int(no_wocom)
            for i in range(1, no_wocom_int + 1):
                w_name = input(f"ENTER NAME OF CANDIDATE {i}: ")
                wocom_list.append(w_name)
        else:
            os.system("cls")
            print("\033[31m""\nEnter Numbers only!""\033[0m")
            time.sleep(2)
            os.system("cls")
            self.Wocom()    

        os.system('cls')
        print("\033[33m""\nREGISTRATION SUCCESSFUL!""\033[0m")
        time.sleep(2)
        os.system('cls')

class Administration(Registration):
    def Administrator(self):
        os.system('cls')
        print("\033[32m""\nWELCOME TO THE ADMIN PAGE""\033[0m")
        print("\n1. REGISTRATION")
        print("2. VIEW RESULTS")
        print("3. BACK")
        
        admin_option = input("\nPlease enter an option: ")
        
        if admin_option == "1":
            os.system("cls")
            self.P_registration()
            self.Gen_secretary()
            self.Fin_secretary()
            self.Wocom()
            os.system('cls')
            
            print(f"Candidates Registered for SRC President:")
            for p in President_list:
                print(p)
            print(f"\nCandidates Registered for SRC General Secretary:")
            for g in gen_secretary_list:
                print(g)
            print(f"\nCandidates Registered for SRC Financial Secretary:")
            for f in fin_secretary_list:
                print(f)
            print(f"\nCandidates Registered for SRC Wocom:")
            for w in wocom_list:
                print(w)

            time.sleep(5)
            
            while True:
                back = input("\n\n\nDo you want to go Back? Yes / No: ").strip().lower()
                if back in ["yes", "y"]:
                    self.Administrator()
                else:
                    break
                time.sleep(5)

        elif admin_option == "2":
            self.Results()
            
            while True:
                back = input("\n\n\nDo you want to go Back? Yes / No: ").strip().lower()
                if back in ["yes", "y"]:
                    os.system('cls')
                    self.Administrator()
                else:
                    break
        
        elif admin_option == "3": 
            os.system('cls')
            FrontPage().Welcome()
            
        else:
            os.system('cls')
            print("\033[31m""\nEnter a correct option""\033[0m")
            time.sleep(1)
            os.system('cls')
            self.Administrator()

    def Password(self):
        os.system('cls')
        N_passW = input("\nENTER A NEW PASSWORD TO CONTINUE: ")
        NN_pass = input("CONFIRM PASSWORD: ") 
        if N_passW == NN_pass:
            os.system('cls')
            print("\n\033[32m""Successful!""\033[0m")
            time.sleep(2)
            os.system('cls')
            self.Administrator()
        else:
            os.system('cls')
            print("\033[31m""\nPassword do not match""\033[0m")
            time.sleep(2)
            self.Password()       

class VotingProcess:
    def vote_Process(self):
        os.system('cls')
        print("\033[32m""WELCOME TO THE 2024 GENERAL ELECTION""\033[0m")
        vote = input("\nENTER YOUR VOTE: ")

class Results(VotingProcess):
    def Results(self):
        os.system('cls')
        print("Results not available")

class FrontPage(VotingProcess):
    def Welcome(self):
        os.system('cls')
        wlc = "\033[32m""WELCOME TO THE 2024 GENERAL ELECTION""\033[0m"
        wlc = wlc.center(100, '_')
        print(wlc)

        ADMIN = "SRC2024"

        student_id = input("\nEnter your ID Number: ").upper()

        if len(student_id) == 9 and (student_id[:2] in ["UG", "UD"]) and student_id[2:7].isdigit() and student_id[-2:] in ["20", "21", "22", "23"]:
            os.system('cls')
            VotingProcess().vote_Process()
        elif student_id == ADMIN:
            Administration().Password()
        else:
            print("\033[31m""\nENTER A VALID ID NUMBER""\033[0m")
            time.sleep(1)
            os.system('cls')
            self.Welcome()

if __name__ == "__main__":
    FrontPage().Welcome()
