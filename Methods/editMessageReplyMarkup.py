from .utils import *
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup

class editMessageReplyMarkup:
    async def edit_message_reply_markup(
        self,
        chat_id : int | str = None,
        message_id : int = None,
        inline_message_id : str = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Args:
            chat_id (int | str): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Required if inline_message_id is not specified. Identifier of the message to edit.

            inline_message_id (str): Required if chat_id and message_id are not specified. Identifier of the inline message.

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for an inline keyboard..
        """

        return await Curl.request(
            url=self.api + "editMessageReplyMarkup",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup,
            }
        )
