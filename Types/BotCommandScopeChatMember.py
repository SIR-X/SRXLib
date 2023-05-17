from .utils import *
import Types

class BotCommandScopeChatMember(TelegramType):
    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

    Args:
        type (str): Scope type, must be chat_member.

        chat_id ("Types.int | str"): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

        user_id (int): Unique identifier of the target user.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        chat_id : "Types.int | str" = None,
        user_id : int = None,
    ):
        self.update(locals())
