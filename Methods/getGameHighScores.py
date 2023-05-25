from .utils import *


class getGameHighScores:
    async def get_game_high_scores(
        self,
        user_id : int = None,
        chat_id : int = None,
        message_id : int = None,
        inline_message_id : str = None,
    ):
        """
        Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of GameHighScore objects.

        Args:
            user_id (int): Target user id.

            chat_id (int): Required if inline_message_id is not specified. Unique identifier for the target chat.

            message_id (int): Required if inline_message_id is not specified. Identifier of the sent message.

            inline_message_id (str): Required if chat_id and message_id are not specified. Identifier of the inline message.
        """

        return await Curl.request(
            url=self.api + "getGameHighScores",
            json={
                "user_id": user_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
            }
        )
