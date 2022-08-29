# HTML 정리
## head 태그
``` html
<head>
</head>
```
## body태그
``` html
<BODY>
	HTML의 본문 부분 표현하려는 내용이 나열되는 공간
</BODY>
```
## h1~ h6 태그
``` html
<h1> 제목을 입력하는 곳 </h1> 
<!-- 숫자가 클수록 하위 제목 -->
```
## span 태그
``` html
<span> 글자를 입력 하고 글자 서식도 지정 가능 </span>
```
## br 태그
``` html
<br> : 줄을 바꿔주는 태그
```

## hr 태그
``` html
<hr> :선 긋기 의미적으로 나눌 때 사용
```

## textarea태그
``` html
여러줄을 입력 받을 때 사용 댓글 기능에 많이 사용 된다.
<textarea>
여러 줄을
입력해도 되요!
</textarea> 
```
## hr 태그
``` html
<hr> :선 긋기 의미적으로 나눌 때 사용
```
## img 태그
``` html
이미지를 삽입할 때 사용하는 태그
<img src="imagename.png" />
```
## style 태그
``` html
<style></style> 
```
- 요소의 속성을 정할 때 사용
- 분리해서 쓰기도 하고 
- 요소의 안쪽에 쓰기도 한다.
- 주로 분리해서 쓰고 파일도 따로 관리한다.

### 안쪽 사용 예시
```html
<h2  style="color: blue; font-size: 15px;">h2</h2>
```
### 바깥쪽 사용 예시
```html
<style>

	<!-- 해당 태그 부분에 모두 적용  -->
	h4 {

		color: brown;

	}

	<!-- 이름으로 불러와서 적용 되는 -->
	.title-brown {

		color: brown;

	}
	
</style>
```
#### 추가 설명
>  CSS는 선택해서 스타일을 적용한다. 
> 적용에는 우선순위가 있다.
> 같은 레벨이라면 나중에 '선언'된 것이 적용된다.
> id, class, 태그는 서로 다른 레벨이다.
> id > class > 태그 순으로 우선순위를 가집니다.
> 다만, 일반적으로 CSS 스타일링은 클래스로만 합니다.
> id는 문서에서 반드시 한번만 등장해야 합니다.
> id는 잘 활용하지 않고, 자바스크립트(JS)로 개발할 때 보통 활용합니다.


## header / main / footer 태그
- 기능에 따른 영역을 나누는 태그
- header 
	  웹페이지의 최상단부분. 주로 사이트의 이름, 검색창, 네비게이션 등의 내용이 포함
	주로 사이트의 이름, 검색창, 네비게이션 등의 내용이 포함

- main 
    본문영역

- footer
    웹페이지의 최하단부분. 주로 상호명, 연락처, 개인정보처리방침 등의 내용이 포함

``` html
<html>
	<body>	
		<header>
		</header>
		<main>
		</main>
		<footer>
		</footer>
	</body>
</html>
```

``` html
<hr> :선 긋기 의미적으로 나눌 때 사용
```
