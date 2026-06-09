class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_info = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_info)

        # Enregistrer l'appel dans l'historique des deux téléphones
        self.call_history.append(call_info)
        other_phone.call_history.append(call_info)

    def show_call_history(self):
        print(f"\nCall history for {self.phone_number}:")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }

        # Sauvegarder le message chez l'expéditeur et le destinataire
        self.messages.append(message)
        other_phone.messages.append(message)

        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")

    def show_outgoing_messages(self):
        print(f"\nOutgoing messages from {self.phone_number}:")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(message)

    def show_incoming_messages(self):
        print(f"\nIncoming messages for {self.phone_number}:")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(message)

    def show_messages_from(self, phone_number):
        print(f"\nMessages from {phone_number} to {self.phone_number}:")
        for message in self.messages:
            if message["from"] == phone_number:
                print(message)


# ======================
# TESTS
# ======================

phone1 = Phone("111-111")
phone2 = Phone("222-222")
phone3 = Phone("333-333")

# Appels
phone1.call(phone2)
phone2.call(phone3)

# Historique des appels
phone1.show_call_history()
phone2.show_call_history()
phone3.show_call_history()

# Messages
phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi there!")
phone3.send_message(phone1, "How are you?")
phone1.send_message(phone3, "I'm fine, thanks!")

# Messages sortants
phone1.show_outgoing_messages()

# Messages entrants
phone1.show_incoming_messages()

# Messages provenant d'un numéro spécifique
phone1.show_messages_from("222-222")
phone1.show_messages_from("333-333")