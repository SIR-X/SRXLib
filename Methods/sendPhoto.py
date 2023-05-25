from .utils import *
import typing
from Types.InputFile import InputFile
from Types.MessageEntity import MessageEntity
from Types.ForceReply import ForceReply
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove

class sendPhoto:
    async def send_photo(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
        photo : typing.Union[InputFile, str] = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list[MessageEntity] = None,
        has_spoiler : bool = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : typing.Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
    ):
        """
        Use this method to send photos. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            photo (InputFile | str): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More information on Sending Files ».

            caption (str): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing.

            parse_mode (str): Mode for parsing entities in the photo caption. See formatting options for more details..

            caption_entities (list[MessageEntity]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode.

            has_spoiler (bool): Pass True if the photo needs to be covered with a spoiler animation.

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=self.api + "sendPhoto",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "photo": photo,
                "caption": caption,
                "parse_mode": parse_mode,
                "caption_entities": caption_entities,
                "has_spoiler": has_spoiler,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
