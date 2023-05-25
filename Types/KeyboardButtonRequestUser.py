from .utils import *
import Types

class KeyboardButtonRequestUser(TelegramObject):
    """
    This object defines the criteria used to request a suitable user. The identifier of the selected user will be shared with the bot when the corresponding button is pressed. More about requesting users »

    Args:
        request_id (int): Signed 32-bit identifier of the request, which will be received back in the UserShared object. Must be unique within the message.

        user_is_bot (bool): Optional. Pass True to request a bot, pass False to request a regular user. If not specified, no additional restrictions are applied..

        user_is_premium (bool): Optional. Pass True to request a premium user, pass False to request a non-premium user. If not specified, no additional restrictions are applied..
    """   
    def __init__(
        self: TelegramObject,
        request_id : int = None,
        user_is_bot : bool = None,
        user_is_premium : bool = None,
    ):
        self.update(locals())
