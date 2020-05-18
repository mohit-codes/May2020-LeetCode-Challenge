"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Constraints:
   *  2 <= coordinates.length <= 1000
   * coordinates[i].length == 2
   * -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
   * coordinates contains no duplicate point.


test case 1
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

test case 2
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2 : return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        if x2 - x1 == 0:
            m=0
        else:
            m = (y2 - y1) / (x2 - x1)
        # print(m)
        for i in range(2,n):
            # print(coordinates[i][1] , coordinates[i-1][1] , m,coordinates[i][0] , coordinates[i-1][0])
            if coordinates[i][1] - coordinates[i-1][1] != m*(coordinates[i][0] - coordinates[i-1][0]):
                # print('fail - ',coordinates[i][1] , coordinates[i-1][1] , m,coordinates[i][0] , coordinates[i-1][0])
                return False
        return True
