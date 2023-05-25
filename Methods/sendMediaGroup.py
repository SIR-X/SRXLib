from .utils import *
import typing
from Types.InputMediaPhoto import InputMediaPhoto
from Types.InputMediaDocument import InputMediaDocument
from Types.InputMediaVideo import InputMediaVideo
from Types.InputMediaAudio import InputMediaAudio

class sendMediaGroup:
    async def send_media_group(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
        media : list[InputMediaAudio | InputMediaDocument | InputMediaPhoto| InputMediaVideo] = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
    ):
        """
        Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            media (list[InputMediaAudio | InputMediaDocument | InputMediaPhoto| InputMediaVideo]): A JSON-serialized array describing messages to be sent, must include 2-10 items.

            disable_notification (bool): Sends messages silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent messages from forwarding and saving.

            reply_to_message_id (int): If the messages are a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.
        """

        return await Curl.request(
            url=self.api + "sendMediaGroup",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "media": media,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
            }
        )
