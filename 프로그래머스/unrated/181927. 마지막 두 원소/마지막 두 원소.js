function solution(num_list) {
    let b = num_list.length - 1;
    let a = num_list.length - 2;
    if (num_list[b] > num_list[a]) {
        num_list.push(num_list[b]-num_list[a]);
    } else {
        num_list.push(num_list[b] * 2);
    }
    return num_list;
}