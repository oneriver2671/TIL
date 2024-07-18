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

<br>

## REST API

> **HTTP 프로토콜을 HTTP답게 사용하기 위해.**

- 개발자들 사이에 널리 지켜지는 약속. 특정 형식임. 기술을 의미하는 것이 아님.
- REST API에서 CRUD를 위해 준비된 `method`들은?

  ⇒ GET, POST, PUT, DELETE 등 사용.

  - GET : 데이터 Read, 조회용
  - POST : Create용
  - PUT, PATCH : Update용 (전체는 put, 부분은 patch)
  - DELETE : 삭제용

> **<가장 중요한 REST API의 특성>**
>
> - 각 요청이 어떤 동작이나 정보를 위한 것인지를 그 요청의 모습 자체로 추론 가능하다는 것.
> - 요청을 보내는 주소(URI)만으로도 대략 이게 뭐를 하는건지 알 수 있는. 단순히 기능만 되는 것이 아니라.
>   - URI는 동사가 아니라 명사로 적어야한다.

<br>

### 기존 @Controller와 @RestController의 차이

> **@RestController = @Controller + @ResponseBody**

전통적인 @Controller는 View를 반환하기 위해 주로 사용됨. But, Data를 반환해야 하는 경우도 있다. 이럴 때 `@ResponseBody`를 사용해 Json형태로 객체 데이터를 반환한다.

⇒ @RestController를 통해 좀 더 편하게.

- 기존 Controller 예시

  ```java
  @PostMapping(value = "/info")
  public @ResponseBody User info(@RequestBody User user){
  	 return userService.retrieveUserInfo(user);
  }
  ```

- @RestController가 Data를 반환하기 위해서는 ViewResolver 대신에 HttpMessageConverter가 동작한다.
- 결과 데이터 + HTTP 상태 코드를 함께 제어해 반환하는게 좋다!

<br><br>

❓ 음. data만 반환하는건 좋아. 근데, 그걸 아무튼 잘 꾸며진 jsp페이지에서 띄우는건데. 데이터만 보여주는게 아니잖아? ajax를 활용한다치면, jsp 새로운 페이지 만들필요가 없는???

일단 READ를 어떻게 jsp페이지에 예쁘게 띄워주는지 궁금하군..

- 해결

  - 만약 `@RestController`에서 jsp페이지를 리턴하고 싶다면, `ModelAndView`를 쓰면 된다.

  > _"RestController 라도 Ajax 통신만을 위한 컨트롤러는 아니고 Ajax 통신도 좀 더 수월하게 처리 해서 편하게 리턴하려고 나온거라, 기본 컨트롤러에 추가 된 거라고 보시면 될 듯 하네요."_

  > _"RestController는 ajax 요청일때만 json으로 리턴해주는 형태이기때문에, 페이지를 이동하시면서 로직처리를 하시는경우는 일반 컨트롤러를 태우셔야합니다."_

  ⇒ 아! 주로 ajax 비동기식으로 데이터만 json 형태로 리턴해줄 때 사용하는 편이구나.
  (그래서 책에 '댓글' 예제가 있었구나.)
