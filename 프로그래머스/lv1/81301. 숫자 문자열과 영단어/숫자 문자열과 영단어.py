def solution(s):
    num_array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(num_array)):
        s = s.replace(num_array[i], str(i))

    answer = int(s)
    return answer