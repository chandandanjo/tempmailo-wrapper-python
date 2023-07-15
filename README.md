# About :
**tempmailo-wrapper-python** provides a convenient wrapper around the *tempmailo.com* service, allowing you to easily interact with temporary email functionality in your projects. With this library, you can create temporary email addresses, retrieve received messages, and perform various operations on them. It abstracts away the complexity of the underlying API and provides a simplified interface for seamless integration of temporary email functionality into your applications. Save time and effort by utilizing this wrapper to handle temporary email interactions in your projects.


## Usage :

   ```python
from tempmailo_wrapper import TempMail

temp_mail_instance = TempMail()

email_address = temp_mail_instance.get_email_address()
print("Temporary email address:", email_address)

messages = temp_mail_instance.get_messages()
print(messages)
  ```
