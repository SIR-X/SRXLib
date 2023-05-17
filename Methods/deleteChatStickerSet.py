from .utils import *


class deleteChatStickerSet:
    async def delete_chat_sticker_set(
        self,
        chat_id : int | str = None,
    ):
        """
        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
        """

        return await Curl.request(
            url=api + "deleteChatStickerSet",
            json={
                "chat_id": chat_id,
            }
        )
