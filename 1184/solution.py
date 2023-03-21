class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance = sum(distance)
        distance_between_stops = abs(start - destination)
        return min(distance_between_stops, total_distance - distance_between_stops)