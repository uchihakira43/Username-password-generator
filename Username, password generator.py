import time
import smtplib

#PRACTICE
def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = ''
  for x in range(0, len(user_name)):
    password += user_name[x-1]
  return password


var_one = username_generator('FIRST NAME', 'LAST NAME')
#print(var_one)
var_two = password_generator(var_one)
#print(var_two)


#PROGRAM STARTS HERE
print('Welcome to username and password generator!')
time.sleep(2)

#USERNAME GENERATOR
print('Time to generate your username!')
time.sleep(2)

var_3 = input('Please type your first name: ')
#print(var_3)
time.sleep(3)
if var_3 == '':
  print('We need a first name.')

var_4 = input('Please type your last name: ')
#print(var_4)

if var_4 == '':
  print('We need a last name.')

print('Generating your username! One moment please...')
time.sleep(2)

new_username = username_generator(var_3, var_4)
print('Your username is:', new_username)
time.sleep(3)

#PASSWORD GENERATOR
print('Time to generate your password!')
time.sleep(2)
print('One moment please...')
time.sleep(2)

new_password = password_generator(new_username)
print('Your password is', new_password)
time.sleep(2)
print('Thank you for using our generator!')
time.sleep(2)

print('Would you like your information to be emailed to you?')
var_5 = input('Type yes or no: ')
if var_5 == 'yes':
  print('Great! Please type in your gmail!')
  var_6 = input('Gmail: ')
  print('One moment please...')
else:
  print('Goodbye! This program will now close.')
  time.sleep(3)
  quit()

#GMAIL
gmail_user_to = var_6
gmail_user = 'THE FROM GMAIL GOES HERE'
gmail_app_password = 'FROM GMAIL PASSWORD GOES HERE'

sent_from = gmail_user
sent_to = [sent_from, gmail_user_to]
sent_subject = " Hello ! Here is your username and password! >>"
sent_body = "Your username is: {}\n\nYour password is: {}".format(new_username, new_password)


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email has been sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)

time.sleep(2)
print('This program will now close. Goodbye!')
time.sleep(3)
quit()