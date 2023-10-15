import time
import psutil
from telethon import TelegramClient, events

# TeamUltroid/Ultroid
def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "w:") if weeks else "") +
           ((str(days) + "d:") if days else "") +
           ((str(hours) + "h:") if hours else "") +
           ((str(minutes) + "m:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp


class TeleClient(TelegramClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = time.time()
        self.add_event_handler(self.status, events.NewMessage(
            pattern="/statusbot", func=lambda e: e.is_private))

    @staticmethod
    async def status(event:events.NewMessage.Event):
        uptime = time_formatter((time.time() - event.client.start_time) * 1000)
        cpu = psutil.cpu_percent()
        TEXT = f"UPTIME: {uptime} | CPU: {cpu}%"
        await event.reply(TEXT)
