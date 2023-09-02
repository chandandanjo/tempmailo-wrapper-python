# TempMailo Python Wrapper

This is a Python wrapper for creating and managing temporary email addresses using the [TempMailo](https://tempmailo.com/) service. This library allows you to create temporary email addresses, retrieve messages sent to those addresses, and get the currently assigned email address.


## Usage

Here's how you can use the TempMail library in your Python code:

```python
from tempmailo import TempMail

# Create a TempMail object
temp_mail = TempMail()

# Get the currently assigned email address
email_address = temp_mail.get_email_address()
print(f"Temporary Email Address: {email_address}")

# Retrieve messages sent to the temporary email address
messages = temp_mail.get_messages()
for message in messages:
    print(f"Subject: {message['Subject']}")
    print(f"From: {message['From']}")
    print(f"Date: {message['Date']}")
    print(f"Message: {message['Message']}")
    print()

# Note: Make sure to handle exceptions and error messages appropriately in your code.
```

## Features

- Create temporary email addresses.
- Retrieve messages sent to the temporary email address.
- Get the currently assigned email address.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library
- JSON library

## Contributing

Contributions to this library are welcome. If you encounter any issues or have suggestions for improvements, please create an issue on the [GitHub repository](https://github.com/chandandanjo/tempmailo-wrapper-python/) or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
