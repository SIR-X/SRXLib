from .utils import *
import Types, typing

class EncryptedCredentials(TelegramObject):
    """
    Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.

    Args:
        data (str): Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication.

        hash (str): Base64-encoded data hash for data authentication.

        secret (str): Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption.
    """   
    def __init__(
        self: TelegramObject,
        data : str = None,
        hash : str = None,
        secret : str = None,
    ):
        self.update(locals())
