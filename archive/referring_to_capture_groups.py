import re

tag = '<div id="123">Hello</div>'

result = re.match(
    r"""
        <(div)\s+     # Match opening tag
        id="(\w+)"    # Match id attribute
        >           # End of opening tag
        ([^<>]+)      # Match contents of tag
        </\1>      # Closing div tag the \1 reffers the first group
    """, tag, re.VERBOSE)

if result is None:
    print("No match")
else:
    tag, id, content = result.groups()
    print(tag, id, content)
