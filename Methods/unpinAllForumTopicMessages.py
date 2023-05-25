from .utils import *
import typing


class unpinAllForumTopicMessages:
    async def unpin_all_forum_topic_messages(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
    ):
        """
        Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            message_thread_id (int): Unique identifier for the target message thread of the forum topic.
        """

        return await Curl.request(
            url=self.api + "unpinAllForumTopicMessages",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )
