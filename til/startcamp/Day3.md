# Day3

## HTML/CSS

### HTML

`HTML`은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

1. HTML 기본 구조

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       <h1>{{name}}아, {{pick}}먹어!!!</h1>
   </body>
   </html>
   ```

   * `<head> </head>`는 문서의 정보를 담고 있다.
   * `<body> </body>`는 문서의 본문을 담고 있다.

2. 태그의 종류

   1. 기본적으로 태그는 `여는태그`와 `닫는태그`로 구성된다.

      ```html
      <h1>제목1</h1>
      ```

   2. `닫는태그`가 없는 경우도 있다.(self-closing tag)

      ```html
      <img src="_"/>
      ```

   3. 태그의 구성

      ```html
      <img src="_" width="300" height="300" class="img-blue"/>
      <a href="https://google.com" class="blue">구글</a>
      ```

      * 태그별로 공통저그로 가질 수 있는 속성 : `id`, `class`, `style`
      * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
        * img - `src`, `width`, `height`
        * a- `href`

# CSS

CSS는 Cascading Style Sheet의 약자로, HTML을 꾸며주는 역할을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)` 를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   * 태그 선택자

     ```css
     p{
         color: red;
     }
     ```

     

   * class 선택자

     ```css
     .blue{
         color: blue;
     }
     ```

   * id 선택자

     ```css
     #pink{
         color: black;
     }
     ```

     선택자 우선순위는 id선택자 > class선택자 > 태그선택자 순서로 적용된다.

## Flask

`Flask` 는 파이썬 기반의 micro framework이다.

### 기본 활용법



1. 설치

   ```bash
   $ pip install flask
   ```

2. 기본 코드

   ```python
   from flask import Flask
   
   app=Flask(_name_)
   
   @app.route('/')
   def hello():
       return 'Hello!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. 서버 실행

   ```bash
   $ flask run
   ```

   * 기본적으로 `flask run`명령어는 `app.py`파일을 실행시킨다. 

     만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.

   * 마지막 두 줄을 작성해 놓았다면, 아래와 같이 실행도 가능하다.

     ```bash
     $ python app.py
     ```

## Variable routing

요청 오는 url을 변수화하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'{name}아 안녕?''
```

## Rendering Template

`HTML`파일을 만들어 활용할 수 있다. 기본적으로 `template`폴더에 파일을 만들어야 한다.

```
app.py
templates/
	hi.html
	lunch.html
	index.html
```

```python
from flask import Flask, render_template
#...
@app.route('/hi')
def hi():
    return render_template('hi.html')
```

`HTML` 파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야 한다.

```python
return render_template('hi.html',name=name)
```

그리고 출력을 위해서는 `{{}}` 사용한다.

```jinja2
<h1>
    {{name}} 안녕?
</h1>
```



## Flask Template Engine-jinja2

Flask는 기본적으로 Template을 만들 때 `jinja2` 언어를 사용한다. 기본 문법은 다음과 같다

1. 값 출력

   ```jinja2
   <h1> {{name}}, 안녕? <h1>
   ```

2.  조건문

   ```jinja2
   {% if name == '용흠' %}
   	<h1>반장님 안녕하세요.</h1>
   {% else %}
   	<h2>학생들 ㅎㅇ</h2>
   {% endif %}
   ```

3. 반복문

   ```jinja2
   {% for menu in menu_list %}
   	<li>{{ menu}}</li>
   {% endfor %}
   ```

## Form data

HTML에서 사용자로부터 정보를 받기 위해서는 `form`태그를 활용한다.

### form 태그 기본 구조

```html
<!-- templates/pind.html -->
<form action = "/pong">
    <input type = "text" name = "say">
    <input type = "radio" name = "gender" value = "M"> 남자
    <input type = "radio" name = "gender" value = "F"> 여자
    <input type = "submit" value = "전송">
</form>
```

* form 태그는 `action`속성으로 해당 폼이 전송될 url을 지정해야 한다.

* form 태그 내에는 `input`태그들을 정의하여, 사용자에게 받을 정보를(설문지를 만든다.)

  만들어 놓는다.

* `input`태그에는 어떤 종류의 입력을 받을지 `(type)`와 어떤 변수를 담아서 보낼지

   `(name)`정의한다.

## Flask에서 사용자로부터 정보 받기

1. 사용자가 입력할 수 있는 `form`보내주기

   ```python
   # app.py
   @app.route('/ping')
   def ping():
       return render_template('ping.html')
   ```

   ```html
   <!-- templates/pind.html -->
   <form action = "/pong">
       <input type = "text" name = "say">   
       <input type = "submit" value = "전송">
   </form>
   ```

2. 정보 받아서 활용하기

   ```python
   #app.py
   from flask import Flask, render_template, request
   
   
   
   @app.route('/pong')
   def pong():
       text = request.args.get('say')
       return render_template('pong.html', say=say)
   ```

   ```html
   <!-- templates/pong.html -->
   <h1>{{say}}!!!!</h1>
   ```

   * `request.args`는 일종의 `dictionary`이고, `key`는 input에 정의한 name이고 사용자가 입력한 값은 `value`이다.

     


# Day 3(2)

# 파이썬 문법

## 문제 1

```python
# 문제 1.
'''
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str = input('문자를 입력하세요: ')
a=list(str)
print(a[0])
print(a[-1])
# 아래에 코드를 작성해 주세요.
```

## 문제 2

```python
'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

N = int(input('숫자를 입력하세요: '))
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.

for i in range(1,N+1):
    print(i)
```

## 문제 3

```python
'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

N = int(input('숫자를 입력하세요: '))
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.

if N%2==0:
    print("짝수")
else:
    print("홀수")
```

## 문제4

```python
'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))
# 위의 4줄의 주석을 풀고 아래에 코드를 작성해 주세요.

if a>=90 and b>80 and c>85 and d>=80:
    print("True")
else:
    print("False")
```

## 문제5

```python
'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000;5000000
'''

p = input('물품 가격을 입력하세요: ')
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.

# map : 첫번째 인자의 함수를 두번째 인자를 반복하여 적용.
# 반복 가능한 객체에 함수를 각각 적용

a=list(map(int,p.split(";")))
print(sorted(a,reverse=True))

# list.sort() :return이 none.  원본 리스트 자체를 변경
# sorted(list) : return이 정렬된 리스트. 원본 자체는 변경하지 않음

```

# HTML

```html
<!DOCTYPE html>
<html lang="ko">
    <head?>
        <meta charset="utf-8">
        <title>첫번째 HTML</title>
        <style>
            h1{
                color:red;
                text-align: center;
                
            }
            p{
                color:blue
            }
            /* 태그 선택자 */
            h2{
                color: black
            }
            /* 클래스 선택자 */
            .red{
                color:red
            }
            /* 아이디 선택자 */
            #pink{
                color:pink
            }
            /* 우선순위
            id > class > 태그
            id는 문서에서 하나만 존재할 수 있다.
            class는 문서에서 여러개 존재할 수 있다.
            태그는 그냥 기본이다.
             */
        </style>
    </head>
    <body>    
        <h1>Happy, hacking!</h1>
        <h2 id="pink">오늘 밥메뉴뭐임?</h2>
        <h6>가장 작은 제목입니다.</h6>
        <p>내용내용, <br>문단의 내용을 작성합니다.</p>
        <p class="red">나는 빨간색이고 싶어요.</p>
        
        <!--a 태그는 href속성으로 해당하는 링크를 설정한다.-->
        <a href="https://www.swexpertacademy.com/main/main.do">SWEA</a>
        <br>
        <!--img 태그는 닫는 태그가 없다. src 속성값은 이미지의 경로이다.-->
        <img src=>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Pxj6mjhmIjA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>       
    </body>
</html>
```

## HTML 처리순서?

- 우선순위

  `id > class > 태그`

  id는 문서에서 하나만 존재할 수 있다. 그리고 class는 문서에서 여러개 존재할 수 있다.

  태그는 그냥 기본이다.

