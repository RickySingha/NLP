minute = 42
sec = 42
totalSeconds = minute*60 + sec
hour  = totalSeconds/(60*60)
totalMin = minute + sec/60
km = 10
kmInMile = 1.61
totalMile = (1/kmInMile)*km

averagePace  = totalMin/totalMile
averageSpeed = totalMile/hour
print(f"Average pace is {averagePace} minutes per mile")
print(f"Average Speed is {averageSpeed} miles per hour")