import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('pyprojectvirtual@gmail.com', 'virtualmail')
    email = EmailMessage()
    email['From'] = 'pyprojectvirtual@gmail.com'#user email
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'vaishali': 'svaishu022@gmail.com',
    'valliammai': 'valliammai102000@gmail.com',
    'sharmila': 'sharmilaropheka@gmail.com',
    'kani': 'kanimozhianbuselvi@gmail.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}


def get_email_info():
    talk('Hi mam, To Whom you want to send email')

    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')

    subject = get_info()
    talk('Tell me the text in your email')

    message = get_info()
    send_email(receiver, subject, message)
    talk('Your email is sent')

    talk('Do you want to send more email?')

    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()