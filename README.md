# BadPfs
Python script that generates pfs payloads to exploit CVE-2022-4510

Simply create a pfs payload using the script. When binwalk is run with -e on the payload, a file can be overwritten with the permission of binwalk.

This example will overwrite /etc/sudoers with the contents of ./data when it is opened with -e through binwalk. This is a great way to privesc.
```
# python3 BadPfs.py --out=payload.pfs --data=./data --target=/etc/sudoers
```
