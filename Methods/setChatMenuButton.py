from .utils import *
import typing
from Types.MenuButton import MenuButton

class setChatMenuButton:
    async def set_chat_menu_button(
        self,
        chat_id : int = None,
        menu_button : MenuButton = None,
    ):
        """
        Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success.

        Args:
            chat_id (int): Unique identifier for the target private chat. If not specified, default bot's menu button will be changed.

            menu_button (MenuButton): A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault.
        """

        return await Curl.request(
            url=self.api + "setChatMenuButton",
            json={
                "chat_id": chat_id,
                "menu_button": menu_button,
            }
        )
