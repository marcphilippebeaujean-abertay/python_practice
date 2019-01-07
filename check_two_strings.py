
def one_opp_necessary(s1, s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    operations_needed = 1 if abs(len(s1)-len(s2)) > 0 else 0
    i=0
    while i < len(s1):
        if s1[i] != s2[i]:
            operations_needed+=1
            if s1[i+1] == s2[i]:
                i+=2
                continue

        i+=1