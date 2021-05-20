import secrets
ac = []
number_buildings, apart_type1, apart_type2 = 0, 0, 0
class Developer:
    corporation_name = "Kiev Buildings"
    apartments_type1 = []
    apartments_type2 = []
    building_info = []

    def __init__(self, n, type1, type2):
        self.n = n
        self.type1 = type1
        self.type2 = type2
        self.ventilation = "off"
        self.water_supply = "off"
        self.sewerage = "off"
        self.heat_supply = "off"
        self.power_supply = "off"

    def start_ventilation_system(self):
        self.ventilation = "on"

    def stop_ventilation_system(self):
        self.ventilation = "off"

    def connect_water_supply(self):
        self.water_supply = "on"

    def disconnect_water_supply(self):
        self.water_supply = "off"

    def start_sewerage_system(self):
        self.sewerage = "on"

    def stop_sewerage_system(self):
        self.sewerage = "off"

    def start_heat_supply(self):
        self.heat_supply = "on"

    def stop_heat_supply(self):
        self.heat_supply = "off"

    def start_power_supply(self):
        self.power_supply = "on"

    def stop_power_supply(self):
        self.power_supply = "off"

    def show_status(self):
        print("Systems status is:\n", "ventilation:", self.ventilation, ", water:", self.water_supply,
              ", sewerage:", self.sewerage, ", heat:", self.heat_supply, ", power:", self.power_supply)

    def apart_info_input(self):
        print("Hi, Developer, enter apartment's parameters:")
        print("How many rooms for type1?")
        rooms1 = input()
        print("What`s the total area?")
        area1 = input()
        print("What`s the height?")
        height1 = input()
        print("What`s the lighting area?")
        lighting1 = input()
        print("What`s the temperature?")
        temperature1 = input()
        self.apartments_type1 = [Apartment(rooms1, area1, height1, lighting1, temperature1, i+1) for i in range(int(self.type1))]
        print("How many rooms for type2?")
        rooms2 = input()
        print("What`s the total area?")
        area2 = input()
        print("What`s the height?")
        height2 = input()
        print("What`s the lighting area?")
        lighting2 = input()
        print("What`s the temperature?")
        temperature2 = input()
        self.apartments_type2 = [Apartment(rooms2, area2, height2, lighting2, temperature2, i+1) for i in range(int(self.type2))]

    def give_aparts_info(self):
        return self.apartments_type1, self.apartments_type2

    def building_info_input(self):
        print("Hi, Developer, enter apartment building`s parameters:")
        print("What`s the fire resistance level?")
        fire_res_level = int(input())
        print("How many floors?")
        floors = int(input())
        print("What`s the floor`s height?")
        floor_height = float(input())
        print("What`s the corridor width?")
        corridor_width = float(input())
        print("What`s the floor`s area?")
        floor_area = int(input())
        print("What`s the temperature?")
        temperature = int(input())
        self.building_info = [fire_res_level, floors, floor_height, corridor_width, floor_area, temperature]

    def give_building_info(self):
        return self.building_info

    def put_into_operation(self):
        self.start_ventilation_system()
        self.connect_water_supply()
        self.start_sewerage_system()
        self.start_heat_supply()
        self.start_power_supply()
        self.show_status()

    def take_out_of_operation(self):
        self.stop_ventilation_system()
        self.disconnect_water_supply()
        self.stop_sewerage_system()
        self.stop_heat_supply()
        self.stop_power_supply()
        self.show_status()

class Worker:
    def __init__(self, first_name, second_name, speciality):
        self.first_name = first_name
        self.second_name = second_name
        self.speciality = speciality
        self.id_pass = 0
        self.status = "without job"

    def job_apply(self):
        self.status = "with job"
        return self.first_name, self.second_name, self.speciality

    def job_retire(self):
        self.status = "without job"

    def get_pass(self, password):
        self.id_pass = password

class Inhabitant:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.address = ""
        self.id_pass = 0

    def get_pass(self, password):
        self.id_pass = password

    def call_stuff(self):
        print("New inhabitant arrived, stuff required at the registration room!")

    def buy_apartment(self, n, type1, type2, rooms):
        if rooms == 1:
            ac.apart_buildings[n-1].apart_type1[type1-1].change_state_b(type1)
            print("Bought flat number", type1)
        if rooms == 2:
            ac.apart_buildings[n-1].apart_type1[type2-1].change_state_b(type2)
            print("Bought flat number", type2)

class Security_System:
    system_type= "wireless"
    notification_type ="siren&sms"
    system_state = "normal"
    def check_system_state(self):
        return self.system_state

    def change_system_state_normal(self):
        self.system_state = "on"

    def change_system_state_emergency(self):
        self.system_state = "emergency"

class TelecommunicationSystem:
    isp = "Triolan"
    database_name = "MariaDB"
    workers_db = []
    inhabitants_db = []
    def add_worker_info(self, worker):
        self.workers_db.append(Worker(worker.first_name, worker.second_name, worker.speciality))

    def add_inhabitants_info(self, inhabitants):
        self.inhabitants_db.append(Inhabitant(inhabitants.first_name, inhabitants.second_name))

class ApartmentManagment:
    workers = []
    inhabitants = []
    sec_system = Security_System()
    tel_system = TelecommunicationSystem()
    def employ_worker(self, worker):
        self.workers.append(Worker(worker.first_name, worker.second_name, worker.speciality))
        self.workers[len(self.workers)-1].job_apply()
        self.tel_system.add_worker_info(worker)

    def add_inhabitants(self, inhabitants):
        self.inhabitants.append(Inhabitant(inhabitants.first_name, inhabitants.second_name))
        self.tel_system.add_inhabitants_info(inhabitants)

    def list_workers(self):
        for i in range (len(self.workers)):
            print("Data about worker #", i+1, self.workers[i].first_name, self.workers[i].second_name, self.workers[i].speciality)

    def list_inhabitants(self):
        for i in range (len(self.inhabitants)):
            print("Data about inhabitant #", i+1, self.inhabitants[i].first_name, self.inhabitants[i].second_name)

    def dismiss_worker(self, first_name, second_name, speciality):
        for i in range (len(workers)-1):
            if self.workers[i].first_name == first_name and self.workers[i].second_name == second_name:
                del self.workers[i]
                print("Worker", first_name, second_name, "dismissed")

    def provide_pass(self):
        print("Enter worker's id to give him password:")
        i = int(input())
        password = secrets.token_hex(6)
        print(password)
        self.workers[i].get_pass(password)

    def provide_inhab_pass(self):
        print("Enter inhabitant's id to give him password:")
        i = int(input()) - 1
        password = secrets.token_hex(6)
        print(password)
        self.inhabitants[i].get_pass(password)

    def take_pass(self):
        print("Enter worker's id to take his password:")
        i = int(input())
        print(self.workers[i].first_name, self.workers[i].second_name, "`s password is:", self.workers[i].id_pass)

    def take_inhab_pass(self):
        print("Enter inhabitant's id to take his password:")
        i = int(input()) - 1
        print(self.inhabitants[i].first_name, self.inhabitants[i].second_name, "`s password is:", self.inhabitants[i].id_pass)

    def install_alarm(self):
        print("Security system alarm installed")

    def turn_on_alarm(self):
        print("!!! ATTENTION! SECURITY ALARM TURNED ON, PLEASE LEAVE BUILDING !!!")
        self.sec_system.change_system_state_emergency()

    def turn_off_alarm(self):
        print("!!! You can now go back into the building !!!")
        self.sec_system.change_system_state_normal()

    def stuff_call(self):
        self.inhabitants[0].call_stuff()
        print("Stuff is ready to work with new inhabitan")

class PowerSupplySystem:
    cable_type = "hidden"
    cable_cores_number = 4
    status = "disconnected"

    def power_supply_check(self):
        return self.status

    def power_on(self):
        self.status = "connected"

    def power_off(self):
        self.status = "disconnected"

class Apartment:
    def __init__(self, rooms, area, height, lighting, temperature, number):
        self.state = "free"
        self.number = number
        self.rooms = rooms
        self.area = area
        self.height = height
        self.lighting = lighting
        self.temperature = temperature

    def change_state_b(self, number):
        self.state = "bought"

    def change_state_f(self, number):
        self.state = "free"

    def send_state(self, number):
        return self.state

class ApartmentBuilding:
    state = "not in exploitation"
    apart_buildings = []
    def __init__(self, type1, type2, a_1, a_2, build_info):
        self.type1 = type1
        self.type2 = type2
        self.fire_res_level = build_info[0]
        self.floors = build_info[1]
        self.floor_height = build_info[2]
        self.corridor_width = build_info[3]
        self.floor_area = build_info[4]
        self.temperature = build_info[5]
        self.apart_type1 = [Apartment(a_1[0], a_1[1], a_1[2], a_1[3], a_1[4], i+1) for i in range(int(self.type1))]
        self.apart_type2 = [Apartment(a_2[0], a_2[1], a_2[2], a_2[3], a_2[4], i+1) for i in range(int(self.type2))]

    def change_state(self):
        self.state = "in exploitation"

    def put_out_of_exploitation(self):
        self.state = "not in exploitation"

class ApartmentComplex:
    pss = PowerSupplySystem()
    def __init__(self, n):
        self.n = n
        self.apart_buildings = []
        self.state = "not in exploitation"
        self.name = "Silver Breeze"

    def change_state_ex(self, type1, type2, a_1, a_2, building_info):
        self.apart_buildings = [ApartmentBuilding(type1, type2, a_1, a_2, building_info) for i in range(int(self.n))]
        check_buildings_state = 0
        for i in range(int(self.n)):
            if self.apart_buildings[i].state == "in exploitation":
                check_buildings_state += 1
        if check_buildings_state == self.n:
            self.state = "in exploitation"

    def set_building_state(self, number):
        self.apart_buildings[number].change_state()

    def change_state_non_ex(self):
        self.state = "not in exploitation"
        for i in range(int(self.n)):
            self.apart_buildings[i].state = "not in exploitation"

    def check_requirements(self, dev):
        print("Checking your building`s parameters . . .")
        if (int(dev.apartments_type1[0].rooms) == 1 and 30 <= int(dev.apartments_type1[0].area) <= 40
                and float(dev.apartments_type1[0].height) >= 2.5 and 5.5 <= float(dev.apartments_type1[0].lighting) <= 8
                and 18 <= int(dev.apartments_type1[0].temperature) <= 25) and (int(dev.apartments_type2[0].rooms) == 2
                and 48 <= int(dev.apartments_type2[0].area) <= 58
                and float(dev.apartments_type2[0].height) >= 2.5 and 5.5 <= float(dev.apartments_type2[0].lighting) <=8
                and 18 <= int(dev.apartments_type2[0].temperature) <= 25):
            if (dev.building_info[0] == 1 and dev.building_info[1] <= 25 and dev.building_info[2] >= 2.8 and
            1.6 <= dev.building_info[3] <= 1.8 and dev.building_info[4] <= 2220 and 5 <= dev.building_info[5] <= 25) or (
                    dev.building_info[0] == 2 and dev.building_info[1] <= 10 and dev.building_info[2] >= 2.8 and
                    1.6 <= dev.building_info[3] <= 1.8 and dev.building_info[4] <= 2220 and 5 <= dev.building_info[
                        5] <= 25
            ):
                print("Requirements satisfied!")
                return True
        else:
            print("Your building doesn't meet the requirements! I won't give you a permission to build!")
            return False

    def connect_electricity(self):
        self.pss.power_on()

    def disconnect_electricity(self):
        self.pss.power_off()

def add_workers():
    worker1 = Worker("Jenya", "Taylor", "guard")
    worker2 = Worker("Zoya", "Wind", "guard")
    worker3 = Worker("Feydor", "Red", "plumber")
    worker4 = Worker("Alexander", "Black", "electrician")
    worker5 = Worker("Mal", "Grey", "cleaner")
    worker6 = Worker("Kaz", "Water", "cleaner")
    worker7 = Worker("Nina", "Spy", "cleaner")
    worker8 = Worker("Alina", "Light", "dispatcher")
    return worker1, worker2, worker3, worker4, worker5, worker6, worker7, worker8

print("     Entering DEVELOPER mode . . .")
print("Enter data for your building, 0 for default, 1 for manual")
choice = int(input())
if choice == 0:
    number_buildings = 2
    apart_type1 = 10
    apart_type2 = 10
    developer = Developer(number_buildings, apart_type1, apart_type2)
    ac = ApartmentComplex(number_buildings)
    a_1 = [Apartment(1, 33, 3, 6, 22, i+1) for i in range(10)]
    a_2 = [Apartment(2, 55, 3, 6.5, 23, i+1) for i in range(10)]
    building_info = [1, 24, 3.2, 1.7, 2000, 20]
    ac.change_state_ex(developer.type1, developer.type2, a_1, a_2, building_info)
    for i in range(2):
        ac.apart_buildings[i] = ApartmentBuilding(10, 10, a_1, a_2, building_info)
        ac.set_building_state(i)
        print("Building`s #", i+1, "state is:", ac.apart_buildings[i].state)

    print("Buildings successfully put into operation! Now starting systems . . .")
    developer.put_into_operation()
    ac.connect_electricity()

if choice == 1:
    print("Hi, Developer, how many buildings?")
    number_buildings = input()
    print("How many one-room apartment?")
    apart_type1 = input()
    print("How many two-room apartment?")
    apart_type2 = input()
    developer = Developer(number_buildings, apart_type1, apart_type2)

    ac = ApartmentComplex(number_buildings)

    developer.apart_info_input()
    developer.building_info_input()
    while not ac.check_requirements(developer):
        developer.apart_info_input()
        developer.building_info_input()

    a_1, a_2 = developer.give_aparts_info()
    building_info = developer.give_building_info()
    ac.change_state_ex(developer.type1, developer.type2, a_1, a_2, building_info)
    for i in range(int(number_buildings)):
        ac.apart_buildings[i] = ApartmentBuilding(apart_type1, apart_type2, a_1, a_2, building_info)
        ac.set_building_state(i)
        print("Building`s #", i + 1, "state is:", ac.apart_buildings[i].state)
    print("Buildings successfully put into operation! Now starting systems . . .")
    developer.put_into_operation()
    ac.connect_electricity()

print("     Entering APARTMENT MANAGEMENT mode . . .")
am = ApartmentManagment()

manag_menu = 0
print("""Here is the menu:
      Press 0 to leave menu
      Press 1 to add workers
      Press 2 to employ workers
      Press 3 to install alarm
      Press 4 to turn alarm on
      Press 5 to turn alarm off
      Press 6 to list workers
      Press 7 to dismiss a worker
      Press 8 to give worker a password
      Press 9 to take worker`s password
      (take notice that it`s not possible to dismiss workers until you employ them!)"""
      )
while True:
    workers = add_workers()
    manag_menu = int(input("Enter desirable option:"))
    if manag_menu == 1:
        workers = add_workers()
    elif manag_menu == 2:
        for i in range(len(workers)):
            am.employ_worker(workers[i])
    elif manag_menu == 3:
        am.install_alarm()
    elif manag_menu == 4:
        am.turn_on_alarm()
    elif manag_menu == 5:
        am.turn_off_alarm()
    elif manag_menu == 6:
        am.list_workers()
    elif manag_menu == 7:
        print("Enter first name:")
        f_n = input()
        print("Enter second name:")
        s_n = input()
        print("Enter speciality:")
        sp = input()
        am.dismiss_worker(f_n, s_n, sp)
    elif manag_menu == 8:
        am.provide_pass()
    elif manag_menu == 9:
        am.take_pass()
    elif manag_menu == 0:
        break

print("     Entering INHABITANT mode . . .")
print("""Here is the menu:
      Press 0 to leave menu
      Press 1 to add inhabitant
      Press 2 to give inhabitant a password
      Press 3 to take inhabitant`s password
      Press 4 to list inhabitants
      Press 5 to buy an apartment
      Press 6 to sell an apartment
      Press 7 to call stuff
      """)
inhab_menu = 0
while True:
    inhab_menu = int(input("Enter desirable option:"))
    if inhab_menu == 1:
        print("Enter new inhabitant`s data:")
        print("Enter first name:")
        f_name = input()
        print("Enter second name:")
        s_name = input()
        inhabitant = Inhabitant(f_name, s_name)
        am.add_inhabitants(inhabitant)
    elif inhab_menu == 2:
        am.provide_inhab_pass()
    elif inhab_menu == 3:
        am.take_inhab_pass()
    elif inhab_menu == 4:
        am.list_inhabitants()
    elif inhab_menu == 5:
        print("Enter inhabitant's id to buy an apartment:")
        i = int(input()) - 1
        print("Enter building`s number, available are from 1 to", number_buildings)
        n = int(input())
        print("How many rooms? 1 or 2?")
        rooms = int(input())
        if rooms == 1:
            print("Enter flat`s, available are from 1 to", apart_type1)
            apart_type1 = int(input())
            apart_type2 = 0
        if rooms == 2:
            print("Enter flat`s, available are from 1 to", apart_type2)
            apart_type2 = int(input())
            apart_type1 = 0
        am.inhabitants[i].buy_apartment(number_buildings, apart_type1, apart_type2, rooms)
    elif inhab_menu == 6:
        am.list_inhabitants()
    elif inhab_menu == 7:
        am.stuff_call()
    elif manag_menu == 0:
        break