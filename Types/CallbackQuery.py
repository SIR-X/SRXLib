from .utils import *
import Types

class CallbackQuery(TelegramType):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    Args:
        id (str): Unique identifier for this query.

        _from ("Types.User"): Sender.

        message ("Types.Message"): Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old.

        inline_message_id (str): Optional. Identifier of the message sent via the bot in inline mode, that originated the query..

        chat_instance (str): Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games..

        data (str): Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data..

        game_short_name (str): Optional. Short name of a Game to be returned, serves as the unique identifier for the game.
    """   
    def __init__(
        self: TelegramType,
        id : str = None,
        _from : "Types.User" = None,
        message : "Types.Message" = None,
        inline_message_id : str = None,
        chat_instance : str = None,
        data : str = None,
        game_short_name : str = None,
    ):
        self.update(locals())
