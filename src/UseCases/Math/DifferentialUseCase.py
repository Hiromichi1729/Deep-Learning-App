from typing import Callable

class DifferentialUseCase:
    
    def __init__(self) -> None:
        pass
    
    def execute(
        function,
        a :float,
    ):
        h = 1e-5
        return (function(a + h) - function(a - h)) / (2 * h)