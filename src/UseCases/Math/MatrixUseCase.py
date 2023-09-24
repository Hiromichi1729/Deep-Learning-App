import numpy as np
from typing import Union,List

class MatrixUseCase:
    
    def __init__(self):
        pass
    
    def execute(
        self,
        matrix1 :Union[List[List[int]],List[int]],
        matrix2 :Union[List[List[int]],List[int]]
    ) -> List[float]:
        npMatrix1 , npMatrix2 = np.array(matrix1) , np.array(matrix2)

        if np.ndim(npMatrix1) != npMatrix2.shape[0]:
            raise Exception("行列1の行と行列2の列を揃えて下さい。") 
            
        return np.dot(npMatrix1 ,npMatrix2).tolist()