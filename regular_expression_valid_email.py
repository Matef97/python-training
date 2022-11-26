import re
mail_request = input("Enter your email : ")
check_mail = re.findall(r"[A-z0-9\.]+@[A-z]+\.com|net",mail_request)
mails =[]
for i in check_mail :
  if check_mail :
    mails.append(check_mail)
  mail_request = input("Enter your email : ")
  check_mail = re.findall(r"[A-z0-9\.]+@[A-z]+\.com|net",mail_request)
  if mail_request == "0" :
      break  

print(mails)    

