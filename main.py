# Author: Mason Hernandez
# Date: 10/28/2022
# Website: www.codewithmason.com

"""Description: Use Sheety API to retrieve users info, Use NewsApi to retrieve top headlines,
Send news to users by SMTP email protocol """

from get_data import DataFile
from news_feed import NewsFeed
from auto_email import EmailOut

file = DataFile()  # Creates a data file class with empty dictionary
data_dictionary = file.get_data()  # retrieves ALL data from Excel sheet and appends to empty dictionary


def news_email():
    first_name = each["name"]
    last_name = each["last"]
    email = each["email"]
    interest = each["interest"]
    feed = NewsFeed(interest)  # call Newsfeed() class pass news interest from user API
    my_data_list = feed.get()  # get top-headline news

    new_body = f"Hello {first_name} {last_name}," \
               f"\n\tCheck out the top Headlines from {interest}!\n\n{my_data_list}\n\n" \
               f"Have a Lovely Day,\n{first_name} {last_name}"
    email_out = EmailOut(sender_email="lbcbeef@gmail.com",  # Send email to each person on xlsx file
                         receiver_email=email,
                         subject=f"Latest news about {interest}",
                         body=new_body)
    email_out.send_me()

    print(f"Email send to {first_name} {last_name}")


for each in data_dictionary:  # for each column in peoples.xlsx file (retrieve name, email, interest)
    news_email()
