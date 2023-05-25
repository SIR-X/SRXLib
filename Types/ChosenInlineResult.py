from .utils import *
import Types

class ChosenInlineResult(TelegramObject):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    
    Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates.

    Args:
        result_id (str): The unique identifier for the result that was chosen.

        _from (User): The user that chose the result.

        location (Location): Optional. Sender location, only for bots that require user location.

        inline_message_id (str): Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message..

        query (str): The query that was used to obtain the result.
    """   
    def __init__(
        self: TelegramObject,
        result_id : str = None,
        _from : "Types.User" = None,
        location : "Types.Location" = None,
        inline_message_id : str = None,
        query : str = None,
    ):
        self.update(locals())
