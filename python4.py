# # sending email in python 
# import smtplib # stands for simple mail transfer protocol library

# sender = "omaid0060@gmail.com"
# receiver = "gjan0393@gmail.com"
# # we will create this password through an app passowrds in our google account   
# password = "ctww yabd jmzd qdry"
# subject = "Python Email Test"
# body = "Hello! how are you, I am missing u badly!!!, I think u should visit us soon."

# #header
# message = f"""From: Muhammad Iqbal {sender}
# To: {receiver}
# Subject: {subject}\n
# {body}
# """

# #server creation for email
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()

# try:
#     #loging to our gmail account
#     server.login(sender,password)
#     print("Logged in...")

#     #sending email
#     server.sendmail(sender,receiver,message)
#     print("Email has been sent.")

# except smtplib.SMTPAuthenticationError:
#     print("unable to sign in")
# except Exception as e:
#     print(e)

# pip = package manager for packages and modules from Python Package Index 
# if python version is 3.4 or above then pip is already install

# help: pip 
# check: pip --version
# update: pip install --upgrade pip 
# installed packages: pip list  
# check outdated packages: pip list --outdated
# install a package: pip install "package name"

# executable python file 
# python -m PyInstaller --onefile --noconsole --icon=icon.ico  clock.py