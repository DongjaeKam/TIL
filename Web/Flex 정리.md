## CSS position
```css
position: static;
 /*기본 정렬 방식*/
position: relative;
 /*기본 정렬 위치 대비 떨어져서 배치 */
 /*원래 위치 공간은 그대로 차지 하면서 보이는 것만 이동 */
 /*차지하는 공간은 그대로 normal flow*/
position: absolute;
 /*부모 위치 기준 배치 */
 /*normal flow 무시 기존 자리를 차지 하지 않음 */
position: Fixed;
 /*View 포인트 기준 배치 */
position : sticky;
/* 스크롤에 따라 static -> fixed */
/* 예시) 구글 검색할 때보이는 상단 부분 스크롤 내려도,로고,검색창,설정 아이콘 등은 상단에 고정*/
	
```

## Flex

### 플렉스 컨테이너 만들기 (CSS)
```css
.container  {  
	display: flex;
}
```
### 플렉스 속성(CSS)
```css
 flex-direction : row;
 /* 행 방향 정렬 / 반대 row-reverse */
 flex-direction : column;
 /* 열 방향 정렬 / 반대 column-reverse */
 flex-wrap : wrap;
 /* 행을 넘기면 다른행에 배치 */
 flex-wrap : nowrap;
 /* 행 크기를 넘기면 크기가 줄어든다. 줄이지 못하는 경우 흘러 넘친다. */
 justify-content : flex-start;
 /* 시작점 부터 배치 */
 justify-content : flex-end;
 /* 뒤쪽 부터 배치 */
 justify-content : flex-center;
 /* 가운데 부터 배치 */
 justify-content : space-between;
 /* 요소들 간에만 여유 공간 */
 justify-content : space-around;   
 /* 컨테이너 내부에도 여유 공간 (flex-direction 쪽으로 여유) */
 
 align-items: stretch;
 /* 기본 설정으로, 플렉스 요소의 높이가 플렉스 컨테이너의 높이와 같게 변경된 뒤 연이어 배치*/
 align-items : flex-start;
 /* 플렉스 요소는 플렉스 컨테이너의 위쪽에 배치*/
 align-items : flex-end; 
 /*플렉스 요소는 플렉스 컨테이너의 아래쪽에 배치*/
 align-items : baseline; 
 /* 플렉스 요소는 플렉스 컨테이너의 기준선을 따라 배치*/
 
```

### 플렉스 사용 예시
```css
	.container{
		display : flex;
	}
```

```html
	<div class="container">
		<div>One</div>  
		<div>Item two</div>  
		<div>The item we will refer to as three</div>  
	</div>
```
