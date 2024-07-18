## EL 표기법 (Expression Language)

- View단에서 java코드를 없애기 위함. <%= request.getAttribute("result") %> 같은 거.
  <br><br>

- <%= request.getAttribute("result") %> => `${result}`
- 배열, List 꺼내기 : <%= ((List)request.getAttribute("list")).get(0) %> → `${list[0]`}
- Map 꺼내기 : `${Map이름.값의이름}` (`.`을 사용)
  <br><br>

⇒ EL을 통해 pageContext에 담긴 것 등 어디에 있든지 뽑아낼 수 있다.

(ex : pageContext.setAttribute("aa", "hello") → ${aa}로 뽑아낼 수 있음)
<br><br>

그렇다면 각 저장소에 같은 키워드로 저장된다면? → <u>우선순위</u>에 따라 첫번째 것이 출력됨.

**(우선순위 : page → request → session → application)**

→ 특정 위치의 것을 뽑고 싶다면? → 내장 객체를 사용.

- pageScope / requestScope / sessionScope / applicationScope
  (ex : ${sessionScope.cnt} )
