contacts =[]

def add_contact():

    name = input("enter name:")
    phone= input("enter phone:")

    contact ={
        "name": name,
        "phone":phone
    }
    contacts.append(contact)

    print("contact saved")

def show_contacts():

    for contact in contacts:

        print("name:", contact["name"])
        print("phone:", contact["phone"])
        print("-------------")


while True:
        print("\n1.add contact")
        print("2.show contacts")
        print("3.exit")

        choice = input("Choose:")

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            print("goodbye")
            break
        else:
            print("invalide choice")


            