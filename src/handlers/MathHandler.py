from typing import Union, List, Callable

from Math.FunctionsUseCase import FunctionsUseCase
from Math.MatrixUseCase import MatrixUseCase
from Math.DifferentialUseCase import DifferentialUseCase

functionsUseCase = FunctionsUseCase()
matrixUseCase = MatrixUseCase()
differentialUseCase = DifferentialUseCase()

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
    
    def differential(
        function,
        a :float
    ):
        return differentialUseCase.execute(function, a)