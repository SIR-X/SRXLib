from .utils import *
import Types

class ShippingAddress(TelegramType):
    """
    This object represents a shipping address.

    Args:
        country_code (str): Two-letter ISO 3166-1 alpha-2 country code.

        state (str): State, if applicable.

        city (str): City.

        street_line1 (str): First line for the address.

        street_line2 (str): Second line for the address.

        post_code (str): Address post code.
    """   
    def __init__(
        self: TelegramType,
        country_code : str = None,
        state : str = None,
        city : str = None,
        street_line1 : str = None,
        street_line2 : str = None,
        post_code : str = None,
    ):
        self.update(locals())
