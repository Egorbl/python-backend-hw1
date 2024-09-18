import json
from helper import is_int, send_answer
from src.factorial import factorial
from src.fibonacci import fibonacci
from src.mean import mean

async def router(scope, receive, send) -> None:
    path = scope['path']

    if path == "/factorial":
        await factorial(scope, receive, send)
        return
    if path.startswith("/fibonacci"):
        await fibonacci(scope, receive, send)
        return
    if path == "/mean":
        await mean(scope, receive, send)
        return

    await send_answer(send, 404, "404 Not Found")
