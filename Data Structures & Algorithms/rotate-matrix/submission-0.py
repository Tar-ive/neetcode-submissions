class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #transpose plus reverse order of elements in each row
        matrix[:] = [list(elem) for elem in zip(*matrix)]
        matrix[:] = [row[::-1] for row in matrix]


