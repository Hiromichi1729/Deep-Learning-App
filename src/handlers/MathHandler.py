from typing import Union,List

from Math.FunctionsUseCase import FunctionsUseCase
from Math.MatrixUseCase import MatrixUseCase

functionsUseCase = FunctionsUseCase()
matrixUseCase = MatrixUseCase()

class MathHandler:
    
    def __init__(slef):
        pass
    
    def functions(
        self,
        funtionName :str,
        parameters :Union[float,List[float]]
    ):
        return functionsUseCase.execute(funtionName,parameters)

    def matrix(
        self,
        matrix1 :Union[List[List[int]],List[int]],
        matrix2 :Union[List[List[int]],List[int]]
    ):
        return matrixUseCase.execute(matrix1,matrix2)