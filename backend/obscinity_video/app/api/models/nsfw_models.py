from typing import List
from pydantic import BaseModel

class VideoUrls(BaseModel):
    urls:List[str]