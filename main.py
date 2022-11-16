import smtplib
import os
from email.mime.text import MIMEText


def sendmail(message):
    sender = "youremail@gmail.com"
    # можно напрямую записать пароль в кавычках, можно взят из переменой окружения
    password = os.getenv("EMAIL_PASSWORD")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        # блок отправки сообщений от кого, кому(тут может быть цикл с сотней адресов), само сообщение
        msg = MIMEText(message)
        msg["Subject"] = "Любая тема хоть кирилицей хоть латиницей"
        server.sendmail(sender, sender, msg.as_string())

        return "message send!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password"


def main():
    message = input("Type your message!: ")
    sendmail(message=message)


if __name__ == "__main__":
    main()
