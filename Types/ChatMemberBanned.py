from .utils import *
import Types, typing

class ChatMemberBanned(TelegramObject):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.

    Args:
        status (str): The member's status in the chat, always “kicked”.

        user (User): Information about the user.

        until_date (int): Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever.
    """   
    def __init__(
        self: TelegramObject,
        status : str = None,
        user : "Types.User" = None,
        until_date : int = None,
    ):
        self.update(locals())
