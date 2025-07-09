


class EmergencyContact:
    def __init__(self, contact_id, name, phone_number, relationship):
        self.contact_id = contact_id
        self.name = name
        self.phone_number = phone_number
        self.relationship = relationship

    def notify_emergency_contact(self, message=None):
        if not message:
            message = f"Emergency alert for {self.name} ({self.relationship})."
        print(f"Notifying {self.name} at {self.phone_number}: {message}")
    
    
def showEmergencyContactMenu(user):
    emergency_contacts = []
    while True:
        print("\nEmergency Contact Menu")
        print("1. Add Emergency Contact")
        print("2. View Emergency Contacts")
        print("3. Notify Emergency Contact")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "0":
            break

        elif choice == "1":
            name = input("Contact Name: ")
            phone_number = input("Phone Number: ")
            relationship = input("Relationship: ")
            contact = EmergencyContact(contact_id=len(emergency_contacts)+1, name=name, phone_number=phone_number, relationship=relationship)
            emergency_contacts.append(contact)
            print("Emergency contact added.")

        elif choice == "2":
            if emergency_contacts:
                for c in emergency_contacts:
                    print(f"{c.contact_id}: {c.name}, {c.phone_number}, {c.relationship}")
            else:
                print("No emergency contacts added.")

        elif choice == "3":
            if emergency_contacts:
                contact_id = int(input("Enter contact ID to notify: "))
                if 0 < contact_id <= len(emergency_contacts):
                    message = input("Enter message (optional): ")
                    emergency_contacts[contact_id-1].notify_emergency_contact(message)
                else:
                    print("Invalid contact ID.")
            else:
                print("No emergency contacts to notify.")

        else:
            print("Invalid option. Please try again.")
            