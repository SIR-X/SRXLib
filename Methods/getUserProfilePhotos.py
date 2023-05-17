from .utils import *


class getUserProfilePhotos:
    async def get_user_profile_photos(
        self,
        user_id : int = None,
        offset : int = None,
        limit : int = None,
    ):
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        Args:
            user_id (int): Unique identifier of the target user.

            offset (int): Sequential number of the first photo to be returned. By default, all photos are returned..

            limit (int): Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100..
        """

        return await Curl.request(
            url=api + "getUserProfilePhotos",
            json={
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
            }
        )
