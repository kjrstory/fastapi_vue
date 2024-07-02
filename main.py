from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse, HTMLResponse
from starlette.staticfiles import StaticFiles

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.mount("/css", StaticFiles(directory="frontend/dist/css"))
app.mount("/js", StaticFiles(directory="frontend/dist/js"))


@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")

@app.get("/{path_name:path}", response_class=HTMLResponse)
def catch_all(path_name: str):
    return FileResponse("frontend/dist/index.html")
