import requests
import pandas as pd
import time

def send_sms_content(content, mobile_no):
        if mobile_no.startswith("+8"):
            mobile_no = mobile_no.replace("+8", "8")
        elif mobile_no.startswith("0"):
            mobile_no = "88" + mobile_no

        headers = {'Content-Type': 'application/json'}

        try:
            if mobile_no[2:5] == "019":
                requests.get(f"http://esoftbd.org:8068/sreceive?client_id=GB AIMSUNIT&mobileno={mobile_no}&SMSText={content}", headers=headers)
            else:
                requests.get(f"http://esoftbd.org:8068/sreceive?client_id=GB-AIMSUNIT&mobileno={mobile_no}&SMSText={content}", headers=headers)
        except Exception as e:
            return False
        else:
            return True
        

FILE_PATH = "./contacts.xlsx"

SMS_CONTENT = '''
ইউনিট প্রতি সম্পদ মূল্য ৳১০.৫১
ক্রয় ৳১০.৫৬
বিক্রয় ৳১০.৪৬
০২ অক্টোবর ২০২৪
'''

def read_excel_content(file_path):
    contacts = pd.read_excel(file_path)
    
    for contact in contacts.values[1:]:
        user_contact = str(contact[0])
        if user_contact[0] != "0":
            user_contact = "0" + user_contact
        
        print(f"Sending message to {user_contact}")
        send_sms_content(SMS_CONTENT, user_contact)
        print("Message sent successfully.")
        time.sleep(0.5)


read_excel_content(FILE_PATH)