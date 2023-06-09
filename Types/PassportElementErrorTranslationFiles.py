from .utils import *
import Types, typing

class PassportElementErrorTranslationFiles(TelegramObject):
    """
    Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    Args:
        source (str): Error source, must be translation_files.

        type (str): Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.

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
