from .utils import *


class createForumTopic:
    async def create_forum_topic(
        self,
        chat_id : int | str = None,
        name : str = None,
        icon_color : int = None,
        icon_custom_emoji_id : str = None,
    ):
        """
        Use this method to create a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns information about the created topic as a ForumTopic object.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            name (str): Topic name, 1-128 characters.

            icon_color (int): Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F).

            icon_custom_emoji_id (str): Unique identifier of the custom emoji shown as the topic icon. Use getForumTopicIconStickers to get all allowed custom emoji identifiers..
        """

        return await Curl.request(
            url=api + "createForumTopic",
            json={
                "chat_id": chat_id,
                "name": name,
                "icon_color": icon_color,
                "icon_custom_emoji_id": icon_custom_emoji_id,
            }
        )
