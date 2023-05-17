from .utils import *
import Types

class MenuButtonWebApp(TelegramType):
    """
    Represents a menu button, which launches a Web App.

    Args:
        type (str): Type of the button, must be web_app.

        text (str): Text on the button.

        web_app ("Types.WebAppInfo"): Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery..
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        text : str = None,
        web_app : "Types.WebAppInfo" = None,
    ):
        self.update(locals())
