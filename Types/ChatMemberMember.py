from .utils import *
import Types

class ChatMemberMember(TelegramType):
    """
    Represents a chat member that has no additional privileges or restrictions.

    Args:
        status (str): The member's status in the chat, always “member”.

        user ("Types.User"): Information about the user.
    """   
    def __init__(
        self: TelegramType,
        status : str = None,
        user : "Types.User" = None,
    ):
        self.update(locals())
