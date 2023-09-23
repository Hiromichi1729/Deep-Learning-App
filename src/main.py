from fastapi import FastAPI

from typing import Union,List
from pydantic import BaseModel

from MathHandler import MathHandler

app = FastAPI(docs_url="/docs")
mathHandler = MathHandler()

@app.post('/math/functions')
def mathIndex(
        funtionName :str,
        parameters :Union[float,List[float]]
    ):
    return mathHandler.functions(funtionName,parameters)