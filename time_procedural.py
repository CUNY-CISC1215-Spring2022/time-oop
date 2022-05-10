# This file demonstrates a procedural approach for managing
# a Time class.

# We will manage all attributes and functionality of the class
# externally, so the class is empty.
class Time:
    pass


def time_to_seconds(t):
    """Convert a Time object to seconds."""
    seconds = t.seconds
    seconds += t.minutes * 60
    seconds += t.hours * 60 * 60

    return seconds

def seconds_to_time(s):
    """Convert a number of seconds to a Time object"""
    result = Time()

    result.seconds = s 
    result.minutes = result.seconds // 60 
    result.seconds = result.seconds % 60 
    result.hours = result.minutes // 60 
    result.minutes = result.minutes % 60

    return result

def add_time(t1, t2):
    """
        Add two Time objects together. This function returns
        a new Time object containing the sum of t1 and t2.
    """
    seconds_1 = time_to_seconds(t1)
    seconds_2 = time_to_seconds(t2)

    return seconds_to_time(seconds_1 + seconds_2)


def increment(t, seconds):
    """
        Increment a Time object.
        This function returns a new Time object containing
        the time from t incremented by the given number of seconds.
    """
    seconds_t = time_to_seconds(t)
    return seconds_to_time(seconds_t + seconds)

def is_after(t1, t2):
    """
        Determine if one Time object comes after another.
        Returns True if t1 comes after t2, and False
        if t1 and t2 are equal or if t2 comes after t1.
    """
    t1_seconds = time_to_seconds(t1)
    t2_seconds = time_to_seconds(t2)

    return t1_seconds > t2_seconds


def print_time(t):
    """Print a human-readable version of a given Time object."""
    print(f"{t.hours}:{t.minutes}:{t.seconds}")

t1 = Time()
t1.hours = 10
t1.minutes = 0

t2 = Time()
t2.hours = 0
t2.minutes = 3
t2.seconds = 10

print("t1")
print_time(t1)

print()
print("t2")
print_time(t2)

print()
print("Is t1 after t2?", is_after(t1, t2))

print()
print("add_time(t1, t2)")
print_time(add_time(t1, t2))

print()
print("increment(t1, 100)")
print_time(increment(t1, 100))