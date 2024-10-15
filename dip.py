from abc import ABC, abstractmethod

# High-level module
class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier  # Depends on abstraction, not concrete classes

    def send_notification(self, message):
        self.notifier.send(message)

# Abstraction
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Low-level module
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Sending email notification: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Sending SMS notification: {message}")

# Main program block
email_service = NotificationService(EmailNotifier())
email_service.send_notification("Hello via Email!")

sms_service = NotificationService(SMSNotifier())
sms_service.send_notification("Hello via SMS!")
