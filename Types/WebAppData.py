from .utils import *
import Types, typing

class WebAppData(TelegramObject):
    """
    Describes data sent from a Web App to the bot.

    Args:
        data (str): The data. Be aware that a bad client can send arbitrary data in this field..

        button_text (str): Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field..
    """   
    def __init__(
        self: TelegramObject,
        data : str = None,
        button_text : str = None,
    ):
        self.update(locals())
