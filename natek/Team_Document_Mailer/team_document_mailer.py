import win32com.client
from datetime import date
from configparser import ConfigParser
import os
import sys
import platform
import win32file




type=win32file.GetBinaryType("C:\\Users\\nathankeech\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\pythonwin\\pythonwin.exe")
if type==win32file.SCS_32BIT_BINARY:
    print("Pywin version: 32 bit")

print("Architecture: ", platform.architecture())

work_week = date.today().isocalendar()[1]
config_file_name = "team_document_mailer_config.txt"


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


try:
    config_dir = get_script_path()
    config_path = os.path.realpath(os.path.join(config_dir, config_file_name))
    print("Config path: ", config_path)

except Exception as e:
    print("Could not find config file.")
    print(e)

#   read config.ini file.
cparser = ConfigParser()
cparser.read(config_path)

# Retrieve configs
documents = cparser.get('General', 'documents').split(', ')
print("config file documents: ", documents)

address = cparser.get('General', 'address')
print("config file address: ", address)
# print("config file address type: ", type(address))

subject = cparser.get('General', 'subject')
print("config file subject: ", subject)

body = cparser.get('General', 'body')
print("config file body: ", body)

print("Work Week {}: {}".format(work_week, subject))

o = win32com.client.Dispatch("Outlook.Application")

Msg = o.CreateItem(0)
Msg.To = address

# Msg.CC = "more email addresses here"
# Msg.BCC = "more email addresses here"

Msg.Subject = "Work week {}: {}".format(work_week, subject)
Msg.Body = body

for document in documents:
    try:
        Msg.Attachments.Add(document)
    except Exception as e:
        print("Could not attach document: ", document)
        print(e)


Msg.Send()
print("Finish")