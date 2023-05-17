from .utils import *
import Types

class MessageId(TelegramType):
    """
    This object represents a unique message identifier.

    Args:
        message_id (int): Unique message identifier.
    """   
    def __init__(
        self: TelegramType,
        message_id : int = None,
    ):
        self.update(locals())
