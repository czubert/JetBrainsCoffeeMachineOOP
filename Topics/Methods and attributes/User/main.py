class User:
    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    # create the method here
    def user_information(self):
        print(f"{self.name} {self.surname} is {self.age} years old and lives in {self.country}.")


u_name = input()
u_surname = input()
u_age = input()
u_country = input()


new_user = User(u_name, u_surname, u_age, u_country)
new_user.user_information()
