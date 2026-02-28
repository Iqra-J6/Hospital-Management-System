class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=None):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): Mobile number
            postcode (string): Postcode
            symptoms (list, optional): List of symptoms. Defaults to empty list.
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = symptoms if symptoms else []  # List of symptoms, defaults to empty list if None

    def full_name(self):
        """Full name is first_name and surname."""
        return f"{self.__first_name} {self.__surname}"

    def get_doctor(self):
        """Returns the name of the linked doctor."""
        return self.__doctor

    def link(self, doctor):
        """Link the patient to a doctor.

        Args:
            doctor (string): The doctor's full name.
        """
        self.__doctor = doctor

    def print_symptoms(self):
        """Prints all the symptoms of the patient."""
        if not self.__symptoms:
            print("No symptoms recorded.")
        else:
            print("Symptoms: " + ", ".join(self.__symptoms))

    def get_symptoms(self):
        """Returns the list of symptoms of the patient."""
        return self.__symptoms

    def add_symptom(self, symptom):
        """Add a symptom to the patient's list."""
        self.__symptoms.append(symptom)

    def get_surname(self):
        """Returns the surname of the patient, used to group by family."""
        return self.__surname

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
