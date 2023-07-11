from pydantic import BaseModel
from datetime import datetime

class FileMetadata(BaseModel):
    content:str
    size: float
    date_of_acquisition:datetime
    source: str
    result: str
    type_of_file:str