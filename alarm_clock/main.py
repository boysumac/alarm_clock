from alarm_clock import alarmclock

my_clock = alarmclock()
print(f"The current time is: {my_clock.time}")
print(f"The current alarm is set at: {my_clock.alarm}")
my_clock.set_time("1900")
my_clock.set_alarm ("0700")

my_clock.toggle_alarm()
my_clock.toggle_alarm()


 