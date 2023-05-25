from .utils import *


class getFile:
    async def get_file(
        self,
        file_id : str = None,
    ):
        """
        Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.tlgr.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.
        
        Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received.

        Args:
            file_id (str): File identifier to get information about.
        """

        return await Curl.request(
            url=self.api + "getFile",
            json={
                "file_id": file_id,
            }
        )
