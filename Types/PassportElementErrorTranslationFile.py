from .utils import *
import Types

class PassportElementErrorTranslationFile(TelegramType):
    """
    Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    Args:
        source (str): Error source, must be translation_file.

        type (str): Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.

        file_hash (str): Base64-encoded file hash.

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
