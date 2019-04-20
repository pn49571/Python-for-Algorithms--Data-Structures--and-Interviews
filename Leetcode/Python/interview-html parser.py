import re
markdown = '##         Lost In Space'
markdown =  markdown.lstrip()
markdown =  markdown.rstrip()
converted = ''
if re.findall(r'^#\s.*$', markdown):
    converted = '<h1>' + (markdown[2:]).lstrip() + '</h1>'
elif re.findall(r'^##\s.*$', markdown):
    converted = '<h2>' + (markdown[3:]).lstrip() + '</h2>'
elif re.findall(r'^###\s.*$', markdown):
    converted = '<h3>' + markdown[4:] + '</h3>'
elif re.findall(r'^####\s.*$', markdown):
    converted = '<h4>' + markdown[5:] + '</h4>'
elif re.findall(r'^#####\s.*$', markdown):
    converted = '<h5>' + markdown[6:] + '</h5>'
elif re.findall(r'^######\s.*$', markdown):
    converted = '<h6>' + markdown[7:] + '</h6>'
print(converted)
