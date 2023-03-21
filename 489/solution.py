class Solution:
    def cleanRoom(self, robot):
        visited = set()
        def dfs(x, y, dx, dy):
            robot.clean()
            visited.add((x, y))
            for _ in range(4):
                if (x+dx, y+dy) not in visited and robot.move():
                    dfs(x+dx, y+dy, dx, dy)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnLeft()
                dx, dy = -dy, dx
        dfs(0, 0, 1, 0)