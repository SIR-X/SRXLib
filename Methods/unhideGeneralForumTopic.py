from .utils import *


class unhideGeneralForumTopic:
    async def unhide_general_forum_topic(
        self,
        chat_id : int | str = None,
    ):
        """
        Use this method to unhide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
        """

        return await Curl.request(
            url=self.api + "unhideGeneralForumTopic",
            json={
                "chat_id": chat_id,
            }
        )
