from .utils import *


class getWebhookInfo:
    async def get_webhook_info(
        self,
        
    ):
        """
        Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.

        Args:
            
        """

        return await Curl.request(
            url=self.api + "getWebhookInfo",
            json={
                
            }
        )
