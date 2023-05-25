from .utils import *
import Types

class PassportElementErrorDataField(TelegramObject):
    """
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    Args:
        source (str): Error source, must be data.

        type (str): The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”.

        field_name (str): Name of the data field which has the error.

        data_hash (str): Base64-encoded data hash.

        message (str): Error message.
    """   
    def __init__(
        self: TelegramObject,
        source : str = None,
        type : str = None,
        field_name : str = None,
        data_hash : str = None,
        message : str = None,
    ):
        self.update(locals())
