from alarm_clock import Alarm_Clock


alarm_clock = Alarm_Clock("13:00", True,"17:00")

print(alarm_clock.current_time)

alarm_clock.current_time.set_current_time(1500)
print(alarm_clock.current_time)