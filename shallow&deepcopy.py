""""
import copy
m=[[23,2],[12,7,9]]
new_line=copy.copy(m)
new_line[1][2]=30
print(new_line)
print(m)
"""
"""
import copy
m=[[23,2],[12,7,9]]
new_line=copy.deepcopy(m)
new_line[1][2]=30
print(new_line)
print(m)
"""