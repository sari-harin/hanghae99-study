def solution(s):
    answer = True
    p_num, y_num = 0, 0;
    
    a = list(s)
    
    for i in a:
        if i.lower() == "p":
            p_num += 1;
        elif i.lower() == "y":
            y_num += 1;
            
    if y_num != p_num:
        answer = False

    return answer