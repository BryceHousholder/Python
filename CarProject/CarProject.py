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
#plt.plot(sortedDistanceMins,sortedDistanceValues)
#plt.title('Distance Driven During Trip')
#plt.xlabel('Minutes')
#plt.ylabel('Miles')
#plt.show()

# Vehicle Speed Calculation
sortedSpeed = df[(df['PID'] == 'Vehicle speed') & (df['VALUE'].notnull() )] 
sortedSpeedValues = sortedSpeed['VALUE'] # MPH
sortedSpeedMins = df.loc[(sortedSpeed.index, 'SECONDS')] / 60 # mins
# Vehicle Speed Plot
#plt.plot(sortedSpeedMins,sortedSpeedValues)
#plt.title('Instant MPH During Trip')
#plt.xlabel('Minutes')
#plt.ylabel('MPH')
#plt.show()

# MPH and Distance Plot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

ax1.plot(sortedDistanceMins, sortedDistanceValues, color='blue')
ax1.set_title('Distance Driven During Trip')
ax1.set_xlabel('Minutes')
ax1.set_ylabel('Miles')

ax2.plot(sortedSpeedMins, sortedSpeedValues, color='red')
ax2.set_title('Instant MPH During Trip')
ax2.set_xlabel('Minutes')
ax2.set_ylabel('MPH')
plt.tight_layout()
plt.show()

# Fuel Used
sortedFuelUsed = df[(df['PID'] == 'Fuel used') & (df['VALUE'].notnull() )] 
sortedFuelUsedValues = sortedFuelUsed['VALUE'] # [Gallons]
totalFuelUsed = round((sortedFuelUsed.iloc[-1]['VALUE']),2)
# Plot Fuel Used4
plt.plot(sortedDistanceMins,sortedFuelUsedValues)
plt.title('Fuel Used During Trip')
plt.xlabel('Mins')
plt.ylabel('Gallons')
plt.show()
# Calculate total cost of trip
pricePerGallon = input('What was the cost per gallon the last time you filled up? $')
pricePerGallon = float(pricePerGallon)
costOfTrip = round(pricePerGallon * totalFuelUsed,2)
print('The total cost of your trip was $',costOfTrip)

# Throttle Position
sortedTPosition = df[(df['PID'] == 'Throttle position') & (df['VALUE'].notnull() )] 
sortedTPositionValues = sortedTPosition['VALUE'] # 

