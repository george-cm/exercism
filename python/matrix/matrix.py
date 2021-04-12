from typing import List

class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [
            [int(x) for x in row.split()]
            for row in matrix_string.splitlines()]
        self.transposed = self._transposed()
    
    def _transposed(self):
        t = [[0 for x in range(len(self.matrix))] for y in range(len(self.matrix[0]))]
        for j in range(len(self.matrix[0])):            
            for i in range(len(self.matrix)):
                t[j][i] = self.matrix[i][j]            
        return t


    def row(self, index: int) -> List[int]:
        # row behaves like column, the simple modification
        return self.matrix[index-1]

    def column(self, index: int) -> List[int]:
        t = []
        for r in range(len(self.matrix)):
            t.extend([self.matrix[r][index-1]])
        return t

    def transposed_str(self) -> str:        
        return "\n".join([
            (" ".join([str(x) for x in row])) 
            for row in self.transposed])

    def __repr__(self) -> str:        
        return "\n".join([
            (" ".join([str(x) for x in row])) 
            for row in self.matrix])