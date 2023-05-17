from .utils import *
import Types

class OrderInfo(TelegramType):
    """
    This object represents information about an order.

    Args:
        name (str): Optional. User name.

        phone_number (str): Optional. User's phone number.

        email (str): Optional. User email.

        shipping_address ("Types.ShippingAddress"): Optional. User shipping address.
    """   
    def __init__(
        self: TelegramType,
        name : str = None,
        phone_number : str = None,
        email : str = None,
        shipping_address : "Types.ShippingAddress" = None,
    ):
        self.update(locals())
