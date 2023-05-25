from .utils import *
from Types.InputFile import InputFile

class setWebhook:
    async def set_webhook(
        self,
        url : str = None,
        certificate : InputFile = None,
        ip_address : str = None,
        max_connections : int = None,
        allowed_updates : list[str] = None,
        drop_pending_updates : bool = None,
        secret_token : str = None,
    ):
        """
        Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success.
        
        If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header “X-Telegram-Bot-Api-Secret-Token” with the secret token as content.

        Args:
            url (str): HTTPS URL to send updates to. Use an empty string to remove webhook integration.

            certificate (InputFile): Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details..

            ip_address (str): The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS.

            max_connections (int): The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput..

            allowed_updates (list[str]): A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used.Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time..

            drop_pending_updates (bool): Pass True to drop all pending updates.

            secret_token (str): A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token” in every webhook request, 1-256 characters. Only characters A-Z, a-z, 0-9, _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you..
        """

        return await Curl.request(
            url=self.api + "setWebhook",
            json={
                "url": url,
                "certificate": certificate,
                "ip_address": ip_address,
                "max_connections": max_connections,
                "allowed_updates": allowed_updates,
                "drop_pending_updates": drop_pending_updates,
                "secret_token": secret_token,
            }
        )
