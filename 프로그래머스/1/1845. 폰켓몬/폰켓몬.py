def solution(nums):
    tmp = []
    answer = 0
    for num in nums:
        if num not in tmp:
            tmp.append(num)
            answer += 1
            if answer == len(nums) // 2:
                break
    return answer