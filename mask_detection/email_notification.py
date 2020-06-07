from exchangelib import Credentials, Account
from exchangelib import Message, Mailbox, Attendee
try:
    # credentials = Credentials('kb_vaishnavi@optum.com', 'XXXXXXX')
    # account = Account('kb_vaishnavi@optum.com', credentials=credentials, autodiscover=True)
    credentials = Credentials('mrinalini_m@optum.com', 'XXXX')
    account = Account('mrinalini_m@optum.com', credentials=credentials, autodiscover=True)
except:
    pass

def send_email(email_id):
    try:
        print("Sending Email")
        m = Message(
            account=account,
            subject='Not complying Mask Protocol',
            body='This is an auto generated mail. Please do not reply\n\nYou have not follwed the mask protocol, you were found not wearing the mask.\nPlease ensure you wear the mask when entering the premises.',
            to_recipients=[Mailbox(email_address=email_id)]
        )
        m.send()
    except:
        pass
    return "Done"
