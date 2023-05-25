from .utils import *
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.MessageEntity import MessageEntity

class editMessageCaption:
    async def edit_message_caption(
        self,
        chat_id : int | str = None,
        message_id : int = None,
        inline_message_id : str = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities : list[MessageEntity] = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Args:
            chat_id (int | str): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Required if inline_message_id is not specified. Identifier of the message to edit.

            inline_message_id (str): Required if chat_id and message_id are not specified. Identifier of the inline message.

            caption (str): New caption of the message, 0-1024 characters after entities parsing.

            parse_mode (str): Mode for parsing entities in the message caption. See formatting options for more details..

            caption_entities (list[MessageEntity]): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode.

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for an inline keyboard..
        """

        return await Curl.request(
            url=self.api + "editMessageCaption",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
                "caption": caption,
                "parse_mode": parse_mode,
                "caption_entities": caption_entities,
                "reply_markup": reply_markup,
            }
        )
