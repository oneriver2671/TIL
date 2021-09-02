### javascript에서 정규식을 활용해 콤마 제거하기

```jsx
// 정규식을 활용해 콤마 제거 (70,000 -> 70000)
var totalPrice = _totalPrice.replace(/,/g, "");
```

<br>

### session에 있는 값 javascript에서 바로 변수로 찍어낼 수 있음

```jsx
// String id = (String)session.getAttribute("id");

// jsp에서 위처럼 받지 않고, 그냥 바로 js에서 EL표기법으로 불러올 수 있음.
var memberId = "${id}"; // 회원 ID (session에서 get)
```

<br>

### 댓글 script 띄운 방법 (취소 / 확인)

`<a href="aaa.jsp" onclick="return 함수명(매개변수);">a링크</a>`

이렇게 사용하는 경우, href에 설정한 경로로 이동하는 것보다 onclick이벤트가 **먼저 실행**된다. onclick 이벤트의 **리턴값**이 true이면 href로 연결된 링크로 이동하고, false이면 이동하지 않는다.

```html
<!-- 내가 쓴 방법. 게시글 삭제 -->
<script>
  function deleteArticle() {
    if (confirm("정말 삭제하시겠습니까?") == true) {
      return true;
    } else {
      // 취소 버튼
      return false;
    }
  }
</script>

<a
  href="boardDelete.bo?orders=<%=dto.getOrders() %>&sort=<%=dto.getSort() %>"
  onclick="return deleteArticle()"
  >삭제</a
>
```

<br>

## [javascript] html의 값 여러개를 가져와 배열에 넣기 ⭐

```jsx
function goNext() {
  /* html부분 생긴 형태 */
  // <div id="seatChoice_show_grade">
  // 	<button> (value="좌석정보", text="좌석등급(R석, S석..)")  </button>
  //	<button> (value="좌석정보", text="좌석등급(R석, S석..)")  </button>
  // </div>

  // '배열'을 만들어 담기
  var selectedSize = $("#seatChoice_show_grade button").length; // button의 갯수를 가져올 수 있음!!
  var selectedSeatGrade = new Array(selectedSize); // js의 배열 생성 (좌석등급)
  var selectedSeatArr = new Array(selectedSize); // (좌석정보)

  for (var i = 0; i < selectedSize; i++) {
    selectedSeatGrade[i] = $("#seatChoice_show_grade button").eq(i).text(); // '좌석등급'을 순서대로 담기
    selectedSeatArr[i] = $("#seatChoice_show_grade button").eq(i).val(); // '좌석정보'를 순서대로 담기
  }
}
```
