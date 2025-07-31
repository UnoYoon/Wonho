import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_with_points = []

        for point in points:
            x, y = point
            dist_sq = x ** 2 + y ** 2
            distance_with_points.append((dist_sq, point))
        
        distance_with_points.sort(key=lambda x: x[0])

        return [point for _, point in distance_with_points[:k]]