from .utils import *
import Types

class PassportElementErrorFrontSide(TelegramObject):
    """
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    Args:
        source (str): Error source, must be front_side.

        type (str): The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”.

        file_hash (str): Base64-encoded hash of the file with the front side of the document.

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
