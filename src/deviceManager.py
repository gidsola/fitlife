


############################
#
#  Need to refactor everything.. (after hand in.. :p)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.fitnessTracker import FitnessTracker
from src.smartwatch import Smartwatch

class DeviceManager:
    def __init__(self, fitnessTracker: 'FitnessTracker'):
        self.fitnessTracker = fitnessTracker
        
        #move/redo this stuff
        # self.fitness_tracker = FitnessTracker(device_manager_id)

    # def sync_with_fitness_tracker(self, device_data):
    #     print("Syncing with fitness tracker")
    #     self.fitness_tracker.sync_with_device(device_data)

    # def sync_with_smartwatch(self, device_data):
    #     print("Syncing with smartwatch")
    #     self.fitness_tracker.sync_with_device(device_data)
