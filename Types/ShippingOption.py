from .utils import *
import Types, typing

class ShippingOption(TelegramObject):
    """
    This object represents one shipping option.

    Args:
        id (str): Shipping option identifier.

        title (str): Option title.

        prices (list[LabeledPrice]): List of price portions.
    """   
    def __init__(
        self: TelegramObject,
        id : str = None,
        title : str = None,
        prices : list["Types.LabeledPrice"] = None,
    ):
        self.update(locals())
