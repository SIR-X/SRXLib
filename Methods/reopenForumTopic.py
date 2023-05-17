from .utils import *


class reopenForumTopic:
    async def reopen_forum_topic(
        self,
        chat_id : int | str = None,
        message_thread_id : int = None,
    ):
        """
        Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            message_thread_id (int): Unique identifier for the target message thread of the forum topic.
        """

        return await Curl.request(
            url=api + "reopenForumTopic",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )
