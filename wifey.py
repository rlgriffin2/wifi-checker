import subprocess
from datetime import datetime
while(True):
    output = subprocess.run(["ping", "8.8.8.8"], capture_output=True)
    first_outage = True
    start = datetime.now()
    end = datetime.now()
    wifi_out = False
    while("Received = 0" in output.stdout):
        if(first_outage):
            start = datetime.now()
            first_outage = False
            wifi_out = True
        end = datetime.now()
    if(wifi_out):
        wifi_out = False
        with open('times.txt', 'w') as f:
            times = f'Start: {start} \nEnd: {end}\n\n'
            f.write(times)