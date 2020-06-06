
import sys

class PatientManagement:
        def __init__(self):
                self.patient_dict = {}
                self.file_name = input("Enter the file Name: ")
                self.read_patients_file(self.file_name)
	
        def read_patients_file(self, file_name):
                while True:
                        try:
                                with open(file_name, 'r') as file:
                                        
                                        file= file.readlines()
                                        i=0
                                        for line in file:
                                                self.patient_dict[i]=line
                                                i+=1
                                                number_lines=len(file)
                        
                                        print ("Loaded", number_lines, "records from file")
                                        self.main_menu()
                        except FileNotFoundError:
                            print ("Could not find the file")
                        except OSError :
                            print (" file found - error reading the file")
                        
                        self.__init__()
                        
                
	
	
        def main_menu(self):
                print("##########################################################")
                print("########               MAIN MENU               ###########")
                print("##########################################################")
                print("########   1.Add Patient                       ###########")
                print("########   2.View patient at specific Index    ###########")
                print("########   3.view all patients                 ###########")
                print("########   4.Search for Patient                ###########")
                print("########   5.Exit                              ###########")
                print("##########################################################")
                print ('\n')

                option= int(input("Select an option :"))
                if   option == 1:
                        self.add_patient()
                elif option == 2:
                        while True:
                                print("number of patients in patient dicrionary are:", len(self.patient_dict), ", selcet any index between 0 and ", int(len(self.patient_dict))-1)
                                try:
                                        ind =int(input("enter the index number: "))
                                
                                        if ind < 0 or ind > int(len(self.patient_dict))-1 :
                                                print(" this index is out of range try another one")
                                        else:
                                                self.find_patient_at_index(ind)
                                except ValueError:
                                        print ("invalid patient index")
                elif option == 3:
                        self.show_all()
                elif option == 4:
                        self.find_patient_with_name()
                elif option == 5:
                        self.call_exit()
		


        def add_patient(self):
                i=4
                while True:
                        name= str(input("Enter name to added: "))
                        ssn= input("Enter SSN to be added (xxx-xx-xxxx): ")
                        age= str(input("Enter Age to be added :"))
                        diag= input("Enter DIAGNOSIS to be added :")
    
                        self.patient_dict[i]=str(name+','+ ssn+','+age+','+diag+'\n') 
                        print("new record added")

                        x= input("wanna add another one (y/n)?")
                        if x.lower() == 'y':
                                continue
                        else:
                                print(self.main_menu())
                                break
                self.call_exit()

	
        def find_patient_at_index(self, ind_to_returned):
                
                print('{:15}'.format('NAME'), '{:15}'.format('SSN'), '{:15}'.format('AGE'), '{:15}'.format('DIAGNOSIS'))
                print("-"*70)
                name, ssn, age, diag =self.patient_dict[ind_to_returned].split(',')
                print('{:15}'.format(name), '{:15}'.format(ssn), '{:15}'.format(age), '{:15}'.format(diag))
               
                print(self.main_menu())
                                
                	
        def show_all(self):
                print('{:15}'.format('NAME'), '{:15}'.format('SSN'), '{:15}'.format('AGE'), '{:15}'.format('DIAGNOSIS'))
                print("-"*70)
                i=0
                for i in self.patient_dict:
                        name, ssn, age, diag =self.patient_dict[i].split(',')
                        print('{:15}'.format(name), '{:15}'.format(ssn), '{:15}'.format(age), '{:15}'.format(diag))
                        print("-"*70)
                print(self.main_menu())       
		


        def find_patient_with_name(self):
                i=0
                patient_check=0
                names=input("Enter the patient to be searched with Name: ")
                for i in self.patient_dict.keys():
                        names=names.title()
                        name, ssn, age, diag =self.patient_dict[i].split(',')
                        if names == name:
                                if names in self.patient_dict[i]:
                                        print('{:15}'.format('NAME'), '{:15}'.format('SSN'), '{:15}'.format('AGE'), '{:15}'.format('DIAGNOSIS'))
                                        print("-"*70)
                                        print('{:15}'.format(name), '{:15}'.format(ssn), '{:15}'.format(age), '{:15}'.format(diag))
                                        patient_check=1
                if patient_check==0:
                        print("Patient not found")
                                
                        
                print(self.main_menu())
                
	
	
        def call_exit(self):
                with open(self.file_name, 'w') as file:
                        for i in self.patient_dict:
                                file.writelines(str(self.patient_dict[i]))

                print(" Program Done!\n Thank you! ")
                sys.exit()
		

print( "Welcome to UB patient managment system")
pm = PatientManagement()
