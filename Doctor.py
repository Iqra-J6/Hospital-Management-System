class Doctor:
    """A class that deals with Doctor operations."""

    def __init__(self, first_name, surname, speciality):
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []  # List of patients assigned to the doctor
        self.__appointments = []  # List of appointments

    def full_name(self):
        """Returns the full name of the doctor."""
        return f"{self.__first_name} {self.__surname}"

    def add_patient(self, patient):
        """Adds a patient to the doctor's list of patients."""
        self.__patients.append(patient)

    def add_appointment(self, appointment):
        """Adds an appointment to the doctor's schedule."""
        self.__appointments.append(appointment)

    def view_patients(self):
        """Displays details of patients assigned to the doctor."""
        if not self.__patients:
            print("No patients assigned.")
        else:
            print("-----Patients Assigned-----")
            print("ID |          Full Name           | Age |    Mobile     | Postcode")
            for index, patient in enumerate(self.__patients):
                print(f"{index+1:2} | {patient}")  

    def view_appointments(self):
        """Displays the list of appointments for the doctor."""
        if not self.__appointments:
            print("No appointments scheduled.")
        else:
            print("-----Appointments Scheduled-----")
            for index, appointment in enumerate(self.__appointments):
                print(f"Appointment {index + 1}: {appointment}")

    def generate_management_report(self, patients):
        """Generate and display a management report for the doctor."""
        print("\n----- Management Report -----")
        print("-" * 30)

        # 1. Doctor's total number of patients
        total_patients = len(self.__patients)
        print(f"Total number of patients: {total_patients}")

        # 2. Doctor's total number of appointments
        total_appointments = len(self.__appointments)
        print(f"Total number of appointments: {total_appointments}")

        # 3. Total number of patients based on illness type 
        print("\nTotal number of patients based on illness type:")
        illness_count = {}

        for patient in self.__patients:
            for illness in patient.get_symptoms():  
                if illness in illness_count:
                    illness_count[illness] += 1
                else:
                    illness_count[illness] = 1

        for illness, count in illness_count.items():
            print(f"{illness}: {count} patients")

    def __str__(self):
        """Returns a string representation of the doctor."""
        return f"{self.full_name():^30}|{self.__speciality:^15}"
