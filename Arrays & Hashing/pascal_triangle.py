# 118. Pascal's Triangle

class Solution:
    # Time: O(n^2), Memory: O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        rows=[]
        rows.append([1])
        if numRows==1:
            return rows
        rows.append([1,1])
        i=2
        while i<numRows:
            rows.append([])
            rows[i].append(1)
            j=1
            while j<len(rows[i-1]):
                rows[i].append(rows[i-1][j-1]+rows[i-1][j])
                j+=1
            rows[i].append(1)
            i+=1
        return rows
