def solution(my_strings, parts):
    result = ""
    
    for string, (start, end) in zip(my_strings, parts):
        substring = string[start:end+1]
        result += substring
    
    return result

