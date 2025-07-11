


############################
#
#  Need to refactor everything.. (after hand in.. :p)


from src.fitnessTracker import FitnessTracker
from src.smartwatch import Smartwatch

class DeviceManager:
    def __init__(self, fitnessTracker: FitnessTracker):
        self.fitnessTracker = fitnessTracker
        
        #move/redo this stuff
        # self.fitness_tracker = FitnessTracker(device_manager_id)

    # def sync_with_fitness_tracker(self, device_data):
    #     print("Syncing with fitness tracker")
    #     self.fitness_tracker.sync_with_device(device_data)

    # def sync_with_smartwatch(self, device_data):
    #     print("Syncing with smartwatch")
    #     self.fitness_tracker.sync_with_device(device_data)

        
        
        
def showSyncMenu():
    while True:
            print("\n1. Sync Fitness Tracker\n2. Sync Smartwatch")
            sub = input("Select: ")

            if sub == "1":
                brand = input("Tracker brand: ")
                model = input("Tracker model: ")
                tracker = FitnessTracker(tracker_id=1)
                DeviceManager.sync_with_fitness_tracker(tracker)
                print(f"Synced with fitness tracker: {tracker.brand} {tracker.model}")

            elif sub == "2":
                brand = input("Smartwatch brand: ")
                model = input("Smartwatch model: ")
                watch = Smartwatch(watch_id=1, brand=brand, model=model)
                DeviceManager.sync_with_smartwatch(watch)
                print(f"Synced with smartwatch: {watch.brand} {watch.model}")

            input("Press Enter to continue...")