from .utils import *
import typing


class deleteForumTopic:
    async def delete_forum_topic(
        self,
        chat_id : typing.Union[int, str] = None,
        message_thread_id : int = None,
    ):
        """
        Use this method to delete a forum topic along with all its messages in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_delete_messages administrator rights. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            message_thread_id (int): Unique identifier for the target message thread of the forum topic.
        """

        return await Curl.request(
            url=self.api + "deleteForumTopic",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )
