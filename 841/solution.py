class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(0, rooms, visited)
        return len(visited) == len(rooms)
    
    def dfs(self, room, rooms, visited):
        visited.add(room)
        for key in rooms[room]:
            if key not in visited:
                self.dfs(key, rooms, visited)