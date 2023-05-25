from .utils import *
import typing


class reopenGeneralForumTopic:
    async def reopen_general_forum_topic(
        self,
        chat_id : typing.Union[int, str] = None,
    ):
        """
        Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically unhidden if it was hidden. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
        """

        return await Curl.request(
            url=self.api + "reopenGeneralForumTopic",
            json={
                "chat_id": chat_id,
            }
        )
