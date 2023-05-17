from .utils import *
import Types

class VideoChatParticipantsInvited(TelegramType):
    """
    This object represents a service message about new members invited to a video chat.

    Args:
        users (list["Types.User"]): New members that were invited to the video chat.
    """   
    def __init__(
        self: TelegramType,
        users : list["Types.User"] = None,
    ):
        self.update(locals())
