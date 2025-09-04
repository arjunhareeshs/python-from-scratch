class PhoneDirectory:
    def __init__(self):
        self.directory = {}
    def add_values(self, name, phonenumber):
        self.directory[name.lower()] = phonenumber
        print(f"User {name} added successfully.\n")
    def select(self, name):
        name_key = name.lower()
        if name_key in self.directory:
            print(f"User {name} found")
        else:
            print(f"No user found.\n")
    def delete(self, name):
        del self.directory[name.lower()]
        print(f"User {name} deleted.\n")
    def display(self,name):
        for nam, phonenumber in self.directory.items():
            print(f"{nam}: {phonenumber}")
        print()
def main():
    phonedirct = PhoneDirectory()

    while True:
        print("---------Operations---------\n")
        print("1. Add user")
        print("2. Select user")
        print("3. Delete user")
        print("4. Display directory")
        print("Enter 5 to Exit\n")

        ch = int(input("Enter the operation: "))
        
        if ch == 1:
            name = input("Enter name :")
            phonenumber = int(input("Enter number :"))
            phonedirct.add_values(name,phonenumber)
        elif ch == 2:
            name = input("Enter name :")
            phonedirct.select(name)    
        elif ch == 3:
            name = input("Enter name :")
            phonedirct.delete(name)
        elif ch == 4:
            name = input("Enter name :")
            phonedirct.display(name)
        elif ch == 5:
            print("----------THANK YOU---------")
            return
        else:
            print("Invalid input")
main()