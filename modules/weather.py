#сделал @Aqendo
import asyncio
import logging
from .. import loader, utils
import requests
logger = logging.getLogger(__name__)
__version__ = 2
@loader.tds
class WeatherMod(loader.Module):
    """Weather module via wttr.in site"""
    strings = {"name":"Weather"}
    @loader.unrestricted
    async def wedcmd(self, message):
        """Sends picture of weather and deletes message"""
        await message.delete()
        image = (await utils.run_sync(requests.get, f"https://wttr.in/{utils.get_args_raw(message)}_0pq_lang=ru.png?m")).content
        await message.client.send_file(message.to_id, image)
        
    @loader.unrestricted
    async def wecmd(self, message):
        """Sends picture of weather without deleting message"""
        image = (await utils.run_sync(requests.get, f"https://wttr.in/{utils.get_args_raw(message)}_0pq_lang=ru.png?m")).content
        await message.client.send_file(message.to_id, image)
