def repeating(s, key_len, min_rep):
    d={}
    for sublen in range(key_len, int(len(s)/min_rep)):
        for i in range(0, len(s)-sublen):
            sub = s[i:i+sublen]
            cnt = s.count(sub)
            if cnt >= min_rep and sub not in d:
                 d[sub] = cnt
    return d

len(re.search(r'apa(.*)apa', two).group(1))
