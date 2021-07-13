class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == 0:
            return []
        totalVals = len(mat) * len(mat[0])
        if r * c == totalVals:
            res = [[]]
            pos = 0
            for i in mat:
                for j in i:
                    if len(res[pos]) == c:
                        pos += 1
                        res.append([])
                    res[pos].append(j)
            return res
        else: 
            return mat
        