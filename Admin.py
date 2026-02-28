from Doctor import Doctor

class Admin:
    """A class that deals with the Admin operations"""

    def __init__(self, username, password, address=''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        """Print a list of printable items"""
        for index, item in enumerate(a_list):
            print(f'{index + 1:3}|{item}')

    def login(self):
        """Handles login"""
        print("-----Login-----")
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        if username == self.__username and password == self.__password:
            print("Login successful!")
            return self.__username
        else:
            raise Exception("Invalid username or password.")

    def find_index(self, index, item_list):
        """Find the index of an item in a list"""
        return 0 <= index < len(item_list)

    def get_doctor_details(self):
        """Gets details needed to register a doctor"""
        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        speciality = input("Enter speciality: ")
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """Handles doctor registration, viewing, updating, and deleting"""
        print("-----Doctor Management-----")
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input('Input: ')

        if op == '1':
            print("-----Register-----")
            first_name, surname, speciality = self.get_doctor_details()
            for doctor in doctors:
                if doctor.get_first_name() == first_name and doctor.get_surname() == surname:
                    print('Name already exists.')
                    return
            doctors.append(Doctor(first_name, surname, speciality))
            print('Doctor registered.')

        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    if self.find_index(index, doctors):
                        break
                    else:
                        print("Doctor not found")
                except ValueError:
                    print('The ID entered is incorrect')

            doctor = doctors[index]
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = input('Input: ')
            if op == '1':
                doctor.set_first_name(input('Enter new first name: '))
            elif op == '2':
                doctor.set_surname(input('Enter new surname: '))
            elif op == '3':
                doctor.set_speciality(input('Enter new speciality: '))
            print('Doctor details updated.')

        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
                if self.find_index(doctor_index, doctors):
                    doctors.pop(doctor_index)
                    print('Doctor deleted.')
                else:
                    print('The ID entered is incorrect')
            except ValueError:
                print('Invalid input.')

        else:
            print('Invalid operation chosen.')

    def view_patient(self, patients):
        """Displays the list of patients with details."""
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor      | Age |    Mobile     | Postcode')
        for index, patient in enumerate(patients):
            print(f'{index + 1:3}|{patient.full_name():^30}|{patient.get_doctor():^18}|'
                  f'{patient._Patient__age:^5}|{patient._Patient__mobile:^15}|{patient._Patient__postcode:^10}')

    def assign_doctor_to_patient(self, patients, doctors):
        """Assign a doctor to a patient and handle symptoms"""
        print("-----Assign-----")
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if not self.find_index(patient_index, patients):
                print('The ID entered was not found.')
                return

            print("-----Doctors Select-----")
            print('Select the doctor that fits these symptoms:')
            patients[patient_index].print_symptoms()  # Ensure symptoms are printed
            print('ID |          Full Name           |  Speciality   ')
            self.view(doctors)

            doctor_index = int(input('Please enter the doctor ID: ')) - 1
            if self.find_index(doctor_index, doctors):
                patients[patient_index].assign_doctor(doctors[doctor_index].full_name())
                print('The patient is now assigned to the doctor.')
            else:
                print('The ID entered was not found.')

        except ValueError:
            print('Invalid input.')

    def discharge(self, patients, discharged_patients):
        """Discharge a patient"""
        print("-----Discharge Patient-----")
        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if self.find_index(patient_index, patients):
                discharged_patients.append(patients.pop(patient_index))
                print('Patient discharged.')
            else:
                print('The ID entered is incorrect.')
        except ValueError:
            print('Invalid input.')

    def view_discharge(self, discharged_patients):
        """View discharged patients"""
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def update_details(self):
        """Update admin details"""
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = input('Input: ')

        if op == '1':
            self.__username = input('Enter new username: ')
        elif op == '2':
            password = input('Enter the new password: ')
            if password == input('Enter the new password again: '):
                self.__password = password
            else:
                print('Passwords do not match.')
        elif op == '3':
            self.__address = input('Enter new address: ')
        else:
            print('Invalid option.')
            
            
    def generate_management_report(self, doctors, patients):
        """Generate and display a management report."""
        print("\n----- Management Report -----")
        print("-" * 30)
        
        # 1. Total number of doctors in the system
        total_doctors = len(doctors)
        print(f"Total number of doctors: {total_doctors}")
        
        # 2. Total number of patients per doctor
        print("\nTotal number of patients per doctor:")
        for doctor in doctors:
            doctor_patients = [patient for patient in patients if patient.get_doctor() == doctor.full_name()]
            print(f"{doctor.full_name()} - {len(doctor_patients)} patients")
        
        # 3. Total number of appointments per month per doctor
        print("\nTotal number of appointments per month per doctor (mock data):")
        for doctor in doctors:
            appointments_per_month = 5  # Assume 5 appointments per month for each doctor for demonstration
            print(f"{doctor.full_name()} - {appointments_per_month} appointments per month")
        
        # 4. Total number of patients based on illness type
        print("\nTotal number of patients based on illness type:")
        illness_count = {}
        
        for patient in patients:
            for illness in patient.symptoms:
                if illness in illness_count:
                    illness_count[illness] += 1
                else:
                    illness_count[illness] = 1

        for illness, count in illness_count.items():
            print(f"{illness}: {count} patients")