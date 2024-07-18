## Core 태그

먼저, 반드시 JSP 페이지 상단에 다음과 같이 taglib 디렉티브 태그를 추가하여 톰캣에게 알려줘야 한다.

```jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
```

<br>

### Core 태그 라이브러리의 기능

- `<c:set>` : JSP 페이지에서 변수 지정.
- `<c:remove>` : 변수 제거
- `<c:if>` : 조건문 사용
- `<c:choose>` : switch문 (`<c:when>`, `<c:otherwise>`를 서브 태그로 가짐)
- `<c:forEach>` : 반복문 사용
- `<c:import>` : URL을 이용해 다른 자원을 JSP 페이지에 추가
- `<c:redirect>` : response.sendRedirect() 기능을 수행
- `<c:url>` : 요청 매개변수로부터 URL을 생성
- `<c:catch>` : 예외 처리에 사용
- `<c:out>` : JspWriter에 내용을 처리한 후 출력함
  <br><br>

## <c:set>

```jsp
<c:set var="id" value="jang" scope="page" />
<c:set var="pwd" value="1234" scope="page" />
<c:set var="name" value="${'장한강'}" scope="page" />   <!-- value에 EL태그를 쓸 수 있음 -->
```

```html
<tr>
  <td>${id}</td>
  <td>${pwd}</td>
  <td>{$name}</td>
</tr>
```

- scope : 변수 스코프를 지정. (page, request, session, application)
  <br><br>

## <c:if>

```jsp
<c:if test="${true}">
  <h1>항상 참입니다.<h1>
</c:if>

<c:if test='${(id=='jang') && (name=='장한강')}'>
  <h1>아이디는 ${id}이고, 이름은 ${name}입니다.</h1>
</c:if>
```

- `<c:if>` 활용 중 생겼던 오류

  ```html
  <c:if test="${performDTO != null}">
    <div class="test">performDTO는 null이 아니다!</div>
  </c:if>

  <!-- 처음에 작동하지 않았던 이유 -->
  <c:if test="${performDTO} != null">
    <!-- null을 {} 바깥에 쓰면 안됨. 안에 써줘야 함! -->
    <div class="test">performDTO는 null이 아니다!</div>
  </c:if>
  ```

<br>

## <c:choose>

```jsp
<c:set var="count" value="3" />

<c:choose>
  <c:when test="${count <= 0 }">
  일치하는 것이 하나도 없습니다.
  </c:when>
  <c:otherwise>
  일치하는 것이 ${count}개 있습니다.
  </c:otherwise>
</c:choose>
```

<br>

## <c:forEach>

```jsp
<h3> 1부터 100까지 3의 배수 합 </h3>
<c:set var="sum" value="0" />
  <c:forEach var="i" begin="3" end="100" step="3">
    <c:set var="sum" value="${sum + i}" />
  </c:forEach>
결과 = ${sum}
```

### ArrayList에 담긴 정보 뽑아내기

```jsp
<%
  List membersList = new ArrayList();
  MemberBean m1 = new MemberBean("son", "손흥민");
  MemberBean m1 = new MemberBean("jang", "장한강");
  MemberBean m1 = new MemberBean("kim", "김덕배");
  membersList.add(m1);
  membersList.add(m2);
  membersList.add(m3);
%>

<c:set var="membersList" value="<%=membersList %>" />

<c:forEach var="i" begin="0" end="2" step="1">
  <tr>
    <td>${membersList[i].id}</td>
    <td>${membersList[i].name}</td>
  </tr>
</c:forEach>
```

```jsp
<%
  String arr[]={"불고기 백반;", "오므라이스", "콩국수" };
  request.setAttribute("MENU", arr)
%>

<h3>오늘의 점심 메뉴입니다.</h3>
<ul>
	<c:forEach var="dish" items="${MENU}">   <!-- EL태그 활용해 request에 담긴 값 가져오기 -->
		<li>${dish}</li>
	</c:forEach>
</ul>
```

- items : 반복할 객체의 이름
  <br><br><br>

### split 기능 사용하기

```jsp
<%@ taglib uri = "http://java.sun.com/jsp/jstl/functions" prefix = "fn" %>

<c:set var="booked_seat" value="${performSeatDTO.booked_seat }" />   <!-- 콤마로 연결된 문자열인 상태 -->
<c:set var="bookedSeatArr" value="${fn:split(booked_seat, ',')}" />		<!-- 위의 function uri 불러와야함. -->
```

<br>

### forEach활용 (배열 출력하기)

⇒ 티켓예매 '좌석 등급', '좌석 정보' 각각 배열에 담아 forEach로 출력했음.

- Java의 String 클래스의 `split()` 메소드를 활용해 배열에 담았다.

  ```java
  <%
  // step2.jsp의 좌석정보
   String selectedSeatGrade = request.getParameter("selectedSeatGrade");
   String selectedSeatVal = request.getParameter("selectedSeatVal");

  // 콤마로 구분되어 넘어오네. 순서대로 처리하자. 배열에 담아야함.
   String[] seatGradeArr = selectedSeatGrade.split(",");		// 콤마 단위로 끊어 배열에 넣을 수 있는 split() 메소드
   String[] seatValArr = selectedSeatVal.split(",");
  %>
  ```

- 이후 jstl 변수 설정.

  ```html
  <c:set var="seatGradeArr" value="<%=seatGradeArr %>" />
  <!-- 이런식으로 넣어줄 수 있음. -->
  <c:set var="seatValArr" value="<%=seatValArr %>" />
  ```

- 마지막으로, html에서 forEach활용해 배열 찍어내기

  ```html
  <div id="selected_seatBox_grade">
    <c:forEach var="grade" items="${seatGradeArr }">
      <div>${grade }</div>
    </c:forEach>
  </div>
  <div id="selected_seatBox_val">
    <c:forEach var="val" items="${seatValArr }">
      <div>${val }</div>
    </c:forEach>
  </div>
  ```

<br><br>

---

### ('21.8.20)

```jsp
<c:out value="${performDTO }" />
```

`session.getAttribute("performDTO")`를 대신해 값을 받아오는 걸 확인. <br>
But, 만약 `<c:set>`으로 performDTO라는 변수를 새로 만들면, 그 변수로 덮어지는 것을 확인. <br>

```jsp
<!-- 예시 -->
<%
  PerformDTO performDTO = (PerformDTO)session.getAttribute("performDTO");
%>
<c:set var="performDTO" value="<%=performDTO.getLocation() %>" />
<c:out value="${performDTO }" />

<!-- 이렇게 찍으면, location 값이 찍혀나온다. -->
```

<br><br>

- if문으로 값 비교할 때 실수.

```html
<c:if test="${performDTO != null}">
  <div class="test">performDTO는 null이 아니다!</div>
</c:if>

<!-- 처음에 작동하지 않았던 이유 -->
<c:if test="${performDTO} != null">
  <!-- null을 {} 바깥에 쓰면 안됨. 안에 써줘야 함! -->
  <div class="test">performDTO는 null이 아니다!</div>
</c:if>
```

&nbsp;&nbsp; => 이처럼 { } 안에서 비교해줘야지, { } 밖에서 비교하면 안된다. <br><br><br>

- 넘어온 객체가 자바빈(JavaBean)의 형태라면, 아래와 같이 값을 뽑아내면 된다.

```jsp
<c:out value="${performDTO.perform_num }" />
<c:out value="${performDTO.perform_title }" />
<c:out value="${performDTO.location }" />
```

<br>

- `<c:out>`으로 보여주는 것 대신, 코드라인 위쪽에서 `<c:set>`으로 변수에 넣은 뒤 아래에선 EL표기법으로 보여주는게 훨씬 보기 깔끔하고 유지보수가 더 편할 듯 하다. 프론트, 백 업무분담하기도 편해보이고.

```jsp
// 이전 코드라인
관람시간: <c:out value="${performDTO.running_time }" />분
(인터미션<c:out value="${performDTO.intermission }" />  분)
```

```jsp
// 바꾼 코드라인
<c:set var="runningTime" value="${performDTO.running_time }" />
<c:set var="intermission" value="${performDTO.intermission }" />


관람시간: ${runningTime}분 (인터미션 ${intermission}분)
```

---
