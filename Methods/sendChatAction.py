from .utils import *


class sendChatAction:
    async def send_chat_action(
        self,
        chat_id : int | str = None,
        message_thread_id : int = None,
        action : str = None,
    ):
        """
        Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.
        
        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_thread_id (int): Unique identifier for the target message thread; supergroups only.

            action (str): Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes..
        """

        return await Curl.request(
            url=api + "sendChatAction",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "action": action,
            }
        )
