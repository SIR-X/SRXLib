from .utils import *
import Types

class WebAppInfo(TelegramType):
    """
    Describes a Web App.

    Args:
        url (str): An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps.
    """   
    def __init__(
        self: TelegramType,
        url : str = None,
    ):
        self.update(locals())
