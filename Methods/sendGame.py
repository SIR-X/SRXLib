from .utils import *
from Types.InlineKeyboardMarkup import InlineKeyboardMarkup

class sendGame:
    async def send_game(
        self,
        chat_id : int = None,
        message_thread_id : int = None,
        game_short_name : str = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id : int = None,
        allow_sending_without_reply : bool = None,
        reply_markup : InlineKeyboardMarkup = None,
    ):
        """
        Use this method to send a game. On success, the sent Message is returned.

        Args:
            chat_id (int): Unique identifier for the target chat.

            message_thread_id (int): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

            game_short_name (str): Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather..

            disable_notification (bool): Sends the message silently. Users will receive a notification with no sound..

            protect_content (bool): Protects the contents of the sent message from forwarding and saving.

            reply_to_message_id (int): If the message is a reply, ID of the original message.

            allow_sending_without_reply (bool): Pass True if the message should be sent even if the specified replied-to message is not found.

            reply_markup (InlineKeyboardMarkup): A JSON-serialized object for an inline keyboard. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game..
        """

        return await Curl.request(
            url=self.api + "sendGame",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "game_short_name": game_short_name,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "reply_to_message_id": reply_to_message_id,
                "allow_sending_without_reply": allow_sending_without_reply,
                "reply_markup": reply_markup,
            }
        )
