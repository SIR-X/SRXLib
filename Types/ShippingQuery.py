from .utils import *
import Types

class ShippingQuery(TelegramType):
    """
    This object contains information about an incoming shipping query.

    Args:
        id (str): Unique query identifier.

        _from ("Types.User"): User who sent the query.

        invoice_payload (str): Bot specified invoice payload.

        shipping_address ("Types.ShippingAddress"): User specified shipping address.
    """   
    def __init__(
        self: TelegramType,
        id : str = None,
        _from : "Types.User" = None,
        invoice_payload : str = None,
        shipping_address : "Types.ShippingAddress" = None,
    ):
        self.update(locals())
