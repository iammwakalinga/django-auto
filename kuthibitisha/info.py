from email import message
from twilio.rest import Client
import random


class MessHandler:
    phone_number=None
    otp=None


    def __init__(self,phone_number,otp)->None:
        self.phone_number=phone_number
        self.otp=otp

    def send_otp_on_phone(self):
        account_sid="ACae70208803484377c50b1dc182e6bd09"
        auth_token="a1354d99448f31d4025d6911488e8ea2"
        client=Client(account_sid,auth_token)

        message=client.messages.create(
                body=f'Your OTP is{{self.otp}}',
                from_='+12183220275',
                to=self.phone_number()


        )
        print(message.sid)

    
