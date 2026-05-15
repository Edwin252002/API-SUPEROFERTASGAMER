from pydantic import BaseModel

class Giveaway(BaseModel):
    id: int
    title: str
    worth: str
    thumbnail: str
    platforms: str
    description: str
    open_giveaway_url: str