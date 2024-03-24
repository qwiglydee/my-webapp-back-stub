from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.requests import Request
from starlette.exceptions import HTTPException
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")


async def homepage(request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


async def foopage(request):
    context = {"request": request, "header": "Foo"}
    return templates.TemplateResponse("page.html", context)


async def barpage(request):
    context = {"request": request, "header": "Bar"}
    return templates.TemplateResponse("page.html", context)


routes = [
    Route("/", homepage),
    Route("/foo", foopage),
    Route("/bar", barpage),
    Mount("/static", app=StaticFiles(directory="static"), name="static"),
]


app = Starlette(
    debug=True,
    routes=routes,
)
