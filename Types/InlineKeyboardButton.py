from .utils import *
import Types, typing

class InlineKeyboardButton(TelegramObject):
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    Args:
        text (str): Label text on the button.

        url (str): Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings..

        callback_data (str): Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes.

        web_app (WebAppInfo): Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot..

        login_url (LoginUrl): Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget..

        switch_inline_query (str): Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions - in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen..

        switch_inline_query_current_chat (str): Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options..

        switch_inline_query_chosen_chat (SwitchInlineQueryChosenChat): Optional. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field.

        callback_game (CallbackGame): Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row..

        pay (bool): Optional. Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages..
    """   
    def __init__(
        self: TelegramObject,
        text : str = None,
        url : str = None,
        callback_data : str = None,
        web_app : "Types.WebAppInfo" = None,
        login_url : "Types.LoginUrl" = None,
        switch_inline_query : str = None,
        switch_inline_query_current_chat : str = None,
        switch_inline_query_chosen_chat : "Types.SwitchInlineQueryChosenChat" = None,
        callback_game : "Types.CallbackGame" = None,
        pay : bool = None,
    ):
        self.update(locals())
