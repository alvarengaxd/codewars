def make_readable(seconds):
    if seconds < 60:
        return f"00:00:{seconds:02d}"
    elif 3600 > seconds >= 60:
        min = seconds // 60
        sec = seconds % 60
        return f"00:{min:02d}:{sec:02d}"
    elif 360000 > seconds >= 3600:
        hour = seconds // 3600
        min = (seconds % 3600) // 60
        sec = (seconds - (hour*3600) - (min * 60))
        return f"{hour:02d}:{min:02d}:{sec:02d}"

print(make_readable(0)) #00:00:00
print(make_readable(5)) #00:00:05
print(make_readable(60)) #00:01:00
print(make_readable(86399)) #23:59:59
print(make_readable(359999)) #99:59:59

'''
most voted solution

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
'''