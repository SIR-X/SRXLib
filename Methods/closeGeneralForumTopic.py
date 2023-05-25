from .utils import *
import typing


class closeGeneralForumTopic:
    async def close_general_forum_topic(
        self,
        chat_id : typing.Union[int, str] = None,
    ):
        """
        Use this method to close an open 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
        """

        return await Curl.request(
            url=self.api + "closeGeneralForumTopic",
            json={
                "chat_id": chat_id,
            }
        )
