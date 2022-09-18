# 배운내용 정리하기

## Markdown
  

### # 개수를 늘리면 글자가 작아지면서 하위문단 느낌으로 정리됨

  
  

### list정리

  

  

1. 인덱스 정리 (숫자. 사용했을 때 적용됨)

  

- 인덱스 정리 ( - 사용했을 때 적용됨 )

  

  

### 이미지 삽입

`![문자열](url)`

  

### 링크

` [문자열](url)`

  

  

### 인용문 삽입

` > 인용문`

> 인용문은 이렇게 쓰는 거다.

  

### 텍스트 강조

  

`<strong> 강조할 문자 </strong>`

  

텍스트는 이렇게 <strong> 강조 </strong> 하면 된다.

  

  

### 코드 넣기

  

  

``` python

  

print("크게 넣기")

  

```

  

  

작게 문장 사이에 넣기 `print("hello")`

  

  

### 라인 그리기 * 세개

  

  

***

  

  

### 라인 그리기 - 세개

  

  

---

  

  

### 라인 그리기 _ 세개

  

  

___

  

  

### 테이블


| Syntax | Description |
| --------- | ----------- |
| Header | Title |
| Paragraph | Text |

  

  

### 텍스트

1.  **굵게** : `**텍스트**`

2.  *기울임* : `*텍스트*`

3.  ~~취소선~~ : `~~텍스트~~`


## Git

### 기초명령어
`git init` : 로컬 저장소 생성 

`git add <파일명>`  : 특정 파일/폴더의 변경사항 추가 

`git commit –m ‘<커밋메시지>` : ’ 커밋 (버전 기록)

`git status` : 상태 확인 

`git log` 버전 확인

### Git 기본 설정 정리
`git config —global user.name “username”`

:GitHub에서 설정한 이름을 등록

`git config —global user.email “my@email.com”`

:GitHub에서 설정한 이름을 등록

`git remote add origin https://github.com/kdt-live/test.git`

:GitHub에서 만든 Repository에 접근하도록 설정

### 원격 저장소 정보 확인
`git remote -v`


### Git 오류 수정
기존 Repository 정보 제거
` git remote remove origin`

###Git push 맨처음에 할 때
`git push -u origin master`
나중에는 'git push'만 해도 된다


