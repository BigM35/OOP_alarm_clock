


class Alarm_Clock:
    def __init__(self, time, alarm_status, time_alarm_is_set_to):
        self.current_time = time
        self.is_alarm_on = alarm_status
        self.alarm_set_to = time_alarm_is_set_to
    
    def set_current_time(self, inputed_time):
        self.current_time = inputed_time
        return self.current_time
    


