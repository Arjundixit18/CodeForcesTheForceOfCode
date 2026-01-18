import string

allowed = string.ascii_letters + string.digits + "_"

s = input().strip()

if s.count('@') != 1:
    print("NO")
    exit()

username, rest = s.split('@')

# check username
if not (1 <= len(username) <= 16):
    print("NO")
    exit()

for ch in username:
    if ch not in allowed:
        print("NO")
        exit()

if '/' in rest:
    hostname, resource = rest.split('/', 1)

    if not (1 <= len(resource) <= 16):
        print("NO")
        exit()

    for ch in resource:
        if ch not in allowed:
            print("NO")
            exit()
else:
    hostname = rest

# check hostname length
if not (1 <= len(hostname) <= 32):
    print("NO")
    exit()

parts = hostname.split('.')

for part in parts:
    if not (1 <= len(part) <= 16):
        print("NO")
        exit()

    for ch in part:
        if ch not in allowed:
            print("NO")
            exit()

print("YES")
