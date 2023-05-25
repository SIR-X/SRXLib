from .utils import *
import typing
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup

class stopMessageLiveLocation:
    async def stop_message_live_location(
        self,
        chat_id : typing.Union[int, str] = None,
        message_id : int = None,
        inline_message_id : str = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.

        Args:
            chat_id (int | str): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Required if inline_message_id is not specified. Identifier of the message with live location to stop.

            inline_message_id (str): Required if chat_id and message_id are not specified. Identifier of the inline message.

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for a new inline keyboard..
        """

        return await Curl.request(
            url=self.api + "stopMessageLiveLocation",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup,
            }
        )
