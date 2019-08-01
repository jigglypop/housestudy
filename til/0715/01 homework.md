# 상승장? 하락장?

> 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

|      Key Name |                    Description |
| ------------: | -----------------------------: |
|  opeing_price |   최근 24시간 내 시작 거래금액 |
| closing_price | 최근 24시간 내 마지막 거래금액 |
|     min_price |   최근 24시간 내 최저 거래금액 |
|     max_price |   최근 24시간 내 최고 거래금액 |

In [86]:











```
import requests

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
print(data)
```







```
{'opening_price': '13593000', 'closing_price': '12308000', 'min_price': '11879000', 'max_price': '13600000', 'average_price': '12686773.5778', 'units_traded': '16949.31898782', 'volume_1day': '16949.31898782', 'volume_7day': '90088.88766032', 'buy_price': '12300000', 'sell_price': '12305000', '24H_fluctate': '-1285000', '24H_fluctate_rate': '-9.45', 'date': '1563172821432'}
```

In [100]:











```
# 아래에 코드를 작성하세요.

B = int(data['max_price'])
S = int(data['min_price'])
O = int(data['opening_price'])

if O + B - S > B:
    print('상승장')
else:
    print('하락장')  
```







```
상승장
```

In [ ]:











```
if int(data['opening_price']) + int(data['min_price']) + int(data['max_price']) > int(data['max_price']):
    print('상승장')
else:
    print('하락장')
```









# 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.

```
예시 입력)
"Life is too short, you need python"
예시 출력)
Lf s t shrt, y nd pythn
```

In [55]:











```
my_str = "Life is too short, you need python"
```







In [114]:











```
# 아래에 코드를 작성하세요.

M = list(my_str)
for i in range(len(M)):
    if ord(my_str[i]) != 97 and ord(my_str[i]) != 101 and ord(my_str[i]) != 105 and ord(my_str[i]) != 111 and ord(my_str[i]) != 117:
        print(M[i],end = "")
```







```
Lf s t shrt, y nd pythn
```

In [131]:











```
M = list(my_str)
for i in range(len(M)):
    if my_str[i] not in ['a','e','i','o','u']:
        print(M[i],end = "")
```







```
Lf s t shrt, y nd pythn
```

In [135]:











```
r = ''
# my_str을 반복하면서, 
# 모음이 아니면, r에 추가한다.
# 반복문이 끝나면 출력한다.

for char in my_str:
#    if char not in ['a','e','i','o','u']:
    if char not in 'aeiou':
        r += char

print(r)
```







```
Lf s t shrt, y nd pythn
```

In [139]:











```
for vowel in 'aeiou':
    my_str = my_str.replace(vowel,'')
print(my_str)
```







```
Lf s t shrt, y nd pythn
```



# 개인정보보호

> 사용자의 핸드폰번호를 입력 받으려고한다. 개인정보 보호를 위하여 뒷자리 4자리를 제외하고는 마스킹 처리를 하려고한다.
>
> 핸드폰번호는 010으로 시작해야하고 11자리여야한다. 핸드폰번호를 입력하지 않았다면 "핸드폰번호를 입력하세요"를 출력한다

```
예시 입력)
01012341234
예시 출력)
*******1234
```

In [141]:











```
phone = input()
```







```
01012341234
```

In [145]:











```
if phone[0:3] == '010' and len(phone) == 11:
    print('*'*7 + phone[-4:])
else:
    print('핸드폰 번호를 입력하세요.')
```







```
*******1234
```

In [147]:











```
if phone.startswith('010') and len(phone) == 11:
    print(f'{phone[-4:]:*>11}')
else:
    print('핸드폰 번호를 입력하세요.')
```







```
*******1234
```

In [113]:











```
# 아래에 코드를 작성하세요.
a = list(phone)
S = ['*']*(len(a)-4)
b =a[len(a)-4:len(a)]

M = S + b
print("".join(M))
```







```
*******1234
```

In [119]:











```
a = list(phone)
for i in range(len(a)):
    for j in range(len(a)-4):
        a[j] = '*'

print("".join(a))
```

```
*******1234
```



# 정중앙

> 사용자가 입력한 문자열중 가운데 글자를 출력하라. 문자열이 짝수라면 가운데 두글자를 출력하라



```
text = input()
```

```
안녕하세요다
```

```
# 아래에 코드를 작성하세요.
if len(text) % 2 == 0:
    print(text[len(text)//2-1]+text[len(text)//2])
else:
    print(text[len(text)//2])
```

```
하세
```

```
num = len(text) // 2
if len(text) % 2:
    print(text[num])
else:
    print(text[num-1 : num+1])
```

```
하세
```