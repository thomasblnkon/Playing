import re


f = open("/Users/thofer/Documents/Projekte/IOC/policy_ioc.txt", "r")
lines = f.readlines()
newlines = []
for line in lines:
    match = re.match("set security policies from-zone (.*) to-zone (.*) policy permit", line)
    if match:
        newlines.append(line.replace("policy permit", "policy {0}_{1}_ANY".format(match.group(1), match.group(2))))
    else:
        newlines.append(line)

for line in newlines:
    print(line)



