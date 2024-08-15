import re
import os
import time
import subprocess
while(True):
    sunshineProcessCount = str(subprocess.check_output("ps -a | grep 'sunshine' | wc -l", shell=True))
    sunshineProcessCount = re.findall(r'\d+', sunshineProcessCount)[0]
    print(sunshineProcessCount)
    if(int(sunshineProcessCount)<1):
        os.system("sunshine output_name=0")

    time.sleep(15)
