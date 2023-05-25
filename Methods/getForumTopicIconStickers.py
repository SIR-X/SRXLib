from .utils import *
import typing


class getForumTopicIconStickers:
    async def get_forum_topic_icon_stickers(
        self,
        
    ):
        """
        Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of Sticker objects.

        Args:
            
        """

        return await Curl.request(
            url=self.api + "getForumTopicIconStickers",
            json={
                
            }
        )
