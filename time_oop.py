
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
    def __init__(self, hours, minutes, seconds):
        """Create a new Time object"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def print_time(self):
        """Print a human-readable version of ourselves."""
        print(f"{self.hours}:{self.minutes}:{self.seconds}")

    def is_after(self, other):
        """
            Determine if one Time object comes after another.
            Returns True if this object comes after other, and False
            if this object and other are equal or if this object comes
            after other.
        """
        t1_seconds = self.to_seconds()
        t2_seconds = other.to_seconds()

        return t1_seconds > t2_seconds
    
    def increment(self, seconds):
        """
            Increment ourselves.
            This method returns a new Time object containing
            our time incremented by the given number of seconds.
        """
        seconds_t = self.to_seconds()
        return seconds_to_time(seconds_t + seconds)

    def add_time(self, other):
        """
            Add two Time objects together. This method returns
            a new Time object containing the sum of ourselves and other.
        """
        seconds_1 = self.to_seconds()
        seconds_2 = other.to_seconds()

        return seconds_to_time(seconds_1 + seconds_2)

    def to_seconds(self):
        """Convert ourselves to seconds"""
        seconds = self.seconds
        seconds += self.minutes * 60
        seconds += self.hours * 60 * 60

        return seconds


t1 = Time(10, 0, 0)
t2 = Time(0, 3, 10)

print("t1")
t1.print_time()

print()
print("t2")
t2.print_time()

print()
print("Is t1 after t2?", t1.is_after(t2))

print()
print("t1.add_time(t2)")
t1.add_time(t2).print_time()

print()
print("t1.increment(100)")
t1.increment(100).print_time()