from .utils import *
from Types.ReplyKeyboardRemove import ReplyKeyboardRemove
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.ReplyKeyboardMarkup import ReplyKeyboardMarkup
from Types.MessageEntity import MessageEntity
from Types.ForceReply import ForceReply
from Types.InputFile import InputFile

class sendVoice:
    async def send_voice(
        self,
        chat_id : int | str = None,
        message_thread_id : int = None,
        voice : InputFile | str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list[MessageEntity] = None,
        duration : int = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
    ):
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            voice (InputFile | str): Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files ».

            caption (str): Voice message caption, 0-1024 characters after entities parsing.

            parse_mode (str): Mode for parsing entities in the voice message caption. See formatting options for more details..

            caption_entities (list[MessageEntity]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode.

            duration (int): Duration of the voice message in seconds.

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
        """

        return await Curl.request(
            url=self.api + "sendVoice",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "voice": voice,
                "caption": caption,
                "parse_mode": parse_mode,
                "caption_entities": caption_entities,
                "duration": duration,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
