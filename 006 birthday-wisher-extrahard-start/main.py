##################### Extra Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 1. Update the birthdays.csv
#yes
# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pandas.read_csv("./birthdays.csv")
# print(birthday_data)
# print(type(birthday_data))
birthday_data_dict = birthday_data.to_dict(orient="records")
print(birthday_data_dict)
print(type(birthday_data_dict))

now = datetime.datetime.now()
today_month = now.month
today_day = now.day
print(today_month)
print(today_day)
letter_content = ""
whose_birthday = ""
birthday_person = {}
for _ in birthday_data_dict:
    if _["month"] == today_month and _["day"] == today_day:
        birthday_person = _
        whose_birthday = _['name']
        print(f"today is {whose_birthday}'s birthday ")


        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        random_letter = random.choice(letter_list)
        print(random_letter)
        letter = open(f"./letter_templates/{random_letter}")
        # print(letter.read())
        # print(type(letter.read()))
        letter_content = letter.read()
        # print(letter_content)
        # print(whose_birthday)
        letter_content = letter_content.replace("[NAME]", whose_birthday)
        print(letter_content)
        # print(msg)
        # print(type(msg))
        # test_string = "a b c"
        # test_string = test_string.replace("a", "b")
        # print(test_string)
# 4. Send the letter generated in step 3 to that person's email address.
my_email = "@gmail.com"
password = ""

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(

            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter_content}"
        )
connection.close()

# email = ""
# password = "#"
#
# msg = MIMEText(letter_content, "plain", "utf-8")
# msg["From"] = "{}<{}>".format("Ginger", email)
# msg["Subject"] = Header(f"{whose_birthday}, HBD", "utf-8")
# connection = smtplib.SMTP_SSL("smtp.qq.com")
# connection.login(user=email, password=password)
# connection.sendmail(from_addr=email, to_addrs="", msg=msg.as_string())
#
# connection.close()



