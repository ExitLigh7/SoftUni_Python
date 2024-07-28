from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."

        except StopIteration:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        try:
            reg_vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        except KeyError:
            return f"Vehicle type {vehicle_type} is inaccessible."

        licence_plate_duplicating = (
            next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None))
        if licence_plate_duplicating:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(reg_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        filtered_route = self._find_route_by_start_point_and_end_point(start_point, end_point)
        if filtered_route is not None:
            if filtered_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if filtered_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if filtered_route.length > length:
                filtered_route.is_locked = True
        new_route = self._create_route(start_point, end_point, length)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int,  is_accident_happened: bool):

        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        route = next(r for r in self.routes if r.route_id == route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return (f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} "
                f"Battery: {vehicle.battery_level}% Status: {'Damaged' if vehicle.is_damaged else 'OK'}")

    def repair_vehicles(self, count: int):

        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_dmg_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))

        able_to_repair = sorted_dmg_vehicles[:count]
        if able_to_repair:
            for vehicle in able_to_repair:
                vehicle.change_status()
                vehicle.recharge()

        return f"{len(able_to_repair)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)

        result = "*** E-Drive-Rent ***\n"
        users_info = '\n'.join(u.__str__() for u in sorted_users)
        result += users_info
        return result

    def _find_route_by_start_point_and_end_point(self, start_point: str, end_point: str):
        filtered_routes = [route for route in self.routes if
                           route.start_point == start_point and route.end_point == end_point]
        if filtered_routes:
            return filtered_routes[0]
        return None

    def _create_route(self, start_point: str, end_point: str, length: float):
        idx = len(self.routes) + 1
        return Route(start_point, end_point, length, route_id=idx)
