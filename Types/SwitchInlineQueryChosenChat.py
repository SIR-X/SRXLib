from .utils import *
import Types

class SwitchInlineQueryChosenChat(TelegramType):
    """
    This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query.

    Args:
        query (str): Optional. The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted.

        allow_user_chats (bool): Optional. True, if private chats with users can be chosen.

        allow_bot_chats (bool): Optional. True, if private chats with bots can be chosen.

        allow_group_chats (bool): Optional. True, if group and supergroup chats can be chosen.

        allow_channel_chats (bool): Optional. True, if channel chats can be chosen.
    """   
    def __init__(
        self: TelegramType,
        query : str = None,
        allow_user_chats : bool = None,
        allow_bot_chats : bool = None,
        allow_group_chats : bool = None,
        allow_channel_chats : bool = None,
    ):
        self.update(locals())
