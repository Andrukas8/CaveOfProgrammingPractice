"""
\w  matches alphanumeric characters
... matches three letters
+   matches one or more, or as many as possible
\s  match a single space
\d  match digits
\.  match a dot
+   one or more
*   zero or more
"""


import re

text = "The temperature is: 37"
result = re.match(r".*:\s*(\d+)", text)

print("No match" if result is None else f"'{result.group(1)}'")