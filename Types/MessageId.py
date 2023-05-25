from .utils import *
import Types

class MessageId(TelegramObject):
    """
    This object represents a unique message identifier.

    Args:
        message_id (int): Unique message identifier.
    """   
    def __init__(
        self: TelegramObject,
        message_id : int = None,
    ):
        self.update(locals())
