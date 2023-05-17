from .utils import *
import Types

class PassportData(TelegramType):
    """
    Describes Telegram Passport data shared with the bot by the user.

    Args:
        data (list["Types.EncryptedPassportElement"]): Array with information about documents and other Telegram Passport elements that was shared with the bot.

        credentials ("Types.EncryptedCredentials"): Encrypted credentials required to decrypt the data.
    """   
    def __init__(
        self: TelegramType,
        data : list["Types.EncryptedPassportElement"] = None,
        credentials : "Types.EncryptedCredentials" = None,
    ):
        self.update(locals())
