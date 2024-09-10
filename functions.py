import re

# Function to remove special characters from names
def sanitize_name(name):
    # Remove non-alphanumeric characters (except spaces)
    return re.sub(r'[^A-Za-z0-9 ]+', '', name)

# Function to generate email address
def generate_email(name, existing_emails):
    # Sanitize the name by removing special characters
    name = sanitize_name(name)
    parts = name.split()

    # Generate email based on the available names
    if len(parts) == 1:
        email_prefix = parts[0].lower()
    elif len(parts) >= 2:
        email_prefix = parts[0][0].lower() + parts[-1].lower()

    # Ensure uniqueness of the email address
    email = f"{email_prefix}@gmail.com"
    counter = 1
    while email in existing_emails:
        email = f"{email_prefix}{counter}@gmail.com"
        counter += 1

    # Add the email to the existing emails set
    existing_emails.add(email)
    return email
