from typing import List
from pydantic import BaseModel

class ImageUrls(BaseModel):
    urls:List[str]