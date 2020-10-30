#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0 
        x_coor = y_coor = 0
        direction = 'initial'

        for _ in range(n * m):
            # update x, y coordinate & diretion
            if direction == 'rt':   # top-right direction
                x_coor += 1
                y_coor -= 1
                if x_coor + 1 >= n:
                    direction = 'b'
                elif y_coor - 1 < 0:
                    direction = 'r'
            elif direction == 'lb': # bottom-left direction
                x_coor -= 1
                y_coor += 1
                if y_coor + 1 >= m:
                    direction = 'r'
                elif x_coor - 1 < 0:
                    direction = 'b'
            elif direction == 'r':   # right direction
                x_coor += 1
                if y_coor + 1 < m:
                    direction = 'lb'
                elif y_coor - 1 >= 0:
                    direction = 'rt'
            elif direction == 'b':   # down direction
                y_coor += 1
                if x_coor + 1 < n:
                    direction = 'rt'
                elif x_coor - 1 >= 0:
                    direction = 'lb'
            else:
                if  x_coor + 1 < n:
                    direction = 'r'
                elif y_coor + 1 < m:
                    direction = 'b'

            output.append(matrix[y_coor][x_coor])

        return output
       
# @lc code=end

