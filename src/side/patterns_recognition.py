import re

with open('keys.txt', 'r', encoding='utf-8') as f:
    next(f)  
    keys = [line.split(',')[1].strip() for line in f]

regex_patterns = [
    '-'.join(
        fr"\d{{{len(x)}}}" if x.isdigit() else
        fr"[A-Z]{{{len(x)}}}" if x.isalpha() else
        fr"[A-Z0-9]{{{len(x)}}}"
        for x in key.split('-')
    )
    for key in keys
]

with open('key_patterns.txt', 'w') as f:
    f.write("key_pattern\n" + '\n'.join(regex_patterns))