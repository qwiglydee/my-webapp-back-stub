from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute, Mount
from starlette.requests import Request
from starlette.exceptions import HTTPException
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket

templates = Jinja2Templates(directory="templates")


async def homepage(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


async def foopage(request: Request):
    context = {"request": request, "header": "Foo"}
    return templates.TemplateResponse("page.html", context)


async def barpage(request: Request):
    context = {"request": request, "header": "Bar"}
    return templates.TemplateResponse("page.html", context)


async def echopage(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("echo.html", context)


async def echosock(websocket: WebSocket):
    await websocket.accept()
    async for msg in websocket.iter_text():
        await websocket.send_text(f"({msg})")
    await websocket.close()


routes = [
    Route("/", homepage),
    Route("/foo", foopage),
    Route("/bar", barpage),
    Route("/echo", echopage),
    WebSocketRoute(
        "/echo/ws",
        echosock,
    ),
    Mount("/static", app=StaticFiles(directory="static"), name="static"),
]


app = Starlette(
    debug=True,
    routes=routes,
)
