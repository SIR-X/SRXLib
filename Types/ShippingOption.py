from .utils import *
import Types

class ShippingOption(TelegramType):
    """
    This object represents one shipping option.

    Args:
        id (str): Shipping option identifier.

        title (str): Option title.

        prices (list["Types.LabeledPrice"]): List of price portions.
    """   
    def __init__(
        self: TelegramType,
        id : str = None,
        title : str = None,
        prices : list["Types.LabeledPrice"] = None,
    ):
        self.update(locals())
