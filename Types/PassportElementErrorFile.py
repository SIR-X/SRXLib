from .utils import *
import Types, typing

class PassportElementErrorFile(TelegramObject):
    """
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    Args:
        source (str): Error source, must be file.

        type (str): The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.

        file_hash (str): Base64-encoded file hash.

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
