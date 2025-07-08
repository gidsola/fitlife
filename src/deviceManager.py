


class DeviceManager:
    def __init__(self, device_manager_id):
        self.device_manager_id = device_manager_id

    def sync_with_fitness_tracker(self, fitness_tracker):
        print(f"Syncing with fitness tracker: {fitness_tracker.brand} {fitness_tracker.model}")

    def sync_with_smartwatch(self, smartwatch):
        print(f"Syncing with smartwatch: {smartwatch.brand} {smartwatch.model}")