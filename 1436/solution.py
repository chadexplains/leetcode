class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}
        for path in paths:
            cities[path[0]] = cities.get(path[0], 0) + 1
            cities[path[1]] = cities.get(path[1], 0) - 1
        for city, count in cities.items():
            if count == -1:
                return city