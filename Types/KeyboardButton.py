from .utils import *
import Types, typing

class KeyboardButton(TelegramObject):
    """
    This object represents one button of the reply keyboard. For simple text buttons, String can be used instead of this object to specify the button text. The optional fields web_app, request_user, request_chat, request_contact, request_location, and request_poll are mutually exclusive.
    
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.
    Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.
    Note: web_app option will only work in Telegram versions released after 16 April, 2022. Older clients will display unsupported message.
    Note: request_user and request_chat options will only work in Telegram versions released after 3 February, 2023. Older clients will display unsupported message.

    Args:
        text (str): Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed.

        request_user (KeyboardButtonRequestUser): Optional. If specified, pressing the button will open a list of suitable users. Tapping on any user will send their identifier to the bot in a “user_shared” service message. Available in private chats only..

        request_chat (KeyboardButtonRequestChat): Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a “chat_shared” service message. Available in private chats only..

        request_contact (bool): Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only..

        request_location (bool): Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only..

        request_poll (KeyboardButtonPollType): Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only..

        web_app (WebAppInfo): Optional. If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private chats only..
    """   
    def __init__(
        self: TelegramObject,
        text : str = None,
        request_user : "Types.KeyboardButtonRequestUser" = None,
        request_chat : "Types.KeyboardButtonRequestChat" = None,
        request_contact : bool = None,
        request_location : bool = None,
        request_poll : "Types.KeyboardButtonPollType" = None,
        web_app : "Types.WebAppInfo" = None,
    ):
        self.update(locals())
