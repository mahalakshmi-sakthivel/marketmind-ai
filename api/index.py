import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

milestone4_dir = os.path.join(BASE_DIR, "Milestone_4")
if os.path.exists(milestone4_dir) and milestone4_dir not in sys.path:
    sys.path.insert(0, milestone4_dir)

from backend.main import app as fastapi_app

class VercelPathFixer:
    def __init__(self, asgi_app):
        self.asgi_app = asgi_app

    async def __call__(self, scope, receive, send):
        if scope.get("type") in ("http", "websocket"):
            headers = dict(scope.get("headers", []))
            matched_path = headers.get(b"x-matched-path")
            if matched_path:
                decoded = matched_path.decode("utf-8").split("?")[0]
                scope["path"] = decoded
        await self.asgi_app(scope, receive, send)

app = VercelPathFixer(fastapi_app)
