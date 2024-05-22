def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowel_dictionary = []
    
    for i in range(5):
        curr = vowels[i]
        answer += 1
        if curr == word:
            return answer
        for j in range(5):
            curr = vowels[i] + vowels[j]
            answer += 1
            if curr == word:
                return answer
            for k in range(5):
                curr = vowels[i] + vowels[j] + vowels[k]
                answer += 1
                if curr == word:
                    return answer
                for l in range(5):
                    curr = vowels[i] + vowels[j] + vowels[k] + vowels[l]
                    answer += 1
                    if curr == word:
                        return answer
                    for m in range(5):
                        curr = vowels[i] + vowels[j] + vowels[k] + vowels[l] + vowels[m]
                        answer += 1
                        if curr == word:
                            return answer
    return answer
