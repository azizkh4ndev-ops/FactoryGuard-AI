# synthetic data generator

import numpy as np
import pandas as pd
np.random.seed(42)

#paramters as per our project

num_machines=500
hours= 24 * 30    #30 days of hourly data
failure_rate = 0.008  # <1% of failure

data=[]

#normal sensor readings

for machine in range(num_machines):
    temperature = np.random.normal(70,5,hours)
    vibration = np.random.normal(0.5,0.1,hours)
    pressure = np.random.normal(30,3,hours)
    
    failure=np.zeros(hours) #initialize failure columns
    

#calculate failures as per our convenience

num_failures = int(hours * failure_rate) 
failure_indices = np.random.choice(range(24,hours),num_failures, replace=False)
# we leave first 24 hours safe
# we need 24 hours before failure to modify sensore



for idx in failure_indices:
    failure[idx]=1 #marking failure at 1
    

temperature[idx-24:idx] += np.linspace(2,10,24) #creates 24 numbers b/w 2 and 10
vibration[idx-24:idx] += np.linspace(0.05,0.3,24)
pressure[idx-24:idx] += np.linspace(1,5,24)

# creates hourly timestamps 

timestamps = pd.date_range(
    start="2025-01-01", periods=hours
)


machine_df = pd.DataFrame({
    "timestamp": timestamps,
    "machine_id": machine,
    "temperature": temperature,
    "vibration": vibration,
    "pressure": pressure,
    "failure": failure
})

data.append(machine_df)
df=pd.concat(data) #combined 500 machines into one data set

df.to_csv("synthetic_data", index=False)