
class alarmclock:
    def __init__(self):
        self.time = "1700"
        self.alarm = "1700"
        self.alarm_on = False

    def set_alarm(self,new_alarm):
        self.alarm = new_alarm
        print(f"Alarm time is now at: {self.alarm}")

    def set_time(self, new_time):
        self.time = new_time
        print (f"The current time is: {self.time}")

    def toggle_alarm(self):
        self.alarm_on = not self.alarm_on
        if self.alarm_on:
            print("Alarm is now on")
        else:
            print("Alarm is now off")


