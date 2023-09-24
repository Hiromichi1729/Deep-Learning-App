import numpy as np
from typing import Union,List

class FunctionsUseCase:
    
    def __init__(self):
        pass
    
    def execute(
        self,
        functionName :str,
        parameters :Union[float,List[float]]
    ) -> Union[float,List[float]]:
        if functionName == 'step':
            return self.__step(parameters)

        if functionName == 'sigmoid':
            return self.__sigmoid(parameters)
        
        if functionName == 'ReLU':
            return self.__relu(parameters)
        
        if functionName == 'softmax':
            return self.__softmax(parameters)
            
        return parameters
        
    def __step(
        self,
        parameters
    ) -> Union[float,List[float]]:
        return np.array(parameters, float).tolist()

    def __sigmoid(
        self,
        parameters
    ):
        return (1 / (1 + np.exp(-np.array(parameters)))).tolist()

    def __relu(
        self,
        parameters
    ) -> Union[float,List[float]]:
        return np.maximum(0,np.array(parameters)).tolist()
    
    def __softmax(
        self,
        parameters
    ) -> Union[float,List[float]]:
        exp = np.exp(np.array(parameters))
        sumExp = np.sum(exp)
        return (exp/sumExp).tolist()
