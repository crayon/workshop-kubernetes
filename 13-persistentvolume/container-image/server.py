import os
from aiohttp import web
from datetime import datetime

def paste_from_config_file(parameter: str):
    with open("/data/hello-server/config/config.yaml") as file:
        for line in file:
            if parameter in line:
                setting = line.rstrip().replace("{}:".format(parameter), "").lstrip()
    return setting

async def handle(request):      
    name = request.match_info.get('name', "World!")
    text = "Hello, " + name + ", your password is " + str(password)
    print('received request, replying with "{}".'.format(text))

    with open(file_path, 'a') as f:
        current_time = datetime.utcnow().strftime("%H:%M:%S %d.%m.%y")
        f.write(f"{current_time} - {text}\n")

    return web.Response(text=text)

password = os.environ.get("PASSWORD")
running_port = paste_from_config_file("server_port")
file_path = paste_from_config_file("logfile_path")

if not os.path.isfile(file_path):
    fp = open(file_path, 'x')
    fp.close()

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, port=int(running_port))
