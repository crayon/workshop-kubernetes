import os
from aiohttp import web

def paste_from_config_file(parameter: str):
    with open("/data/hello-server/config/config.yaml") as file:
        for line in file:
            if parameter in line:
                setting = line.rstrip().replace("{}:".format(parameter), "").lstrip()
    return setting

async def handle(request):      
    name = request.match_info.get('name', "World!")
    password = os.environ.get("PASSWORD")
    print(password)
    text = "Hello, " + name + ", your password is " + str(password)
    print('received request, replying with "{}".'.format(text))
    return web.Response(text=text)

running_port = paste_from_config_file("server_port")
app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, port=int(running_port))
