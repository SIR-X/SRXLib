from .utils import *
import Types

class sendVideoNote(TelegramObject):
    """
    As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

    Args:
        chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

        message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

        video_note (InputFile | str): Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More information on Sending Files ». Sending video notes by a URL is currently unsupported.

        duration (int): Duration of sent video in seconds.

        length (int): Video width and height, i.e. diameter of the video message.

        thumbnail (InputFile | str): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files ».

        disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

        protect_content (bool): Protects the contents of the sent message from forwarding and saving.

        reply_to_message_id (int): If the message is a reply, ID of the original message.

        allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

        reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user..
    """   
    def __init__(
        self: TelegramObject,
        chat_id : int | str = None,
        message_thread_id : int = None,
        video_note : "Types.InputFile" | str = None,
        duration : int = None,
        length : int = None,
        thumbnail : "Types.InputFile" | str = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : "Types.InlineKeyboardMarkup" | "Types.ReplyKeyboardMarkup" | "Types.ReplyKeyboardRemove" | "Types.ForceReply" = None,
    ):
        self.update(locals())
