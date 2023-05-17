from .utils import *
from Types.ForceReply import ForceReply
from Types.MessageEntity import MessageEntity
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.InputFile import InputFile
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup

class sendAnimation:
    async def send_animation(
        self,
        chat_id : int | str = None,
        message_thread_id : int = None,
        animation : InputFile | str = None,
        duration : int = None,
        width : int = None,
        height : int = None,
        thumbnail : InputFile | str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list[MessageEntity] = None,
        has_spoiler : bool = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
    ):
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            animation (InputFile | str): Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More information on Sending Files ».

            duration (int): Duration of sent animation in seconds.

            width (int): Animation width.

            height (int): Animation height.

            thumbnail (InputFile | str): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files ».

            caption (str): Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing.

            parse_mode (str): Mode for parsing entities in the animation caption. See formatting options for more details..

            caption_entities (list[MessageEntity]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode.

            has_spoiler (bool): Pass True if the animation needs to be covered with a spoiler animation.

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=api + "sendAnimation",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "animation": animation,
                "duration": duration,
                "width": width,
                "height": height,
                "thumbnail": thumbnail,
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
