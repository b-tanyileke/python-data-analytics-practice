MINUTES_PER_HOUR = 60
video_count = int(input("Number of videos: "))
average_minutes = float(input("Average minutes per video: "))
total_minutes = video_count * average_minutes
total_hours = total_minutes / MINUTES_PER_HOUR
print("Total study time: " + format(total_minutes, ".1f") + " minutes")
print("Total study time: " + format(total_hours, ".1f") + " hours")
