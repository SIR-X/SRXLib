from .utils import *
import Types

class VideoChatScheduled(TelegramType):
    """
    This object represents a service message about a video chat scheduled in the chat.

    Args:
        start_date (int): Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator.
    """   
    def __init__(
        self: TelegramType,
        start_date : int = None,
    ):
        self.update(locals())
