import requests
from collections import Counter

def calc_age(uid):
    token = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
    r1 = requests.get(f'https://api.vk.com/method/users.get?v=5.71&access_token={token}&user_ids={uid}')
    id = r1.json()['response'][0]['id']
    r2 = requests.get(f'https://api.vk.com/method/friends.get?v=5.71&access_token={token}&user_id={id}&fields=bdate')
    friends = r2.json()['response']['items']

    dates = []

    for friend in friends:
        try:
            dates.append(friend['bdate'])
        except KeyError:
            continue

    ages = []

    for date in dates:
        if len(date.split('.')) == 3:
            year = date.split('.')[2]
            age = 2020 - int(year)
            ages.append(age)

    result = []

    c = Counter(ages)
    for i in c:
        result.append((i, c[i]))

    res = sorted(result)
    res1 = sorted(res, key=lambda a: a[1], reverse=True)

    return res1


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
