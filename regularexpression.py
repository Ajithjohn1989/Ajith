"""import re
p=r"python"#pattern which need to be find in expression
s="I Love python"#expression to which pattern to be find
m=re.search(p,s)
print(m)
"""
""""
import re
p=r"python"
s="python programming on Aug20"
m=re.match(p,s)
print(m)
"""
import re
p=r"^python$"#$ used for starting till end same pattern
s="python12"
m=re.search(p,s)
print(m)