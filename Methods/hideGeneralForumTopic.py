from .utils import *


class hideGeneralForumTopic:
    async def hide_general_forum_topic(
        self,
        chat_id : int | str = None,
    ):
        """
        Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically closed if it was open. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
        """

        return await Curl.request(
            url=api + "hideGeneralForumTopic",
            json={
                "chat_id": chat_id,
            }
        )
