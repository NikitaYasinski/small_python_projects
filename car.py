import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        root_ext = os.path.splitext(self.photo_file_name)
        return root_ext[1]

class Car(CarBase):
    car_type = "car"

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.passenger_seats_count = int(passenger_seats_count)
        super().__init__(brand, photo_file_name, carrying)


class Truck(CarBase):
    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

        try:
            length, width, height = (float(c) for c in body_whl.split("x"))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height


    def get_body_volume(self):
        return float(self.body_length) * float(self.body_width) * float(self.body_height)


class SpecMachine(CarBase):
    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def file_valid(s):
    list_res = [".jpg", ".jpeg", ".gif", ".png"]
    res = os.path.splitext(s)[1]
    for i in list_res:
        if res == i:
            return True
    return False

def truck_valid(row):
    if row[1] != "" and row[3] != "" and row[5] != "":
        return True
    return False

def car_valid(row):
    if truck_valid(row) and row[2] != "":
        return True
    return False

def spec_valid(row):
    if truck_valid(row) and row[6] != "":
        return True
    return False




def get_car_list(csv_filename):

    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row:
                if row[0] == "car":
                    if car_valid(row) and file_valid(row[3]):
                        car = Car(row[1], row[3], row[5], row[2])
                        car_list.append(car)
                elif row[0] == "truck" and file_valid(row[3]):
                    if truck_valid(row):
                        truck = Truck(row[1], row[3], row[5], row[4])
                        car_list.append(truck)
                elif row[0] == "spec_machine" and file_valid(row[3]):
                    if spec_valid(row):
                        spec = SpecMachine(row[1], row[3], row[5], row[6])

                        car_list.append(spec)
    return car_list


