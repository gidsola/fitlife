


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
        
        