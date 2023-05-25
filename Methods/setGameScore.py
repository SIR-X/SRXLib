from .utils import *


class setGameScore:
    async def set_game_score(
        self,
        user_id : int = None,
        score : int = None,
        force : bool = None,
        disable_edit_message : bool = None,
        chat_id : int = None,
        message_id : int = None,
        inline_message_id : str = None,
    ):
        """
        Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.

        Args:
            user_id (int): User identifier.

            score (int): New score, must be non-negative.

            force (bool): Pass True if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters.

            disable_edit_message (bool): Pass True if the game message should not be automatically edited to include the current scoreboard.

            chat_id (int): Required if inline_message_id is not specified. Unique identifier for the target chat.

            message_id (int): Required if inline_message_id is not specified. Identifier of the sent message.

            inline_message_id (str): Required if chat_id and message_id are not specified. Identifier of the inline message.
        """

        return await Curl.request(
            url=self.api + "setGameScore",
            json={
                "user_id": user_id,
                "score": score,
                "force": force,
                "disable_edit_message": disable_edit_message,
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
            }
        )
