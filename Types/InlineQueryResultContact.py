from .utils import *
import Types

class InlineQueryResultContact(TelegramType):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    Args:
        type (str): Type of the result, must be contact.

        id (str): Unique identifier for this result, 1-64 Bytes.

        phone_number (str): Contact's phone number.

        first_name (str): Contact's first name.

        last_name (str): Optional. Contact's last name.

        vcard (str): Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes.

        reply_markup ("Types.InlineKeyboardMarkup"): Optional. Inline keyboard attached to the message.

        input_message_content ("Types.InputMessageContent"): Optional. Content of the message to be sent instead of the contact.

        thumbnail_url (str): Optional. Url of the thumbnail for the result.

        thumbnail_width (int): Optional. Thumbnail width.

        thumbnail_height (int): Optional. Thumbnail height.
    """   
    def __init__(
        self: TelegramType,
        type : str = None,
        id : str = None,
        phone_number : str = None,
        first_name : str = None,
        last_name : str = None,
        vcard : str = None,
        reply_markup : "Types.InlineKeyboardMarkup" = None,
        input_message_content : "Types.InputMessageContent" = None,
        thumbnail_url : str = None,
        thumbnail_width : int = None,
        thumbnail_height : int = None,
    ):
        self.update(locals())
