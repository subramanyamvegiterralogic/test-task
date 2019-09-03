import re
input_str  = ['U1,U2', 'U3,U4', 'U2,U1', 'U1,U5', 'U4,U5', 'U5,U3', 'U3,U1','U2,U6']
unique_list = []
local_set = set()
for item in input_str:
    local_set.add(','.join(sorted(re.split(r',',item))))
output_str = list(sorted(local_set))
print(output_str)
