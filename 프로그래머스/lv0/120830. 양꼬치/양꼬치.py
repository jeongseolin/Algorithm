def solution(n, k):
    free_drink_count = n // 10
    total = 12000 * n + 2000 * k - 2000 * free_drink_count
    return total