from typing import List
from project.robots.female_robot import FemaleRobot
from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService


class RobotsManagingApp:
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services = List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        pass

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        pass

    def add_robot_to_service(self, robot_name: str, service_name: str):
        pass

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        pass

    def feed_all_robots_from_service(self, service_name: str):
        pass

    def service_price(self, service_name: str):
        pass

    def __str__(self):
        pass

