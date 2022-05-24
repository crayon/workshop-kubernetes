import os
from aiohttp import web

async def handle(request):      
    name = request.match_info.get('name', "World!")
    password = os.environ.get("PASSWORD")
    print(password)
    text = "Hello, " + name + ", your password is " + str(password)
    print('received request, replying with "{}".'.format(text))
    return web.Response(text=text)

running_port = os.environ.get("SERVER_PORT")
app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, port=int(running_port))
