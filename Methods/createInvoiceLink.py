from .utils import *
import typing
from Types.LabeledPrice import LabeledPrice

class createInvoiceLink:
    async def create_invoice_link(
        self,
        title : str = None,
        description : str = None,
        payload : str = None,
        provider_token : str = None,
        currency : str = None,
        prices : list[LabeledPrice] = None,
        max_tip_amount : int = None,
        suggested_tip_amounts : list[int] = None,
        provider_data : str = None,
        photo_url : str = None,
        photo_size : int = None,
        photo_width : int = None,
        photo_height : int = None,
        need_name : bool = None,
        need_phone_number : bool = None,
        need_email : bool = None,
        need_shipping_address : bool = None,
        send_phone_number_to_provider : bool = None,
        send_email_to_provider : bool = None,
        is_flexible : bool = None,
    ):
        """
        Use this method to create a link for an invoice. Returns the created invoice link as String on success.

        Args:
            title (str): Product name, 1-32 characters.

            description (str): Product description, 1-255 characters.

            payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes..

            provider_token (str): Payment provider token, obtained via BotFather.

            currency (str): Three-letter ISO 4217 currency code, see more on currencies.

            prices (list[LabeledPrice]): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.).

            max_tip_amount (int): The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0.

            suggested_tip_amounts (list[int]): A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount..

            provider_data (str): JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider..

            photo_url (str): URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service..

            photo_size (int): Photo size in bytes.

            photo_width (int): Photo width.

            photo_height (int): Photo height.

            need_name (bool): Pass True if you require the user's full name to complete the order.

            need_phone_number (bool): Pass True if you require the user's phone number to complete the order.

            need_email (bool): Pass True if you require the user's email address to complete the order.

            need_shipping_address (bool): Pass True if you require the user's shipping address to complete the order.

            send_phone_number_to_provider (bool): Pass True if the user's phone number should be sent to the provider.

            send_email_to_provider (bool): Pass True if the user's email address should be sent to the provider.

            is_flexible (bool): Pass True if the final price depends on the shipping method.
        """

        return await Curl.request(
            url=self.api + "createInvoiceLink",
            json={
                "title": title,
                "description": description,
                "payload": payload,
                "provider_token": provider_token,
                "currency": currency,
                "prices": prices,
                "max_tip_amount": max_tip_amount,
                "suggested_tip_amounts": suggested_tip_amounts,
                "provider_data": provider_data,
                "photo_url": photo_url,
                "photo_size": photo_size,
                "photo_width": photo_width,
                "photo_height": photo_height,
                "need_name": need_name,
                "need_phone_number": need_phone_number,
                "need_email": need_email,
                "need_shipping_address": need_shipping_address,
                "send_phone_number_to_provider": send_phone_number_to_provider,
                "send_email_to_provider": send_email_to_provider,
                "is_flexible": is_flexible,
            }
        )
