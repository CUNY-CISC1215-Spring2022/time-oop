
# This file demonstrates an objet-oriented approach for managing
# a Time class.

def seconds_to_time(s):
    """Convert a number of seconds to a Time object"""
    seconds = s
    minutes = seconds // 60 
    seconds = seconds % 60 
    hours = minutes // 60 
    minutes = minutes % 60

    return Time(hours, minutes, seconds)


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        """Create a new Time object"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        """Print a human-readable version of ourselves."""
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __gt__(self, other):
        """
            Determine if one Time object comes after another.
            Returns True if this object comes after other, and False
            if this object and other are equal or if this object comes
            after other.
        """
        print("gt", self)
        t1_seconds = self.to_seconds()
        t2_seconds = other.to_seconds()

        return t1_seconds > t2_seconds

    def __ge__(self, other):
        """
            Determine if one Time object comes after another.
            Returns True if this object comes after other, and False
            if this object and other are equal or if this object comes
            after other.
        """
        print("gt", self)
        t1_seconds = self.to_seconds()
        t2_seconds = other.to_seconds()

        return t1_seconds >= t2_seconds
    
    def increment(self, seconds):
        """
            Increment ourselves.
            This method returns a new Time object containing
            our time incremented by the given number of seconds.
        """
        seconds_t = self.to_seconds()
        return seconds_to_time(seconds_t + seconds)

    def __add__(self, other):
        """
            Add two Time objects together. This method returns
            a new Time object containing the sum of ourselves and other.
        """
        seconds_1 = self.to_seconds()

        if isinstance(other, Time):
            seconds_2 = other.to_seconds()
        else:
            seconds_2 = other

        return seconds_to_time(seconds_1 + seconds_2)
    
    def __radd__(self, other):
        return self.__add__(other)

    def to_seconds(self):
        """Convert ourselves to seconds"""
        seconds = self.seconds
        seconds += self.minutes * 60
        seconds += self.hours * 60 * 60

        return seconds


t1 = Time(10, 0, 0)
t2 = Time(0, 3, 10)
t3 = Time(minutes=10)

print(10 + t1)