import urllib.request, re

#Script to find latest artifact in the artifactory location
fp = urllib.request.urlopen("https://repo1.uhc.com/artifactory/generic-local/com/optum/exts/k8s/images/")
mybytes = fp.readlines()

fp.close()
items={}
for line in mybytes:
    if 'centos7' in line.decode("utf-8").lower() or 'centos-7' in line.decode("utf-8").lower():
        line=line.decode("utf-8")
        items[re.search('"(.*)"', line).group(1)]=' '.join(line.split(' ')[-5:-3])
print(items)