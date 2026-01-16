# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 김지륜
# 작성일: 2026. 01. 16. 16:14:52

def solution(numbers):
    sums = sum(numbers)
    count = len(numbers)
    avg = sums / count
    return avg