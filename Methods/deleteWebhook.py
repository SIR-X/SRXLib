from .utils import *
import typing


class deleteWebhook:
    async def delete_webhook(
        self,
        drop_pending_updates : bool = None,
    ):
        """
        Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.

        Args:
            drop_pending_updates (bool): Pass True to drop all pending updates.
        """

        return await Curl.request(
            url=self.api + "deleteWebhook",
            json={
                "drop_pending_updates": drop_pending_updates,
            }
        )
