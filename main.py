from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router
from domain.comment import comment_router
from domain.user import user_router

app = FastAPI()

origins = [
    "http://192.168.100.12:8080",
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
app.include_router(comment_router.router)
app.include_router(user_router.router)
