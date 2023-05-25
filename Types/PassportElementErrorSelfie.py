from .utils import *
import Types, typing

class PassportElementErrorSelfie(TelegramObject):
    """
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    Args:
        source (str): Error source, must be selfie.

        type (str): The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”.

        file_hash (str): Base64-encoded hash of the file with the selfie.

        message (str): Error message.
    """   
    def __init__(
        self: TelegramObject,
        source : str = None,
        type : str = None,
        file_hash : str = None,
        message : str = None,
    ):
        self.update(locals())
