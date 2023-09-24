from fastapi import FastAPI

from typing import Union,List
from pydantic import BaseModel

from MathHandler import MathHandler

app = FastAPI(docs_url="/docs")
mathHandler = MathHandler()

@app.post('/math/functions')
def mathFunctions(
        funtionName :str,
        parameters :Union[float,List[float]]
    ):
    return mathHandler.functions(funtionName,parameters)

@app.post('/math/matrix')
def mathMatrix(
       matrix1: Union[List[List[int]],List[int]],
       matrix2: Union[List[List[int]],List[int]]
    ):
    
    return mathHandler.matrix(matrix1,matrix2)
    