from form_mediator import FormMediator
from text_field import TextField
from label import Label
from button import Button

class MediatorApp:
   @staticmethod
   def main():
       mediator = FormMediator()

       username_field = TextField(mediator)
       password_field = TextField(mediator)
       login_button = Button(mediator)
       status_label = Label(mediator)

       mediator.set_username_field(username_field)
       mediator.set_password_field(password_field)
       mediator.set_login_button(login_button)
       mediator.set_status_label(status_label)

       # Simulate user interaction
       username_field.text = "admin"
       password_field.text = "1234"
       login_button.click()  # Should succeed

       print("\n--- New Attempt with Wrong Password ---")
       password_field.text = "wrong"
       login_button.click()  # Should fail

if __name__ == "__main__":
   MediatorApp.main()
