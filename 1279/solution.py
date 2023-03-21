class TrafficLight:
    def __init__(self):
        self.green = False
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)

    def switchLight(self):
        with self.lock:
            self.green = not self.green
            self.cv.notify_all()

    def isGreen(self):
        return self.green


class Road:
    def __init__(self):
        self.cars = []
        self.lock = threading.Lock()

    def addCar(self, carId):
        with self.lock:
            self.cars.append(carId)

    def removeCar(self, carId):
        with self.lock:
            self.cars.remove(carId)


class Intersection:
    def __init__(self, n):
        self.roads = [Road() for i in range(n)]
        self.trafficLight = TrafficLight()
        self.currentRoad = 0

    def trafficLight(self, carId, roadId, direction, arrivalTime, turnGreen, crossCar):
        road = self.roads[roadId - 1]
        with self.trafficLight.cv:
            while self.currentRoad != roadId or (turnGreen and not self.trafficLight.isGreen()):
                self.trafficLight.cv.wait()

            road.addCar(carId)

            if crossCar:
                road.removeCar(carId)

                if not road.cars:
                    self.trafficLight.switchLight()

            else:
                self.trafficLight.switchLight()

            if self.currentRoad == roadId:
                self.currentRoad = (self.currentRoad + 1) % len(self.roads)




