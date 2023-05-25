from .utils import *
import typing
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup

class stopPoll:
    async def stop_poll(
        self,
        chat_id : typing.Union[int, str] = None,
        message_id : int = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).

            message_id (int): Identifier of the original message with the poll.

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for a new message inline keyboard..
        """

        return await Curl.request(
            url=self.api + "stopPoll",
            json={
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
            }
        )
