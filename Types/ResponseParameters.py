from .utils import *
import Types, typing

class ResponseParameters(TelegramObject):
    """
    Describes why a request was unsuccessful.

    Args:
        migrate_to_chat_id (int): Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier..

        retry_after (int): Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated.
    """   
    def __init__(
        self: TelegramObject,
        migrate_to_chat_id : int = None,
        retry_after : int = None,
    ):
        self.update(locals())
