from .utils import *
import Types

class VideoChatEnded(TelegramType):
    """
    This object represents a service message about a video chat ended in the chat.

    Args:
        duration (int): Video chat duration in seconds.
    """   
    def __init__(
        self: TelegramType,
        duration : int = None,
    ):
        self.update(locals())
