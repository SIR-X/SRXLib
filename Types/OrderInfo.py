from .utils import *
import Types

class OrderInfo(TelegramObject):
    """
    This object represents information about an order.

    Args:
        name (str): Optional. User name.

        phone_number (str): Optional. User's phone number.

        email (str): Optional. User email.

        shipping_address (ShippingAddress): Optional. User shipping address.
    """   
    def __init__(
        self: TelegramObject,
        name : str = None,
        phone_number : str = None,
        email : str = None,
        shipping_address : "Types.ShippingAddress" = None,
    ):
        self.update(locals())
