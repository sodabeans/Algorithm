def solution(n, arr1, arr2):
    answer = []
    for idx in range(n):
        ans = [' '] * n
        bin1 = str(bin(arr1[idx]).replace("0b", ""))
        bin2 = str(bin(arr2[idx]).replace("0b", ""))
        if len(bin1) < n:
            bin1 = ' ' * (n - len(bin1)) + bin1
        if len(bin2) < n:
            bin2 = ' ' * (n - len(bin2)) + bin2
        for j in range(n):
            if bin1[j] == '1':
                ans[j] = '#'
            if bin2[j] == '1':
                ans[j] = '#'
        
        answer.append(''.join(ans))
        
    return answer
  
