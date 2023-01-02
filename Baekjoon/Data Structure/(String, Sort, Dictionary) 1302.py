import sys
input = sys.stdin.readline

N = int(input())
dict_books = {}
ans_cnt = 0
ans_book = ''

for _ in range(N):
    book = input().rstrip()
    if book in dict_books:
        dict_books[book] += 1
    else:
        dict_books[book] = 1

for (book, count) in dict_books.items():
    if count > ans_cnt:
        ans_cnt = count
        ans_book = book
    elif count == ans_cnt:
        if ans_book > book:
            ans_book = book

print(ans_book)
