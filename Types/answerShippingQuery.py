from .utils import *
import Types, typing

class answerShippingQuery(TelegramObject):
    """
    If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.

    Args:
        shipping_query_id (str): Unique identifier for the query to be answered.

        ok (bool): Pass True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible).

        shipping_options (list[ShippingOption]): Required if ok is True. A JSON-serialized array of available shipping options..

        error_message (str): Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user..
    """   
    def __init__(
        self: TelegramObject,
        shipping_query_id : str = None,
        ok : bool = None,
        shipping_options : list["Types.ShippingOption"] = None,
        error_message : str = None,
    ):
        self.update(locals())
