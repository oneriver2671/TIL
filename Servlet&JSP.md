## Servlet에서 session 사용하기

- 아래는 JSP페이지에서 session에 넣어둔 값이다.

```jsp
session.setAttribute("id", id);
session.setAttribute("memberName", name);
```

- Servlet의 Controller로 이동했는데, 여기서 이 session을 다루고 싶었음.

```java
HttpSession session = request.getSession();      // 이걸 써주면 된다!

System.out.println(session.getAttribute("id"));
System.out.println(session.getAttribute("memberName"));
```

<br>

### session값 삭제

- 이를 활용해서, 포폴 '티켓예매'가 완료된 후 session값 삭제를 Controller에서 할 수 있었다.

```java
// 예약 간 사용된 '공연정보' 관련 session 삭제.
HttpSession session = request.getSession();
session.removeAttribute("performDTO");
session.removeAttribute("performSeatDTO");
```

- 위의 session 값들은 JSP페이지에서 아래와 같이 추가되었었음.

```jsp
// 티켓 예매 시 계속 필요해서, 일단 session에 넣어보기로.
session.setAttribute("performDTO", performDTO);
session.setAttribute("performSeatDTO", performSeatDTO);
```

<br>

---

session에 넣는게 서버 과부하 때문에 별로 좋은 것은 아닌데, 애초에 티켓예매 페이지를 5개로 나눠 설계한 것이 골치아파져 일단 session으로 처리했다.

(나중에 forward를 활용해 request가 유지되며 넘어갈 수 있게 수정해보는 걸로. 그럴려면 먼저 티켓예매 페이지를 한 페이지로 통일해야할 듯.)
