from .utils import *
import Types, typing

class VideoChatParticipantsInvited(TelegramObject):
    """
    This object represents a service message about new members invited to a video chat.

    Args:
        users (list[User]): New members that were invited to the video chat.
    """   
    def __init__(
        self: TelegramObject,
        users : list["Types.User"] = None,
    ):
        self.update(locals())
