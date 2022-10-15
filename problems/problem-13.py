def get_n_letters(s):
    x = set()
    for c in s:
        x.add(c)
    
    return len(x)

def get_longest_str(k, s):
    # String position indices
    i = 0
    j = 0
    
    # Substring indices
    t_start = 0
    t_end = 0
    t_max = 0
    t_diff = 0
    
    s_len = len(s)
    
    while j < s_len:
        while (t_diff <= k) & (j < s_len):
            j += 1 
            t = s[i:j]
            t_diff = get_n_letters(t)
            t_len = len(t)
            
            cond_len = t_len > t_max
            cond_k = t_diff <= k
            
            if cond_len & cond_k:
                t_max = t_len
                t_start = i
                t_end = j
                
        while t_diff > k:
            i += 1
            t = s[i:j]
            t_diff = get_n_letters(t)
    
    return (s[t_start:t_end])

s = get_longest_str(2, 'abcbadcddddcbbab')  

print(f"The longest string is {s}")

        
    
    
    
