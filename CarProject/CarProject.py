# Bryce Housholder
# Python Script which pulls data from the ODB-ii port on my 2017 Toyota Rav4
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CarProject/ODBii CSV Test 2.csv',delimiter=';',usecols=[0,1,2,3])
# Fix seconds values
df.eval("SECONDS = SECONDS - SECONDS[0]",inplace= True)
#Calculate Time Steps
startSeconds = df.at[0,'SECONDS']
endSeconds = df.at[df.index[-1],'SECONDS']
totalSeconds = round(endSeconds - startSeconds,2)
totalMins = round(totalSeconds/60,2)
# Sort and total trip distance in miles 
sortedDistance = df[(df['PID'] == 'Distance travelled') & (df['VALUE'].notnull() )] 
sortedDistanceValues = sortedDistance['VALUE'] # miles
sortedDistanceMins = df.loc[(sortedDistance.index, 'SECONDS')] / 60 # mins
totalDistance = round((sortedDistance.iloc[-1]['VALUE']),2) # miles

# plot Distance [Miles]/ Time [Min]
plt.plot(sortedDistanceMins,sortedDistanceValues)
plt.title('Distance Driven During Trip')
plt.xlabel('Minutes')
plt.ylabel('Miles')
plt.show()

# Instantaneous MPH calculation 
#Hours = df['SECONDS'] / 3600
#distanceDiff = sortedDistanceValues.diff()
#distanceDiff = distanceDiff.fillna(0)
#timeDiff = Hours.diff()
#timeDiff = timeDiff.fillna(0)
#InstantMPH = distanceDiff / timeDiff
#InstantMPH.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
#print(MPH)
#plt.plot(InstantMPH)
#plt.show()




    



