from .utils import *


class getMyDefaultAdministratorRights:
    async def get_my_default_administrator_rights(
        self,
        for_channels : bool = None,
    ):
        """
        Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success.

        Args:
            for_channels (bool): Pass True to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned..
        """

        return await Curl.request(
            url=api + "getMyDefaultAdministratorRights",
            json={
                "for_channels": for_channels,
            }
        )
