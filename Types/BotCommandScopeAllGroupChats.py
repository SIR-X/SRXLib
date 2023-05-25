from .utils import *
import Types, typing

class BotCommandScopeAllGroupChats(TelegramObject):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.

    Args:
        type (str): Scope type, must be all_group_chats.
    """   
    def __init__(
        self: TelegramObject,
        type : str = None,
    ):
        self.update(locals())
