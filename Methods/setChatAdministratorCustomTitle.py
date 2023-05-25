from .utils import *
import typing


class setChatAdministratorCustomTitle:
    async def set_chat_administrator_custom_title(
        self,
        chat_id : typing.Union[int, str] = None,
        user_id : int = None,
        custom_title : str = None,
    ):
        """
        Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            user_id (int): Unique identifier of the target user.

            custom_title (str): New custom title for the administrator; 0-16 characters, emoji are not allowed.
        """

        return await Curl.request(
            url=self.api + "setChatAdministratorCustomTitle",
            json={
                "chat_id": chat_id,
                "user_id": user_id,
                "custom_title": custom_title,
            }
        )
