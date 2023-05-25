from .utils import *
import typing


class setChatStickerSet:
    async def set_chat_sticker_set(
        self,
        chat_id : typing.Union[int, str] = None,
        sticker_set_name : str = None,
    ):
        """
        Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

            sticker_set_name (str): Name of the sticker set to be set as the group sticker set.
        """

        return await Curl.request(
            url=self.api + "setChatStickerSet",
            json={
                "chat_id": chat_id,
                "sticker_set_name": sticker_set_name,
            }
        )
