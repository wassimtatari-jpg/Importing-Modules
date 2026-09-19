from datetime import datetime
class Event:
    def __init__(self,name):
        self.name=name
        self.event_date=None
    def set_event_date(self,date):
        self.event_date=datetime.strptime(date,"%d.%m.%Y")
    def is_event_passed(self,current_date):
        self.current_date=datetime.strptime(current_date,"%d.%m.%Y")
        if self.event_date<self.current_date:
            return True
        else:
            return False
event = Event("Python Workshop")

event.set_event_date("15.09.2026")

print(event.is_event_passed("19.09.2026"))

        