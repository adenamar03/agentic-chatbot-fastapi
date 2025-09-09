# step 1 --> setup pydantic model (schema validaton)

from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt:str
    messages:List[str]
    allow_search:bool 

# step 2 -> step up ai agent from frontend request



#step 3--> run app and explore swagger ui docs