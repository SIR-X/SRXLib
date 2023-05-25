from .utils import *
import typing
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.LabeledPrice import LabeledPrice

class sendInvoice:
    async def send_invoice(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
        title : str = None,
        description : str = None,
        payload : str = None,
        provider_token : str = None,
        currency : str = None,
        prices : list[LabeledPrice] = None,
        max_tip_amount : int = None,
        suggested_tip_amounts : list[int] = None,
        start_parameter : str = None,
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
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to send invoices. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            title (str): Product name, 1-32 characters.

            description (str): Product description, 1-255 characters.

            payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes..

            provider_token (str): Payment provider token, obtained via @BotFather.

            currency (str): Three-letter ISO 4217 currency code, see more on currencies.

            prices (list[LabeledPrice]): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.).

            max_tip_amount (int): The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0.

            suggested_tip_amounts (list[int]): A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount..

            start_parameter (str): Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter.

            provider_data (str): JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider..

            photo_url (str): URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for..

            photo_size (int): Photo size in bytes.

            photo_width (int): Photo width.

            photo_height (int): Photo height.

            need_name (bool): Pass True if you require the user's full name to complete the order.

            need_phone_number (bool): Pass True if you require the user's phone number to complete the order.

            need_email (bool): Pass True if you require the user's email address to complete the order.

            need_shipping_address (bool): Pass True if you require the user's shipping address to complete the order.

            send_phone_number_to_provider (bool): Pass True if the user's phone number should be sent to provider.

            send_email_to_provider (bool): Pass True if the user's email address should be sent to provider.

            is_flexible (bool): Pass True if the final price depends on the shipping method.

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button..
        """

        return await Curl.request(
            url=self.api + "sendInvoice",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "title": title,
                "description": description,
                "payload": payload,
                "provider_token": provider_token,
                "currency": currency,
                "prices": prices,
                "max_tip_amount": max_tip_amount,
                "suggested_tip_amounts": suggested_tip_amounts,
                "start_parameter": start_parameter,
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
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
