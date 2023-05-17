from .utils import *
import Types

class PassportElementErrorReverseSide(TelegramType):
    """
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    Args:
        source (str): Error source, must be reverse_side.

        type (str): The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”.

        file_hash (str): Base64-encoded hash of the file with the reverse side of the document.

        message (str): Error message.
    """   
    def __init__(
        self: TelegramType,
        source : str = None,
        type : str = None,
        file_hash : str = None,
        message : str = None,
    ):
        self.update(locals())
