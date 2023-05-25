from .utils import *
import Types

class EncryptedPassportElement(TelegramObject):
    """
    Describes documents or other Telegram Passport elements shared with the bot by the user.

    Args:
        type (str): Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”..

        data (str): Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials..

        phone_number (str): Optional. User's verified phone number, available only for “phone_number” type.

        email (str): Optional. User's verified email address, available only for “email” type.

        files (list[PassportFile]): Optional. Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials..

        front_side (PassportFile): Optional. Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials..

        reverse_side (PassportFile): Optional. Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials..

        selfie (PassportFile): Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials..

        translation (list[PassportFile]): Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials..

        hash (str): Base64-encoded element hash for using in PassportElementErrorUnspecified.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
        data : str = None,
        phone_number : str = None,
        email : str = None,
        files : list["Types.PassportFile"] = None,
        front_side : "Types.PassportFile" = None,
        reverse_side : "Types.PassportFile" = None,
        selfie : "Types.PassportFile" = None,
        translation : list["Types.PassportFile"] = None,
        hash : str = None,
    ):
        self.update(locals())
