from .utils import *
import Types

class WriteAccessAllowed(TelegramType):
    """
    This object represents a service message about a user allowing a bot to write messages after adding the bot to the attachment menu or launching a Web App from a link.

    Args:
        web_app_name (str): Optional. Name of the Web App which was launched from a link.
    """   
    def __init__(
        self: TelegramType,
        web_app_name : str = None,
    ):
        self.update(locals())
