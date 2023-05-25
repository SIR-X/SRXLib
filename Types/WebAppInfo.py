from .utils import *
import Types, typing

class WebAppInfo(TelegramObject):
    """
    Describes a Web App.

    Args:
        url (str): An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps.
    """   
    def __init__(
        self: TelegramObject,
        url : str = None,
    ):
        self.update(locals())
