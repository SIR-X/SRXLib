from .utils import *


class getChatMenuButton:
    async def get_chat_menu_button(
        self,
        chat_id : int = None,
    ):
        """
        Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success.

        Args:
            chat_id (int): Unique identifier for the target private chat. If not specified, default bot's menu button will be returned.
        """

        return await Curl.request(
            url=api + "getChatMenuButton",
            json={
                "chat_id": chat_id,
            }
        )
