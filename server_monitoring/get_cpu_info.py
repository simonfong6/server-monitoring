import json
import os
import subprocess
import re

statistics = {}

# Get Physical and Logical CPU Count
physical_and_logical_cpu_count = os.cpu_count()
statistics['physical_and_logical_cpu_count'] = physical_and_logical_cpu_count
"""
# Load average 
# This is the average system load calculated over a given period of time of 1, 5 and 15 minutes.
# In our case, we will show the load average over a period of 15 minutes.

# The numbers returned by os.getloadavg() only make sense if
# related to the number of CPU cores installed on the system.

# Here we are converting the load average into percentage. The higher the percentage the higher the load
"""

cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]
statistics['cpu_load'] = cpu_load

print(json.dumps(statistics, indent=4, sort_keys=True))
