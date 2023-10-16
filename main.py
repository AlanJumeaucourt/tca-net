import os
from dotenv import load_dotenv
import asyncio


async def send_update(auth_token: str, discord_al: DiscordAccessLayer):
    """
    Fetch timetable though the crawler,
    and sends an update message though the discord_al.
    """

    while True:

        # Fetch timetable
        with get_crawler_ctx(auth_token) as crawler:
            timetable = crawler.get_timetable()

        # Action to do with the timetable ...
        discord_al.send_next_course(timetable.next_course)

        # async wait for next iteration
        await asyncio.sleep(3600)


def main():
    # Load environment
    load_dotenv()
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')  # noqa
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  # noqa

    if not AUTH_TOKEN or not DISCORD_TOKEN:
        raise EnvironmentError("Environment badly set-up.")

    with get_discord_ctx(DISCORD_TOKEN) as discord_al:
        # Now, the Discord bot runs even if it is not called directly

        # Create an asyncio task
        loop = asyncio.get_event_loop()
        task = loop.create_task(send_update(AUTH_TOKEN, discord_al))

        try:
            loop.run_until_complete(task)
        except (Exception, KeyboardInterrupt):
            pass


if __name__ == "__main__":
    main()
