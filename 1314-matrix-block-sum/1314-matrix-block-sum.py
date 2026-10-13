class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        answer = [[0] * cols for _ in range(rows)]
        p = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                p[i +1][j+1] = mat[i][j] + p[i][j +1] + p[i + 1][j] - p[i][j]


        for i in range(rows):
            for j in range(cols):
                r1 = max(0 , i -k)
                c1 = max( 0 , j -k)
                r2 = min(rows , i +k + 1)
                c2 = min(cols , j + k + 1)
                answer[i][j] = p[r2][c2] - p[r1][c2] - p[r2][c1] + p[r1][c1] 

        return answer


                
        