"""
module to calculate the angle between clock arms
given the time
"""

class Clock:
    """class to hold the attributes of clock class
    """

    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def calculate_angle(self):
        """
        calculate the angle between the hour and minute hand
        """
        hour_angle = (self.hours % 12 + self.minutes / 60) * (360 / 12)
        minute_angle = (self.minutes / 60) * 360
        angle = abs(hour_angle - minute_angle)
        return angle
