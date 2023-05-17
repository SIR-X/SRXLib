from .utils import *
import Types

class Contact(TelegramType):
    """
    This object represents a phone contact.

    Args:
        phone_number (str): Contact's phone number.

        first_name (str): Contact's first name.

        last_name (str): Optional. Contact's last name.

        user_id (int): Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier..

        vcard (str): Optional. Additional data about the contact in the form of a vCard.
    """   
    def __init__(
        self: TelegramType,
        phone_number : str = None,
        first_name : str = None,
        last_name : str = None,
        user_id : int = None,
        vcard : str = None,
    ):
        self.update(locals())
