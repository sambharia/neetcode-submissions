class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for s in range(len(matrix)):
            if matrix[s][len(matrix[s])-1] < target:
                continue
            elif matrix[s][len(matrix[s])-1] == target:
                return True
            else: 
                l = 0
                r = len(matrix[s]) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if matrix[s][m] == target:
                        return True
                    elif matrix[s][m] > target:
                        r = m - 1
                    else:
                        l = m + 1  # Fixed: Jump past the middle
                return False # Fixed: Indented outside the while loop
        
        return False # Fixed: Handles cases where target is greater than all elements