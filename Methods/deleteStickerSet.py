from .utils import *


class deleteStickerSet:
    async def delete_sticker_set(
        self,
        name : str = None,
    ):
        """
        Use this method to delete a sticker set that was created by the bot. Returns True on success.
        
        The following methods and objects allow your bot to work in inline mode.
        Please see our Introduction to Inline bots for more details.
        
        To enable this option, send the /setinline command to @BotFather and provide the placeholder text that the user will see in the input field after typing your bot's name.

        Args:
            name (str): Sticker set name.
        """

        return await Curl.request(
            url=self.api + "deleteStickerSet",
            json={
                "name": name,
            }
        )
