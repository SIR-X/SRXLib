from .utils import *
import Types, typing

class InlineQuery(TelegramObject):
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    Args:
        id (str): Unique identifier for this query.

        _from (User): Sender.

        query (str): Text of the query (up to 256 characters).

        offset (str): Offset of the results to be returned, can be controlled by the bot.

        chat_type (str): Optional. Type of the chat from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat.

        location (Location): Optional. Sender location, only for bots that request user location.
    """   
    def __init__(
        self: TelegramObject,
        id : str = None,
        _from : "Types.User" = None,
        query : str = None,
        offset : str = None,
        chat_type : str = None,
        location : "Types.Location" = None,
    ):
        self.update(locals())
