import datetime as dt
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import random

now = dt.datetime.now()
week_of_day = now.weekday()
# print(type(week_of_day))
date_dic = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

if week_of_day == 5:
    with open("quotes.txt") as quotes:
        data = quotes.readlines()
        # print(data)
        # print(type(data))

    today_quote = random.choice(data)
    # print(today_quote)
    my_email = "your email"
    password = "QQ authorization code for SMTP service, not your email password" # QQ authorization code for SMTP service
    msg = MIMEText(today_quote, "plain", "utf-8")
    # header = Header("Ginger", "utf-8")
    msg['From'] = "{}<{}>".format("Ginger", my_email)
    msg["Subject"] = Header(f"Babe,it's {date_dic[week_of_day]}", 'utf-8')
    connection = smtplib.SMTP_SSL("smtp.qq.com")
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="an email address", msg=msg.as_string())
    connection.close()

# now = dt.datetime.now()
# # print(now)  2025-01-20 20:58:09.702806
#
# year = now.year
# # print(year) 2025
# month = now.month
# # print(month)
# day_of_week = now.weekday()  #indicate what day it is, like Monday, Tuesday etc
# print(day_of_week)
#
# # create an object of date_of_birthday using datetime module
# date_of_birth = dt.datetime(year=1999, month=4, day=17, hour=4)
# print(date_of_birth)


# # --------------------send email between qq email -------------------
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import formataddr
#
# '''
# # ////////////
# # https://gist.github.com/changkun/8ce6da2da380540b70126e37a68d0452
# 参考，尚未成功发送邮件
# '''
#
#
#
# my_email = ""
# password = "" # QQ authorization code for SMTP service
# #set up the email body, plain text
# msg = MIMEText(' Hello','plain','utf-8')
# #set up email sender: name<111111@qq.com> on the top of the page of qq email
# #https://blog.csdn.net/weixin_39504722/article/details/134816492?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-134816492-blog-132314400.235%5Ev43%5Epc_blog_bottom_relevance_base3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-134816492-blog-132314400.235%5Ev43%5Epc_blog_bottom_relevance_base3
# msg['From'] = formataddr((str(Header('Ginger', 'utf-8')), '111111111@qq.com'))
# #set up the subject of the email
#
# msg['Subject'] = Header('Happy_birthday','utf-8')
# #set up connection with the SMTP server of the sender's email, just google
#
# # with smtplib.SMTP_SSL("smtp.qq.com") as connection:
# #     connection.login(user=my_email, password=password)
# #     # send email
# #     connection.sendmail(my_email, "email", msg.as_string())
#
# connection = smtplib.SMTP_SSL("smtp.qq.com")
# # # connection.starttls()# for message security
# # #log in
# connection.login(user=my_email, password=password)
# # #send email
# connection.sendmail(my_email, "email", msg.as_string())
# connection.close()
#
# #