from .utils import *
import Types, typing

class PassportElementErrorFiles(TelegramObject):
    """
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    Args:
        source (str): Error source, must be files.

        type (str): The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.

        file_hashes (list[str]): List of base64-encoded file hashes.

        message (str): Error message.
    """   
    def __init__(
        self: TelegramObject,
        source : str = None,
        type : str = None,
        file_hashes : list[str] = None,
        message : str = None,
    ):
        self.update(locals())
