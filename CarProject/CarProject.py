# Bryce Housholder
# Python Script which pulls data from the ODB-ii port on my 2017 Toyota Rav4
import pandas as pd
import matplotlib as plt

df = pd.read_csv('CarProject/ODBii CSV Test 1.csv',delimiter=';',usecols=[0,1,2,3])
#print(df.head(5))

#Calculate Time Steps
startSeconds = df.at[0,'SECONDS']
endSeconds = df.at[df.index[-1],'SECONDS']
totalSeconds = round(endSeconds - startSeconds,2)
totalMins = round(totalSeconds/60,2)

# Calculate total distance travelled
distance = df['PID'] == 'Distance Travelled'
for 
if df['PID']=='Distance Travelled':


#totalDistance = df[distance]['VALUES'].sum()
#print(totalDistance)
print(distance)

#groupedDistance = df.groupby(['PID','Distance Travelled'])