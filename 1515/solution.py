class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def dist(x, y):
            return sum(((a-x)**2 + (b-y)**2)**0.5 for a, b in positions)
        def gradient(x, y):
            grad_x, grad_y = 0, 0
            for a, b in positions:
                grad_x += (x-a)/((a-x)**2 + (b-y)**2)**0.5
                grad_y += (y-b)/((a-x)**2 + (b-y)**2)**0.5
            return [grad_x, grad_y]
        def hessian(x, y):
            hess_xx, hess_xy, hess_yx, hess_yy = 0, 0, 0, 0
            for a, b in positions:
                d = ((a-x)**2 + (b-y)**2)**0.5
                hess_xx += (y-b)**2/d**3
                hess_xy += (x-a)*(y-b)/d**3
                hess_yx += (x-a)*(y-b)/d**3
                hess_yy += (x-a)**2/d**3
            return [[hess_xx, hess_xy], [hess_yx, hess_yy]]
        x, y = sum(x for x, y in positions)/len(positions), sum(y for x, y in positions)/len(positions)
        step_size = 1
        while step_size > 1e-6:
            grad = gradient(x, y)
            hess = hessian(x, y)
            delta_x, delta_y = numpy.linalg.solve(hess, [-g for g in grad])
            if dist(x+delta_x, y+delta_y) < dist(x, y):
                x, y = x+delta_x, y+delta_y
            else:
                step_size /= 2
        return dist(x, y)