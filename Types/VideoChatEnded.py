from .utils import *
import Types, typing

class VideoChatEnded(TelegramObject):
    """
    This object represents a service message about a video chat ended in the chat.

    Args:
        duration (int): Video chat duration in seconds.
    """   
    def __init__(
        self: TelegramObject,
        duration : int = None,
    ):
        self.update(locals())
