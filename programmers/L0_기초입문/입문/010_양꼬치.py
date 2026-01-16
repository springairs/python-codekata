# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김지륜
# 작성일: 2026. 01. 16. 15:58:32

def solution(n, k):
    service = n // 10 
    drink = k - service
    total = n * 12000 + drink * 2000
    return total