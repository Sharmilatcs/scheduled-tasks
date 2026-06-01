# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################
import os
import pandas
import datetime as dt
import random
import smtplib

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day

for index, row in data.iterrows():
    if row["month"] == current_month and row["day"] == current_day:


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        number = random.randint(1,3)
        with open (f"letter_templates/letter_{number}.txt","r") as file:
            name = file.read()
            if "[NAME]" in name:
                new_name = name.replace("[NAME]", row["name"])

# 4. Send the letter generated in step 3 to that person's email address.
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()

                    connection.login(my_email, my_password)

                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs="mala.ram83@yahoo.com",
                        msg=f"Subject: Birthday day Wishes\n\n{new_name}"
                    )



