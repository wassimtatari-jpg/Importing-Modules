from datetime import datetime

class Sleep:
    def __init__(self,person):
        self.person=person
        self.sleep_time=None
    def set_sleep_time(self,sleep_time):
        self.sleep_time=datetime.strptime(sleep_time,"%H:%M")
    def is_early_sleep(self,target_time):
        self.target_time=datetime.strptime(target_time,"%H:%M")
        if self.sleep_time<=self.target_time:
            return True
        else:
            return False
        
sleep = Sleep("Mohamed")

sleep.set_sleep_time("21:30")

print(sleep.is_early_sleep("22:00"))
        