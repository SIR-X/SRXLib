from .utils import *
import Types

class ChatMemberLeft(TelegramObject):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.

    Args:
        status (str): The member's status in the chat, always “left”.

        user (User): Information about the user.
    """   
    def __init__(
        self: TelegramObject,
        status : str = None,
        user : "Types.User" = None,
    ):
        self.update(locals())
