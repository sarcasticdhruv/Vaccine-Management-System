
import csv
import random
import pickle
import pandas as pd

vaccination_fields=['Name','DOB','Phone','Email','Gender',"ID","AADHAAR No."]
vaccination_database='vaccination.csv'                    


#creating files for before use
vac_fout=open("doses.dat","ab")
vac_fout.close()
feedfile=open("feedback.txt","a")
feedfile.close()
vaccine_main=open(vaccination_database,"w")
vaccine_main.close()

with open(vaccination_database, "a",newline="") as fr:
    vreader=csv.reader(fr)
    try:
        for row in vreader:
            if row[1]=="DOB" or row[2].isnumeric():
                print("True")
                break
            else:
                vwriter=csv.writer(fr)
                vwriter.writerow(vaccination_fields)
                break
            fr.close()
      
    except:
        FileNotFoundError
        with open(vaccination_database, "w",newline='') as fw:
                    vwriter = csv.writer(fw)
                    vwriter.writerow(vaccination_fields)


#login
def login():
    login=60108
    pawd=80106
    value=True
    attempt=3
    print("*** Welcome to the Login page for Vaccination Management ***\n\t[For Official Use Only]")

    while value:
        print("You have only 3 attempts for login\n(Enter carefully)\n")
        l=eval(input("Enter Login ID : "))
        p=eval(input("Enter Password : "))
        if login==l and pawd==p:
            print("You have Logged In successfully")
            break
            
        else:
            attempt-=1
            if attempt==0:
                print("Login limit exceeded - Program suspended")
                value=False
        
            else:
                print("Login credentials Invalid\nTry Again\n")
    while value:
        print("""Choose one option :-
                 1. Change Vaccine Availabilty
                 2. Delete Record
                 3. Logout""")
        ans=input("Choose to proceed : ")
        if ans=='1':
            doses_mod()
        elif ans=='2':
            del_person()
        elif ans=='3':
            print("Logged Out Succesfully")
            break
        else:
            pass

# sub_main
def sub_main():
        while True:
            sdisplay_menu()
            print("-----------------------------------------------------")
            enter=input("\tEnter Your Choice : ")
            print("-----------------------------------------------------")
            if enter=='1':
                add_person()
                book_vaccine()
            elif enter=='2':
                edit_person()
            elif enter=='3':
                search_person()
            elif enter=='4':
                view_persons_table()
            elif enter=='5':
                try:
                    vac_fin=open("doses.dat","rb")
                    vaccine_record = pickle.load(vac_fin)
                    covishield = vaccine_record[0]
                    covaxine = vaccine_record[1]
                    print("Covishield : ",covishield,"\nCovaxine   : ", covaxine)
                except:
                    EOFError
                    vac_fout=open("doses.dat","wb")
                    vac_fout.seek(0)
                    pickle.dump([100,100],vac_fout)
                    vac_fout.close()
                    ac_fin=open("doses.dat","rb")
                    vaccine_record = pickle.load(vac_fin)
                    covishield = vaccine_record[0]
                    covaxine = vaccine_record[1]
                    print("Covishield : ",covishield,"\nCovaxine   : ", covaxine)
                    vac_fout.close()
            elif enter=='6':
                print("------------------------------------------------------")
                break
            else:
                print("Error!!!")
                pass


# display menu
def display_menu():
    print('--------------------------------------------------------------------------------------------')
    print("""\t\t\t\t\t  Def-Cov\n\t\t\t\t     Defeating Covid\n\t\t\t\t[A Vaccine Management System]
    \n\nAre you protected Againt Covid?\t\tVaccines are Safe\t\tBook your slot now\n\n""")
    print('--------------------------------------------------------------------------------------------')
    print("""\nSelect an option :""")
    print("--------------------------------------------------------------------------------------------")
    print(" 1. Open Vaccine Manager (For Public Use - Vaccine Appointment Booking")
    print(" 2. Login (For Authorized Persons Only)")
    print(" 3. How to book vaccine appointment")
    print(" 4. Feedback")
    print(" 5. See our Reviews")
    print(" 6. Exit")
    print("--------------------------------------------------------------------------------------------")


# view feedback
def review():
    try:
        feedin=open("feedback.txt","r")
        feedin.seek(0)
        feed_file=feedin.read()
        print("\nOur Reviews:- ")
        print(feed_file)
        feedin.close()
        
    except:
        EOFError
        print("\nNO Reviews Now\nVisit Later")

#feedback
def feedback():
    feedfile=open("feedback.txt","a")
    feedfile.seek(0)
    feedback_n=input("Enter your Name : ")
    feedback=input("Give your Feedback regarding our system : ")
    feed_list=[feedback_n," : ",feedback]
    feedfile.writelines(feed_list)
    feedfile.writelines("\n")
    feedfile.close()
    print("Thank You for your Feedback\n")
    
# accessing Vaccine doses
def vaccine_doses():
    try:
        vac_fin=open("doses.dat","rb")
        vac_fin.seek(0)
        vaccine_record = pickle.load(vac_fin)
        covishield = vaccine_record[0]
        covaxine = vaccine_record[1]
        vac_fin.close()
    except:
        EOFError
        vac_fin=open("doses.dat","wb")
        vac_fin.seek(0)
        covishield = 100
        covaxine = 100
        pickle.dump([covishield,covaxine],vac_fin)
        vac_fin.close()
    

# modifying vaccine doses
def doses_mod():
    vac_fout=open("doses.dat","wb")
    vac_fout.seek(0)
    covishield_dos=input("Enter the modified doses for Covishield : ")
    covaxine_dos=input("Enter the modified doses for Covaxine : ")
    pickle.dump([covishield_dos,covaxine_dos],vac_fout)
    vac_fout.close()
    print("Doses updated succesfully")
    
#sub-Display menu
def sdisplay_menu():
    print("-------------------------------------------------------")
    print("               WELCOME TO VACCINATION MANGER           ")
    print("-------------------------------------------------------")
    print(" Please select any one otion:-                         ")
    print("-------------------------------------------------------")
    print("    1. Register for Vaccination                        ")
    print("    2. Edit your Credentials                           ")
    print("    3. Search for your Vaccine Booking details         ")
    print("    4. View Vaccinated Persons LIST                    ")
    print("    5. Vaccine availablity check                       ")
    print("    6. Back                                            ")
    print("-------------------------------------------------------")


# ADD VACCINATED PERSON
def add_person():

    print("*******************************************************")
    print("\t\t\tEnter your Details")
    print("*******************************************************")
    global vaccination_fields
    global vaccination_database

    vaccinated_person_data = []
    
    for field in vaccination_fields:
        ID=random.randint(1111,9999)
        if field=="ID":
            value = ID
            vaccinated_person_data.append(value)
            print("\nYour ID is ",ID,"\nNote it down for further use\n")

        elif field=="DOB":
            while True:
                value=input("Enter your Date of Birth [DD/MM/YYYY]: " )
                if len(value)==10:
                    if value[2]=="/" and value[5]=="/" :
                        if int(value[6:10])<=2003:
                            vaccinated_person_data.append(value)
                            break
                        else:
                            print("Your Age is Below 18 Years\n")
                    else:
                        print("Invalid Date of Birth\n")
                else:
                    print("Invalid Date of Birth\n")
       
        elif field=="Phone":
            while True:
                value=input("Enter your Mobile No.: ")
                if len(value)==10:
                    if value.isnumeric():
                        vaccinated_person_data.append(value)
                        break
                    else:
                        print("Invalid Mobile No.\n")
                else:
                    print("Invalid Mobile No.\n")
        elif field=="Email":
            while True:
                value=input("Enter your Email ID : ")
                if '@'in value and '.com' in value:
                    vaccinated_person_data.append(value)
                    break  
                else:
                    print("Invalid Email ID\n")
                    
        elif field=="Gender":
            while True:
                value=input("Enter your Gender [Male / Female / Other] : ")
                if value.lower()=='male' or value.lower()=='female' or value.lower()=='other':
                   vaccinated_person_data.append(value)
                   break
                else:
                    print("Invalid Gender\n")

        elif field=="AADHAAR No.":
            while True:
                value = input("Enter your Aadhar No. [XXXX-XXXX-XXXX] : " )
                if len(value)==14:
                    if value[4]=='-' and value[9]=='-':
                        vaccinated_person_data.append(value)
                        break
                    else:
                        print("Invalid Aadhaar No.\n")
                else:
                    print("Invalid Aadhaar No.\n")
                              
        else:
            value = input("Enter your " + field + " : ")
            vaccinated_person_data.append(value)

    with open(vaccination_database, "a",newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([vaccinated_person_data])

    print("Vaccine Regestration Completed")
    input("Press any key to continue for Vaccine Booking")
    return

# vaccine booking
def book_vaccine():
    from datetime import date, timedelta
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    value=True

    while value:
        try :
            vac_fin=open("doses.dat","rb")
            vac_fin.seek(0)
            vaccine_record = pickle.load(vac_fin)
            covishield = int(vaccine_record[0])
            covaxine = int(vaccine_record[1])
            vac_fin.close()
        except:
            EOFError
            vac_fin=open("doses.dat","wb")
            vac_fin.seek(0)
            covishield = 100
            covaxine = 100
            pickle.dump([covishield,covaxine],vac_fin)
            vac_fin.close()
        if covishield=='0' and covaxine=='0':
            print("\nNo Dose Available\nTry again later")
            break
        print("""\nWhich vaccine you want to have :
                1. Covishield (Availability of Doses : """, covishield,"\n"
             """\t\t2. Covaxine (Availability of Doses : """, covaxine)
        
        vaccine=['Covishield','Covaxine']
        while True:
            ask_v=eval(input("Choose which vaccine : "))
            if ask_v==1:
                covishield-=1
                break
            elif ask_v==2:
                covaxine-=1
                break
            else:
                print("Invalid Request\n")
                
        print("You have initiated booking for ",vaccine[ask_v-1],"Vaccine\n")
        cov_file=open("doses.dat","wb")
        cov_file.seek(0)
        pickle.dump([covishield,covaxine],cov_file)
        cov_file.close()

        while value:
            print("\nCongratulations!!! \nYou have been succesfully vaccinated on (Today)",d1, " by vaccine : ",vaccine[ask_v-1])
            value=False

#DELETE VACCINATED PERSON INFORMATION
def del_person():
    global vaccination_fields
    global vaccination_database
    print("----------------------------------------------------")
    print("--------- Delete Vaccinated Person Record ----------")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    with open(vaccination_database)as csvfile:
            reader = csv.DictReader(csvfile)
            deletion = input("Enter Id to delete: ")
            print("----------------------------------------------------")
            pcsv=0
            for row in reader:
                pcsv+=1
                print(pcsv)
                if deletion == row["ID"]:
                    fcsv=pd.read_csv("vaccination_database")
                    fcsv.drop(pcsv-1,axis=0,inplace=True)
                else:
                    pass
                
                

                print("Record Deleted")
    input("Press any key to continue")

#edit vaccination record
def edit_person():
    global vaccination_fields
    global vaccination_database
    red=pd.read_csv(vaccination_database)
    ask_rec=input("Enter the ID : ")
    ask_name=input("Enter the Name registered during regestration : ")
    pointer=-2
    with open(vaccination_database, "r",encoding="utf-8") as f:
        sreader = csv.reader(f)
        for rec in sreader:
            pointer+=1
     
            if str(rec[5])==ask_rec and rec[0]==ask_name:
                print("ID Found")
                print("""What do you wanna Update :
                          1. Mobile No.
                          2. Email ID
                          3. Exit""")
                print("[Only Given Below Objects can be Updated!!!]")
                ask_ch=input("Choose from the above options : ")

                if ask_ch=='1':
                    ask_mb=input("Enter the New Mobile No.:")
                    red.loc[pointer, 'Phone'] = ask_mb
                    print("Data Edited Succesfully!!")
                    break
                    
                elif ask_ch=='2':
                    ask_mb=input("Enter the New Email ID : ")
                    red.loc[pointer, 'Email'] = ask_mb
                    print("Data Edited Succesfully!!")
                    break

                else:
                    break
                break
            else:
                print("id not found in our database")

    red.to_csv(vaccination_database, index=False)
    input("Press any key to continue")   

    
#SEARCH VACCINATED PERSONS
def search_person():
    global vaccination_fields
    global vaccination_database
    print("---------------------------------------------")
    print("-------- Search Vaccinated Person -----------")
    print("---------------------------------------------")
    roll = input("Enter id to search: ")
    with open(vaccination_database, "r",newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[5]:
                    print("---------------------------------------------")
                    print("--------------- Vaccinator Found ------------")
                    print("---------------------------------------------")
                    print("   Name    :\t", row[0])
                    print("   DOB     :\t", row[1])
                    print("   Gender  :\t", row[2])
                    print("   Email   :\t", row[3])
                    print("   Phone   :\t", row[4])
                    print("   ID      :\t", row[5])
                    print("   Status  :\t","Vaccinated")
                    break
        else:
            print("--------------------------------------")
            print("   Id not found in our database       ")
            print("--------------------------------------")
    input("Press any key to continue")
#DISPLAY VACCINATED PERSONS LISTS
def view_persons_table():
    import csv
    from prettytable import PrettyTable

    stable=PrettyTable()
    with open(vaccination_database, "r",newline="") as pt:
        sreader=csv.reader(pt)
        for row in sreader:
            if sreader.line_num==1:
                stable.field_names=row
            else:
                stable.add_row(row)
    print(stable)

#HOW TO BOOK VACCINES
def how_vac():
    print("---------------------------------------------------------------------------")
    print("Provided are the Steps to Book Vaccine Appointment :-")
    print("1. Open Vaccine Manager (For Public Use - Vaccine Appointment Booking")
    print("2. Click Register for Vaccination ")
    print("3. Enter your Information as asked carefully")
    print("4. Choose the vaccine")
    print("5. Enter Time time slot for vaccine appointment")
    print("6. And your Vaccine Appointment would be successful")
    print("|`````````````````````````````````````````````````````````````````````````|")
    print("|                          **For any Query:**                             |")
    print("|                       HELPLINE NO. 5667576575                           |")
    print("|.........................................................................|")
    
    
#MAIN SOURCE CODE
while True:
    display_menu()
    ask_main=input("Enter your choice : ")
    if ask_main=='1':
        sub_main()
    elif ask_main=='2':
        login()
    elif ask_main=='3':
        how_vac()
    elif ask_main=='4':
        feedback()
    elif ask_main=='5':
        review()
    elif ask_main=='6':
        print("---------------------------------------------------------------------------")
        print("----------THANKS FOR USING OUR SYSTEM YOU DATA IS SAFE WITH US-------------")
        print("---------------------------------------------------------------------------")
        print("---------------------------________________--------------------------------")
        print("--------------------------/   Created By : \-------------------------------")
        print("-------------------------|  Dhruv Choudhary |------------------------------")
        print("---------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------")
        break
    else:
        print("Invalid Request\nTry Again")
    
    
        

        

