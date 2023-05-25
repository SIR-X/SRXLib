from .utils import *
import Types

class PreCheckoutQuery(TelegramObject):
    """
    This object contains information about an incoming pre-checkout query.
    
    Telegram Passport is a unified authorization method for services that require personal identification. Users can upload their documents once, then instantly share their data with services that require real-world ID (finance, ICOs, etc.). Please see the manual for details.

    Args:
        id (str): Unique query identifier.

        _from (User): User who sent the query.

        currency (str): Three-letter ISO 4217 currency code.

        total_amount (int): Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies)..

        invoice_payload (str): Bot specified invoice payload.

        shipping_option_id (str): Optional. Identifier of the shipping option chosen by the user.

        order_info (OrderInfo): Optional. Order information provided by the user.
    """   
    def __init__(
        self: TelegramObject,
        id : str = None,
        _from : "Types.User" = None,
        currency : str = None,
        total_amount : int = None,
        invoice_payload : str = None,
        shipping_option_id : str = None,
        order_info : "Types.OrderInfo" = None,
    ):
        self.update(locals())
