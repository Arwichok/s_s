from litestar import Litestar, get
import msgspec


class Data(msgspec.Struct):
    name: str
    age: int


@get("/")
async def hello() -> dict:
    return Data(name="John", age=42)

app = Litestar(route_handlers=[hello])
