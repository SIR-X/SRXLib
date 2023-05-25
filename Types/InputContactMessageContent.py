from .utils import *
import Types, typing

class InputContactMessageContent(TelegramObject):
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    Args:
        phone_number (str): Contact's phone number.

        first_name (str): Contact's first name.

        last_name (str): Optional. Contact's last name.

        vcard (str): Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes.
    """   
    def __init__(
        self: TelegramObject,
        phone_number : str = None,
        first_name : str = None,
        last_name : str = None,
        vcard : str = None,
    ):
        self.update(locals())
