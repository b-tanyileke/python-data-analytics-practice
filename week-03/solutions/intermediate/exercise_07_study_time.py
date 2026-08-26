""" Exercise 07 - Sample Solution """

MINUTES_PER_HOUR = 60
video_count = int(input("Number of videos: "))
average_minutes = float(input("Average minutes per video: "))
total_minutes = video_count * average_minutes
total_hours = total_minutes / MINUTES_PER_HOUR
print("Total time in minutes: " + format(total_minutes, ".1f"))
print("Total time in hours: " + format(total_hours, ".1f"))
