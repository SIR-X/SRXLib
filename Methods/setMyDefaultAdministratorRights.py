from .utils import *
from Types.ChatAdministratorRights import ChatAdministratorRights

class setMyDefaultAdministratorRights:
    async def set_my_default_administrator_rights(
        self,
        rights : ChatAdministratorRights = None,
        for_channels : bool = None,
    ):
        """
        Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns True on success.

        Args:
            rights (ChatAdministratorRights): A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared..

            for_channels (bool): Pass True to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed..
        """

        return await Curl.request(
            url=self.api + "setMyDefaultAdministratorRights",
            json={
                "rights": rights,
                "for_channels": for_channels,
            }
        )
