import re

with open("/Users/masonaviles/Apps/Codefellows/CodeFellows-401-Python/Labs/automation/data/potential_contacts.txt") as file:
  potentials = file.read()

# PHONE

phone = []
phone.extend(re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', potentials))

phone_no_duplicates = list(set(phone))
phone_ordered = phone_no_duplicates.sort()

phone_num_string = ''
for num in phone_no_duplicates:
  phone_num_string += num + ", "


with open("/Users/masonaviles/Apps/Codefellows/CodeFellows-401-Python/Labs/automation/data/phone_numbers.txt", 'w') as file:
  phone_nums = file.write(phone_num_string)

# EMAIL

email = []
email.extend(re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', potentials))

email_no_duplicates = list(set(email))
mail_ordered = email_no_duplicates.sort()

email_string = ''
for num in email_no_duplicates:
  email_string += num + ", "

print(email_string) 

with open("/Users/masonaviles/Apps/Codefellows/CodeFellows-401-Python/Labs/automation/data/emails.txt", 'w') as file:
  emails = file.write(email_string)