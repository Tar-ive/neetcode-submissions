class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix1 = [list(elem) for elem in zip(*matrix)]
        return matrix1
        