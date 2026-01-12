def solve():
    s = input().strip()
    max_char = max(s)         
    count = s.count(max_char) 
    print(max_char * count)
