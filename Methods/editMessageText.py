from .utils import *
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup
from Types.MessageEntity import MessageEntity

class editMessageText:
    async def edit_message_text(
        self,
        chat_id : int | str = None,
        message_id : int = None,
        inline_message_id : str = None,
        text : str = None,
        parse_mode : str = None,
        entities : list[MessageEntity] = None,
        disable_web_page_preview : bool = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Args:
            chat_id (int | str): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Required if inline_message_id is not specified. Identifier of the message to edit.

            inline_message_id (str): Required if chat_id and message_id are not specified. Identifier of the inline message.

            text (str): New text of the message, 1-4096 characters after entities parsing.

            parse_mode (str): Mode for parsing entities in the message text. See formatting options for more details..

            entities (list[MessageEntity]): A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode.

            disable_web_page_preview (bool): Disables link previews for links in this message.

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for an inline keyboard..
        """

        return await Curl.request(
            url=self.api + "editMessageText",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
                "text": text,
                "parse_mode": parse_mode,
                "entities": entities,
                "disable_web_page_preview": disable_web_page_preview,
                "reply_markup": reply_markup,
            }
        )
