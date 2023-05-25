from .utils import *
import Types, typing

class ChatMemberMember(TelegramObject):
    """
    Represents a chat member that has no additional privileges or restrictions.

    Args:
        status (str): The member's status in the chat, always “member”.

        user (User): Information about the user.
    """   
    def __init__(
        self: TelegramObject,
        status : str = None,
        user : "Types.User" = None,
    ):
        self.update(locals())
