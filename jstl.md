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
