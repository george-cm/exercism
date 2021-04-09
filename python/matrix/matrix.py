class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [
            [int(x) for x in row.split()]
            for row in matrix_string.splitlines()]

    def row(self, index: int) -> list:
        # row behaves like column, the simple modification
        return self.matrix[index-1][:]

    def column(self, index: int) -> list:
        return [row[index-1] for row in self.matrix]

    def __repr__(self) -> str:        
        return "\n".join([
            (" ".join([str(x) for x in row])) 
            for row in self.matrix])