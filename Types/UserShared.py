from .utils import *
import Types

class UserShared(TelegramType):
    """
    This object contains information about the user whose identifier was shared with the bot using a KeyboardButtonRequestUser button.

    Args:
        request_id (int): Identifier of the request.

        user_id (int): Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means..
    """   
    def __init__(
        self: TelegramType,
        request_id : int = None,
        user_id : int = None,
    ):
        self.update(locals())
