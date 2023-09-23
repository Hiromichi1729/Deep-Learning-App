from Math.FunctionsUseCase import FunctionsUseCase

functionsUseCase = FunctionsUseCase()

class MathHandler:
    
    def __init__(slef):
        pass
    
    def functions(
        self,
        funtionName :str,
        parameters
    ):
        return functionsUseCase.execute(funtionName,parameters)