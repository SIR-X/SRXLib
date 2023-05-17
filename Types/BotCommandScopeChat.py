from .utils import *
import Types

class BotCommandScopeChat(TelegramType):
    """
    Represents the scope of bot commands, covering a specific chat.

    Args:
        type (str): Scope type, must be chat.

        chat_id ("Types.int | str"): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        chat_id : "Types.int | str" = None,
    ):
        self.update(locals())
