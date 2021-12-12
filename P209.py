#

import re

zen = """Although never is
ofen better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If hte implemantation
is easy to explain,
if may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""


m = re.findall("^If", zen, re.MULTILINE)
print(m)

