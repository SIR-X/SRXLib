from .utils import *


class editGeneralForumTopic:
    async def edit_general_forum_topic(
        self,
        chat_id : int | str = None,
        name : str = None,
    ):
        """
        Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            name (str): New topic name, 1-128 characters.
        """

        return await Curl.request(
            url=self.api + "editGeneralForumTopic",
            json={
                "chat_id": chat_id,
                "name": name,
            }
        )
