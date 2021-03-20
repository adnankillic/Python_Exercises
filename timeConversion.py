# Given a time in 12 -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


def timeConversion(s):
    hour = int(s[0:2])
    
    if "AM" in s:
        if hour == 12:
            hour = "00"
            s = hour + s[2:-2]
            return s
        else:
            return s.replace("AM","")
    else:
        if hour == 12:
            return s.replace("PM","")
        else:
            hour += 12
            return str(hour) + s[2:-2]

result= timeConversion("07:05:45PM")
print(result)