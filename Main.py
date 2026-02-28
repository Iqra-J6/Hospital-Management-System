# Admin.py
class Admin:
    def __init__(self, username, password, postcode):
        self.username = username
        self.password = password
        self.postcode = postcode

    def login(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        return username == self.username and password == self.password

    def assign_doctor_to_patient(self, patients, doctors):
        print('Available Doctors:')
        for idx, doctor in enumerate(doctors, 1):
            print(f'{idx}. {doctor.first_name} {doctor.surname} - {doctor.specialty}')
        
        patient_name = input('Enter patient full name to assign doctor: ')
        doctor_choice = int(input('Enter doctor number to assign: ')) - 1

        found_patient = next((p for p in patients if p.full_name().lower() == patient_name.lower()), None)
        
        if found_patient:
            found_patient.link(doctors[doctor_choice].full_name())
            print(f'Doctor {doctors[doctor_choice].full_name()} assigned to patient {found_patient.full_name()}')
        else:
            print('Patient not found.')

    def update_details(self):
        new_username = input('Enter new username: ')
        new_password = input('Enter new password: ')
        self.username = new_username
        self.password = new_password
        print('Admin details updated successfully.')

    def view_patient(self, patients):
        """Displays patient details grouped by surname."""
        from itertools import groupby
        patients.sort(key=lambda x: x.surname)  # Sort patients by surname
        
        print(f"{'Full Name':^30}|{'Doctor':^30}|{'Age':^5}|{'Mobile':^15}|{'Postcode':^10}|{'Symptoms':^30}|{'Address':^40}")
        print('-' * 155)
        
        for surname, group in groupby(patients, key=lambda x: x.surname):
            print(f"\n--- Family Group: {surname} ---")  # Display family grouping
            for patient in group:
                print(patient)

    def update_patient_details(self, patients):
        """Allows updating of patient details."""
        patient_name = input('Enter patient full name to update details: ')
        found_patient = next((p for p in patients if p.full_name().lower() == patient_name.lower()), None)
        
        if found_patient:
            found_patient.age = int(input(f'Enter new age (current: {found_patient.age}): '))
            found_patient.mobile = input(f'Enter new mobile number (current: {found_patient.mobile}): ')
            found_patient.address = input(f'Enter new address (current: {found_patient.address}): ')
            symptoms = input('Enter symptoms separated by commas: ')
            found_patient.symptoms = symptoms.split(', ') if symptoms else found_patient.symptoms
            print(f'Updated details for {found_patient.full_name()}')
        else:
            print('Patient not found.')
            
    def relocate_patient(self, patients, doctors):
        """Relocate a patient from one doctor to another."""
        patient_name = input('Enter patient full name to relocate: ')
        found_patient = next((p for p in patients if p.full_name().lower() == patient_name.lower()), None)
        
        if found_patient:
            print(f'Current doctor for {found_patient.full_name()}: {found_patient.get_doctor()}')
            print('Available Doctors:')
            for idx, doctor in enumerate(doctors, 1):
                print(f'{idx}. {doctor.first_name} {doctor.surname} - {doctor.specialty}')
            
            new_doctor_choice = int(input('Enter new doctor number to assign: ')) - 1
            
            if 0 <= new_doctor_choice < len(doctors):
                new_doctor = doctors[new_doctor_choice].full_name()
                found_patient.link(new_doctor)
                print(f'{found_patient.full_name()} has been relocated to Dr. {new_doctor}')
            else:
                print('Invalid doctor selection.')
        else:
            print('Patient not found.')

    def generate_management_report(self, doctors, patients):
        """Generate a management report"""
        print("\nManagement Report")
        print("-" * 50)
        
        # 1. Total number of doctors in the system
        total_doctors = len(doctors)
        print(f"Total number of doctors in the system: {total_doctors}")
        
        # 2. Total number of patients per doctor
        print("\nTotal number of patients per doctor:")
        for doctor in doctors:
            doctor_patients = [patient for patient in patients if patient.get_doctor() == doctor.full_name()]
            print(f"{doctor.full_name()} - {len(doctor_patients)} patients")
        
        # 3. Total number of appointments per month per doctor
        print("\nTotal number of appointments per month per doctor (mock data):")
        for doctor in doctors:
            # Assumption of 5 appointments per month for each doctor
            appointments_per_month = 5
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

# Doctor.py
class Doctor:
    def __init__(self, first_name, surname, specialty):
        self.first_name = first_name
        self.surname = surname
        self.specialty = specialty

    def full_name(self):
        return f'{self.first_name} {self.surname}'

# Patient.py
class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=None, address=None):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.postcode = postcode
        self.__doctor = 'None'
        self.symptoms = symptoms if symptoms is not None else []
        self.address = address

    def full_name(self):
        """Returns the full name of the patient"""
        return f'{self.first_name} {self.surname}'

    def get_doctor(self):
        """Returns the name of the doctor assigned to the patient"""
        return self.__doctor

    def link(self, doctor):
        """Links the patient to a doctor"""
        self.__doctor = doctor

    def __str__(self):
        return f'{self.full_name():^30}|{self.get_doctor():^30}|{self.age:^5}|{self.mobile:^15}|{self.postcode:^10}|{" | ".join(self.symptoms):^30}|{self.address:^40}'


# Main Program
def main():
    """
    The main function to be ran when the program runs
    """
    admin = Admin('admin', '123', 'B1 1AB')  # username is 'admin', password is '123'
    doctors = [Doctor('John', 'Smith', 'Internal Med.'), 
               Doctor('Jone', 'Smith', 'Pediatrics'), 
               Doctor('Jone', 'Carlos', 'Cardiology')]
    patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['Fever', 'Cough'], '123 Main St'),
                Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['Headache'], '456 Elm St'),
                Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['Cold', 'Sore Throat'], '789 Oak St'),
                Patient('Anna', 'Smith', 45, '07234567890', 'B2 DEF', ['Fatigue'], '123 Main St'),  
                Patient('Tom', 'Jones', 42, '07987654321', 'L3 GHJ', ['Chest Pain'], '457 Elm St')]
    discharged_patients = []

    while True:
        if admin.login():
            running = True  
            break
        else:
            print('Incorrect username or password.')

    while running:
        # Print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- View or update patient details')  
        print(' 7- Relocate patient to another doctor')
        print(' 8-Generate management report')
        print(' 9-Quit')

        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            print('Choose an operation for doctors:')
            print(' 1- Register a new doctor')
            print(' 2- View doctors')
            print(' 3- Update doctor details')
            print(' 4- Delete a doctor')

            doctor_op = input('Option: ')

            if doctor_op == '1':
                # Register new doctor
                first_name = input('Enter first name: ')
                last_name = input('Enter last name: ')
                specialty = input('Enter specialty: ')
                doctors.append(Doctor(first_name, last_name, specialty))
                print(f'Doctor {first_name} {last_name} registered.')

            elif doctor_op == '2':
                # View doctors
                for doctor in doctors:
                    print(f'{doctor.first_name} {doctor.surname} - {doctor.specialty}')

            elif doctor_op == '3':
                # Update doctor details
                first_name = input('Enter doctor first name to update: ')
                found = False
                for doctor in doctors:
                    if doctor.first_name == first_name:
                        found = True
                        doctor.surname = input(f'Enter new surname (current: {doctor.surname}): ')
                        doctor.specialty = input(f'Enter new specialty (current: {doctor.specialty}): ')
                        print(f'Doctor {doctor.first_name} updated.')
                if not found:
                    print('Doctor not found.')

            elif doctor_op == '4':
                # Delete doctor
                first_name = input('Enter doctor first name to delete: ')
                for doctor in doctors:
                    if doctor.first_name == first_name:
                        doctors.remove(doctor)
                        print(f'Doctor {doctor.first_name} deleted.')
                        break
                else:
                    print('Doctor not found.')

        elif op == '2':
            # 2- View or discharge patients
            print('List of patients:')
            for patient in patients:
                print(f'{patient.full_name()} - Age: {patient.age} - Mobile: {patient.mobile}')

            discharge_op = input('Do you want to discharge a patient(Y/N):').lower()

            if discharge_op in ['yes', 'y']:
                patient_name = input('Enter patient full name to discharge: ')
                found = False
                for patient in patients:
                    if patient.full_name().lower() == patient_name.lower():
                        found = True
                        patients.remove(patient)
                        discharged_patients.append(patient)
                        print(f'Patient {patient.full_name()} discharged.')
                        break
                if not found:
                    print('Patient not found.')

        elif op == '3':
            # 3 - view discharged patients
            print('List of discharged patients:')
            for patient in discharged_patients:
                print(f'{patient.full_name()} - Age: {patient.age} - Mobile: {patient.mobile}')

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin details
            admin.update_details()

        elif op == '6':
            # 6- View or update patient details
            print('Choose operation:')
            print(' 1- View patient details')
            print(' 2- Update patient details')
            
            patient_op = input('Option: ')
            
            if patient_op == '1':
                admin.view_patient(patients)
            elif patient_op == '2':
                admin.update_patient_details(patients)
            else:
                print('Invalid option.')
                
        elif op == '7':
            # 7-Relocate patient to another doctor
            admin.relocate_patient(patients, doctors)
            
            
        elif op == '8':
                # 8-Generate management report
                admin.generate_management_report(doctors, patients)
               
        
        elif op == '9':
            # 9-Quit and save data
            running = False
            print('exiting.....')
    


if __name__ == '__main__':
    main()

