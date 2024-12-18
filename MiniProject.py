import pickle

class vehicle:
    def __init__(self, type, vehicleName, driverName, vehicleNumber, maxPassengers, AC, size, maxLoad, status):
        self.type = type
        self.vehicleName = vehicleName
        self.driverName = driverName
        self.vehicleNumber = vehicleNumber
        self.maxPassengers = maxPassengers
        self.AC = AC
        self.status = status
        self.size = size
        self.maxLoad = maxLoad

    def setStatus(self, status):
        self.status = status

    def Type(self):
        return self.type

    def VehicleName(self):
        return self.vehicleName

    def VehicleNumber(self):
        return self.vehicleNumber

    def DriverName(self):
        return self.driverName

    def MaxPassengers(self):
        return self.maxPassengers

    def Ac(self):
        return self.AC

    def Status(self):
        return self.status

    def Size(self):
        return self.size

    def MaxLoad(self):
        return self.maxLoad

    def showCV(self):
        print('\n'+self.vehicleName)
        print(self.vehicleNumber)
        print(self.driverName)

class vehiclesManager:
    vehicles = []
    def __init__(self):
        try:
            pickle_in = open("vehicles.pickle", "rb")
            self.vehicles = pickle.load(pickle_in)
        except:
            self.update()

    def add(self, type, vehicleName, maxPassengers, AC, driverName, vehicleNumber, size, maxLoad):
        self.vehicles.append(vehicleName)
        self.vehicles[-1] = vehicle(type, vehicleName, driverName, vehicleNumber, maxPassengers, AC, size, maxLoad, True)
        self.update()
        print("\nVehicle successfully added.\n")
        return 1

    def remove(self, vehicleName):
        for v in self.vehicles:
            if v.VehicleName() == vehicleName:
                del self.vehicles[self.vehicles.index(v)]
                self.update()
                print('\nVehicle is successfully removed from the system.')
                return 1
        print('\nPlease enter valid vehicle name.\n')
        return 0

    def Assignjob(self, type, maxPassengers, AC, size, maxLoad):
        for v in self.vehicles:
            if v.Type() == type and v.MaxPassengers() == maxPassengers and v.Ac() == AC and v.Status() == True and v.Size() == size and v.MaxLoad() == maxLoad:
                self.vehicles[self.vehicles.index(v)].showCV()
                self.vehicles[self.vehicles.index(v)].setStatus(False)
                #self.vehicles[self.vehicles.index(v)] = vehicle(type, v.vehicleName, v.driverName, v.vehicleNumber, maxPassengers, AC, v.size, v.maxLoad, False)
                self.update()
                print('\nAssigned the job.\n')
                return 1
        print('\nNo vehicle available what you want right now.')
        return 0

    def Releasejob(self, vehicleName):
        for v in self.vehicles:
            if v.VehicleName() == vehicleName and v.Status() == False:
                type = v.Type()
                vehicleNumber = v.VehicleNumber()
                driverName = v.DriverName()
                maxPassengers = v.MaxPassengers()
                AC = v.Ac()
                size = v.Size()
                maxLoad = v.MaxLoad()
                del self.vehicles[self.vehicles.index(v)]
                self.vehicles.append(vehicleName)
                self.vehicles[-1] = vehicle(type, vehicleName, driverName, vehicleNumber, maxPassengers, AC, size, maxLoad, True)
                self.update()
                print('\nReleased from the job')
                return 1
        print('\nPlease enter valid vehicle name.\n')
        return 0



    def availableVehicles(self, type, maxPassengers, AC, size, maxLoad):
        c = 0
        for v in self.vehicles:
            if v.Type() == type and v.Status() == True and v.MaxPassengers() == maxPassengers and v.Ac() == AC and v.Size() == size and v.MaxLoad() == maxLoad:
                print(self.vehicles[self.vehicles.index(v)].VehicleName())
                c = c + 1
        if c > 0:
            return 1
        else:
            print('\n              No vehicle available in this category right now\n')
            return 0

    def update(self):
        pickle_out = open("vehicles.pickle","wb")
        pickle.dump(self.vehicles, pickle_out)
        pickle_out.close()

VM = vehiclesManager()

def setType():
    while True:
        type = input('\nWhich category do you want? \n (Enter Car / Van / 3 Wheeler / Truck / Lorry / H for Home):- ').lower()
        if type == 'car' or type == 'van' or type == '3 wheeler' or type == 'truck' or type == 'lorry':
            return type
        elif type == 'h':
            start()
        else:
            print('\nEnter valid input')

def setMaxPassengers(type):
    if type == 'car':
        while True:
            maxPassenger = input('\nMaximum number of passengers \n (Enter 3 / 4 / H for Home):- ')
            if maxPassenger == '3' or maxPassenger == '4':
                maxPassenger = int(maxPassenger)
                return maxPassenger
            elif maxPassenger == 'h':
                start()
            else:
                print('\nEnter valid input')
    elif type == 'van':
        while True:
            maxPassenger = input('\nMaximum number of passengers \n (Enter 6 / 8 / H for Home):- ')
            if maxPassenger == '6' or maxPassenger == '8':
                maxPassenger = int(maxPassenger)
                return maxPassenger
            elif maxPassenger == 'h':
                start()
            else:
                print('\nEnter valid input')

def setAC():
    while True:
        AC = input('\nAC type \n (Enter AC / Non AC / H for Home):- ').lower()
        if AC == 'ac' or AC == 'non ac':
            return AC
        elif AC == 'h':
            start()
        else:
            print('\nEnter valid input')

def setSize():
    while True:
        size = input('\nSize \n (Enter 7 / 12 / H for Home):- ')
        if size == '7' or size == '12':
            size =int(size)
            return size
        elif size == 'h':
            start()
        else:
            print('\nEnter valid input')

def setMaxLoad():
    while True:
        maxLoad = input('\nMax Load (kg) \n (Enter 2500 / 3500 / H for Home):- ')
        if maxLoad == '2500' or maxLoad == '3500':
            maxLoad = int(maxLoad)
            return maxLoad
        elif maxLoad == 'h':
            start()
        else:
            print('\nEnter valid input')

def Details():
    print('\n    Cars')
    print('            maximum number of passengers - 3 and 4')
    print('            AC/ Non AC')
    print('\n    Vans')
    print('            maximum number of passengers - 6 and 8')
    print('            AC/ Non AC')
    print('\n    3 Wheeler')
    print('            maximum number of passengers - 3')
    print('\n    Trucks')
    print('            Size – 7 ft and 12 ft')
    print('\n    Lorries')
    print('            Max load and size - 2500kg and 3500kg')

def Assign():
    type = False
    maxPassengers = False
    AC = False
    size = False
    maxLoad = False

    print('_____________Vehicle Details for Assign_____________')
    Details()

    type = setType()
    if type == 'car' or type == 'van':
        maxPassengers = setMaxPassengers(type)
        AC = setAC()
    elif type == 'trucks':
        size = setSize()
    elif type == 'lorry':
        maxLoad = setMaxLoad()
    else:
        maxPassengers = 3

    VM.Assignjob(type, maxPassengers, AC, size, maxLoad)

def Add():
    type = False
    maxPassengers = False
    AC = False
    size = False
    maxLoad = False
    vehicleName = False
    driverName = False
    vehicleNumber = False

    print('_____________Vehicle Details for Add_____________')
    Details()


    vehicleName = input('\nEnter Name for Vehicle:- ')
    driverName = input('\nEnter Driver Name:- ')
    vehicleNumber = input('Enter Vehicle Number:- ')

    type = setType()
    if type == 'car' or type == 'van':
        maxPassengers = setMaxPassengers(type)
        AC = setAC()
    elif type == 'truck':
        size = setSize()
    elif type == 'lorry':
        maxLoad = setMaxLoad()
    else:
        maxPassengers = 3

    result = VM.add(type, vehicleName, maxPassengers, AC, driverName, vehicleNumber, size, maxLoad)

def Remove():
    vehicleName = input('\nEnter Vehicle Name for remove or H for Home:- ')
    if vehicleName == 'h' or vehicleName == 'H':
        start()
    else:
        result = VM.remove(vehicleName)

def Release():
    vehicleName = input('\nEnter Vehicle Name for Release Job or H for Home:- ')
    if vehicleName == 'h' or vehicleName == 'H':
        start()
    else:
        result = VM.Releasejob(vehicleName)

def app(index):
    if index == 'get' or index == 'assign':
        Assign()
    elif index == '?':

        print('\nAvailable Cars Name-list of Max.No.ofPssengers-3  AC')
        VM.availableVehicles('car', 3, 'ac', False, False)
        print('\nAvailable Cars Name-list of Max.No.ofPssengers-3  Non AC')
        VM.availableVehicles('car', 3, 'non ac', False, False)
        print('\nAvailable Cars Name-list of Max.No.ofPssengers-4  AC')
        VM.availableVehicles('car', 4, 'ac', False, False)
        print('\nAvailable Cars Name-list of Max.No.ofPssengers-4  Non AC')
        VM.availableVehicles('car', 4, 'non ac', False, False)

        print('\nAvailable Vans Name-list of Max.No.ofPssengers-6  AC')
        VM.availableVehicles('van', 6, 'ac', False, False)
        print('\nAvailable Vans Name-list of Max.No.ofPssengers-6  Non AC')
        VM.availableVehicles('van', 6, 'non ac', False, False)
        print('\nAvailable Vans Name-list of Max.No.ofPssengers-8  AC')
        VM.availableVehicles('van', 8, 'ac', False, False)
        print('\nAvailable Vans Name-list of Max.No.ofPssengers-8  Non AC')
        VM.availableVehicles('van', 8, 'non ac', False, False)

        print('\nAvailable 3 Wheelers Name-list')
        VM.availableVehicles('3 wheeler', 3, False, False, False)

        print('\nAvailable Trucks Name-list of Size – 7 ft')
        VM.availableVehicles('truck', False, False, 7, False)
        print('\nAvailable Trucks Name-list of Size – 12 ft')
        VM.availableVehicles('truck', False, False, 12, False)

        print('\nAvailable Lorries Name-list of size - 2500kg')
        VM.availableVehicles('lorry', False, False, False, 2500)
        print('\nAvailable Lorries Name-list of size - 3500kg')
        VM.availableVehicles('lorry', False, False, False, 3500)
    elif index == 'add':
        Add()
    elif index == 'remove':
        Remove()
    elif index == 'release':
        Release()

def customer():
    while True:
        print('**********Welcome**********')
        print('  inputs   \t            Description')
        print('    get    \t   for Get vehicle (hire)')
        print('     ?     \t   for See available vehicles in each category')
        print('     H     \t   for go to home')
        inp = input('\nEnter here:-').lower()
        if inp == 'h':
            start()
        elif inp == 'get' or inp == '?':
            app(inp)
        else:
            print('\nEnter Valid input.......')

def adminR():
    while True:
        print('**********Welcome**********')
        print('  inputs   \t            Description')
        print('   Add     \t   for Add a new vehicle to the system')
        print('  Remove   \t   for Remove a vehicle from the system')
        print('  Assign   \t   for Assign a job (hire)')
        print('  Release  \t   for Release form assigned job (hire) after completing')
        print('     ?     \t   for See available vehicles in each category')
        print('     H     \t   for go to home')
        inp = input('\nEnter here:-').lower()
        if inp == 'h':
            start()
        elif inp == 'add' or inp == 'remove' or inp == 'assign' or inp == 'release' or inp == '?':
            app(inp)
        else:
            print('\nEnter Valid input.......')

def admin():
    while True:
        print('Enter  \'H\'  for go home')
        u = input("Enter user name:- ")
        if u == 'H' or u == 'h':
            start()
        p = input("Enter password:- ")
        if u == 'H' or u == 'h':
            start()
        elif u!='admin' or p!='admin':
            print('User name or/and password is/are wrong.')
            print('Mock user name:- admin')
            print('Mock password:- admin')
        else:
            adminR()

def start():
    while True:
        user = input('Who are you? (user/admin):- ').upper()
        if user == 'USER':
            customer()
        elif user == 'ADMIN':
            admin()
        else:
            print('Enter valid input')

start()