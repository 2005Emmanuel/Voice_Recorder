# importing Recorder from module recorder
from recorder import Recorder  
r = Recorder()  
record = r.record(10, output="record.wav")
print(record)


