from litestar import Litestar, get
import msgspec
import faker


fake = faker.Faker()


class User(msgspec.Struct):
    name: str
    age: int


class Data(msgspec.Struct):
    user: User
    text: str



@get("/")
async def hello() -> list[Data]:
    return [Data(user=User(name=fake.name(), age=fake.random_int(min=1, max=100)), text=fake.text()) for _ in range(4)]



app = Litestar(route_handlers=[hello])
