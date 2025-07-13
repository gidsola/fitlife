
# import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User
    # from src.activityManager import ActivityManager
from src.deviceManager import DeviceManager

class FitnessTracker:
    def __init__(self, user: 'User'):
        self.user = user
        self.device_manager = DeviceManager(self)

#########################
#  Need to re-factor all this also..

    # def trackActivity(self, activity_type, duration, calories_burned, date, source="manual"):
    #     activity = self.user.activity_manager.createActivity(
    #         activity_id=len(self.user.activity_manager.activities) + 1,
    #         activity_type=activity_type,
    #         duration=duration,
    #         calories_burned=calories_burned,
    #         date=date
    #     )
    #     self.user.activity_manager.trackActivity(activity, source)
    #     print(f"Tracked {activity_type} activity: {duration} minutes, {calories_burned} calories burned")

    # def sync_with_device(self, device_data):
    #     for activity_data in device_data:
    #         try:
    #             activity = self.user.activity_manager.createActivity(
    #                 activity_id=activity_data['activity_id'],
    #                 activity_type=activity_data['activity_type'],
    #                 duration=activity_data['duration'],
    #                 calories_burned=activity_data['calories_burned'],
    #                 date=activity_data['date']
    #             )
    #             self.user.activity_manager.trackActivity(activity, source="device")
    #         except KeyError as e:
    #             print(f"Missing data in device sync: {e}")
    #     print("Synced with device successfully")
