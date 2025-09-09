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

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama-3.3-70b-versatile","gpt-4o-mini","mistral-8x7b-32768"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request:RequestState):
    """
    API ENDPOINT TO INTERACT WITH THE CHATBOT USING LANGRAPGH AND SEARCHTOOLS.
    IT DYNAMICALLY SELECTS THE MODEL SPECIFID IN THE REQUEST
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"INVALID MODEL NAME. KINDLY SELECT A VALID AI MODEL"}
    
    llm_id=request.model_name
    query = request.messages[-1] if request.messages else ""
    allow_search=request.allow_search
    system_prompt=request.system_prompt
    provider=request.model_provider
    #create an ai agent and get response from it    
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider) 
    return response

#step 3--> run app and explore swagger ui docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1", port=9999)