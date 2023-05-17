from .utils import *
import Types

class MessageAutoDeleteTimerChanged(TelegramType):
    """
    This object represents a service message about a change in auto-delete timer settings.

    Args:
        message_auto_delete_time (int): New auto-delete time for messages in the chat; in seconds.
    """   
    def __init__(
        self: TelegramType,
        message_auto_delete_time : int = None,
    ):
        self.update(locals())
