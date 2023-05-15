def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        slice_array = array[i-1:j]
        sort_array = sorted(slice_array)
        answer.append(sort_array[k-1])
        
    return answer