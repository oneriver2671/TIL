## REST 방식

> REST (Representational State Transfer) : 하나의 URI는 하나의 고유한 리소스(Resource)를 대표하도록 설계된다는 개념에 전송방식을 결합해서 원하는 작업을 지정하는 방식.

- 스프링 어노테이션 : `@RequestMapping` , `@ResponseBody` 등 사용

  - `@RestController` : Controller가 REST 방식을 처리하기 위한 것임을 명시. 메서드의 리턴 타입으로 사용자가 정의한 클래스 타입을 사용할 수 있다.
  - `@ResponseBody` : 일반적인 JSP와 같은 뷰로 전달되는 것이 아니라, 데이터 자체를 전달하기 위한 용도.
  - `@ReqeustBody` : JSON 데이터를 원하는 타입으로 바인딩 처리

- 서버에서 전송하는 것이 '순수한 데이터'이다.
- 기존의 Controller와는 조금 다르게 동작함.

<br>

- **HTTP의 전송방식**
  - Create : POST 방식
  - Read : GET 방식
  - Update : PUT 방식
  - Delete : DELETE 방식
