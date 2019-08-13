
def get_sum(number):
    number = 3*number * number + number + 1
    ans = 0
    while number > 0:
        ans += number % 10
        number //= 10
    return ans
att = 1
cnt = 0
while True:
    if get_sum(att) == 100:
        cnt += 1
        print('Answer', cnt, '\t', att)
        if cnt % 100 == 0:
            input()
    att += 1