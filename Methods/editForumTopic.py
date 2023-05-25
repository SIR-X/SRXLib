from .utils import *


class editForumTopic:
    async def edit_forum_topic(
        self,
        chat_id : int | str = None,
        message_thread_id : int = None,
        name : str = None,
        icon_custom_emoji_id : str = None,
    ):
        """
        Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            message_thread_id (int): Unique identifier for the target message thread of the forum topic.

            name (str): New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept.

            icon_custom_emoji_id (str): New unique identifier of the custom emoji shown as the topic icon. Use getForumTopicIconStickers to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept.
        """

        return await Curl.request(
            url=self.api + "editForumTopic",
            json={
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "name": name,
                "icon_custom_emoji_id": icon_custom_emoji_id,
            }
        )
