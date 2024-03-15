import asyncio
from aiohttp import web

import config
from bot import main


async def handle(request):
    return web.Response(text="ok")


async def start_ws():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()


async def main_task():
    if bool(config.ENABLE_RENDER):
        await asyncio.gather(
            main(),
            start_ws()
        )
    else:
        await asyncio.gather(
            main()
        )


if __name__ == "__main__":
    asyncio.run(main_task())
