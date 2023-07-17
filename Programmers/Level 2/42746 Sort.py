def solution(numbers):
    numbers = list(map(str, numbers)) # string으로 변환
    numbers.sort(key=lambda x: x*4, reverse=True)  # 최대 길이가 4라서 4번 반복 ('1000')
    answer = ''.join(numbers) # 순서대로 concat해서 가장 큰 숫자 만들기
    if answer[0] == '0': # '00' 같은 케이스 처리
        answer = '0'
    return answer
