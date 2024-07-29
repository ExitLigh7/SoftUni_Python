from typing import List
from project.robots.female_robot import FemaleRobot
from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    VALID_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        try:
            service = self.VALID_SERVICE_TYPES[service_type](name)
        except KeyError:
            raise Exception("Invalid service type!")

        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        try:
            robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        except KeyError:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = self._find_service_by_name(service_name)
        robot = self._find_robot_by_name(robot_name)
        is_suitable = True

        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ != robot.SUITABLE_SERVICE:
            is_suitable = False
        elif robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ != robot.SUITABLE_SERVICE:
            is_suitable = False

        if not is_suitable:
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._find_service_by_name(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        number_of_robots_fed = 0
        service = self._find_service_by_name(service_name)

        for robot in service.robots:
            robot.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = self._find_service_by_name(service_name)
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(service.details() for service in self.services)

    # helper methods
    def _find_service_by_name(self, service_name):
        service = next(s for s in self.services if s.name == service_name)
        return service

    def _find_robot_by_name(self, robot_name):
        robot = next(r for r in self.robots if r.name == robot_name)
        return robot
