## ✔ 싱글톤 패턴

- 웹 어플리케이션의 특징: 요청이 들어오는 고객이 많다. → 객체를 무수히 많이 생성하게 됨. ⇒ 비효율적!! (메모리 낭비가 심하다)
- 해결: 해당 객체가 딱 1개만 생성되고, 공유되게 하면 됨. ⇒ **싱글톤 패턴**

### 싱글톤 패턴

- 클래스의 인스턴스가 딱 1개만 생성되는 것을 보장하는 디자인 패턴.
- 그래서 객체 인스턴스를 2개 이상 생성하지 못하도록 막아야 한다.
  ⇒ **private 생성자를 사용해서 외부에서 임의로 new 키워드를 사용하지 못하도록 막아야 한다**.

싱글톤 생성은 여러가지 방법이 있다.

- 객체를 미리 생성해두는 가장 안전하고 단순한 방법

```java
public class SingletonService {

	// 1. static 영역에 객체를 딱 1개만 생성해둔다.
	private static final SingletonService instance = new SingletonService();

	// 2. public으로 열어, 이 static 메서드를 통해서만 조회되도록 한다.
	public static SingletonService getInstance() {
		return instance;
	}

	// 3. 생성자를 private으로 해서, 다른 곳에서 new로 객체를 생성하지 못하게 막는다. ★★★
	private SingletonService() {
	}

	public void logic() {
		System.out.println("싱글톤 객체 로직 호출");
	}

}
```

- **싱글톤 패턴의 문제점**
  1. 싱글톤 패턴을 구현하는 코드 자체가 많이 들어간다.
  2. 의존관계상 클라이언트가 구체 클래스에 의존한다. DIP를 위반한다.
  3. 클라이언트가 구체 클래스에 의존해서 OCP 원칙을 위반할 가능성이 높다.
  4. 테스트하기 어렵다.
  5. 내부 속성을 변경하거나 초기화하기 어렵다.
  6. private 생성자로 자식 클래스를 만들기 어렵다.
  7. 결론적으로 유연성이 떨어진다.
  8. 안티패턴으로 불리기도 한다.

> 📌 **But! 스프링 컨테이너를 쓰면, 객체를 싱글톤으로 알아서 관리해준다.
> 위의 단점을 다 제거해줌!!**

<br>

## 싱글톤 컨테이너

- **스프링 컨테이너는 싱글톤 컨테이너 역할을 한다**.
  이렇게 싱글톤 객체를 생성하고 관리하는 기능을 싱글톤 레지스트리라 한다.
- 테스트 코드로 확인해보기

  ```java
  @Test
  	@DisplayName("스프링 컨테이너와 싱글톤")
  	void springContainer() {
  //		AppConfig appConfig = new AppConfig();
  		ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);


  		// 1. 조회: 호출할 때마다 객체를 생성
  		MemberService memberService1 = ac.getBean("memberService", MemberService.class);

  		// 2. 조회: 호출할 때마다 객체를 생성
  		MemberService memberService2 = ac.getBean("memberService", MemberService.class);

  		// 참조값이 다르단 것을 확인해보자.
  		System.out.println("memberService1 = " + memberService1);
  		System.out.println("memberService2 = " + memberService2);

  		// memberService1 != memberService2
  		Assertions.assertThat(memberService1).isSameAs(memberService2);
  	}
  ```

<Br>

## ✔ 싱글톤 방식의 주의점 ★★★

> 싱글톤 방식은 **여러 클라이언트가 하나의 같은 객체 인스턴스를 공유하기 때문에,** 싱글톤 객체는 상태를 유지(stateful)하게 설계하면 안된다.
> **무상태(stateless)로 설계해야 한다.**

- 특정 클라이언트에 의존적인 필드가 있으면 안된다.
- 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안된다.
- 가급적 읽기만 가능해야 한다.(가급적 값을 수정하면 안 된다)
- 필드 대신에 자바에서 공유되지 않는 `지역변수`, `파라미터,` `ThreadLocal` 등을 사용해야 한다.

- **예시 🔽**

  ```java
  public class StatefulService {

  	private int price;	// 상태를 유지하는 필드

  	public void order(String name, int price) {
  		System.out.println("name = " + name + ", price = " + price);
  		this.price = price;		// 이부분이 문제!
  	}

  	public int getPrice() {
  		return price;
  	}
  }
  ```

  ```java
  /* 싱글톤 방식의 주의점!! */
  class StatefulServiceTest {

  	@Test
  	void statefulServiceSingleton() {
  		ApplicationContext ac = new AnnotationConfigApplicationContext(TestConfig.class);
  		StatefulService statefulService1 = ac.getBean(StatefulService.class);
  		StatefulService statefulService2 = ac.getBean(StatefulService.class);

  		// Thread A: A사용자가 10000원 주문
  		statefulService1.order("userA", 10000);
  		// Thread B: B사용자가 20000원 주문
  		statefulService2.order("userB", 20000);

  		// Thread A: A사용자가 주문 금액을 조회
  		int price = statefulService1.getPrice();
  			// 이게 10000원이 나와야하는데, 20000원이 나옴.
  			// why? 같은 인스턴스를 쓰기 때문. statefulService1,2로 다른 필드지만 같은 객체임.

  		Assertions.assertThat(statefulService1.getPrice()).isEqualTo(20000);
  	}

  	static class TestConfig{

  		@Bean
  		public StatefulService statefulService() {
  			return new StatefulService();
  		}
  	}

  }
  ```

> **실무에서 이런 경우가 종종 생기는데, 이로인해 정말 큰 문제가 생긴다‼
> 실무는 굉장히 복잡한 멀티 쓰레드의 상황이라 찾기 쉽지 않다...
> ex) 다른 사람 결제내역 보이고, 실제 결제도 다른 사람 것으로 되고ㄷㄷ😱**

<br>

**✔ 지역변수를 통해 해결**

- 위의 코드를 아래와 같이 수정 **🔽**

  ```java
  public class StatefulService {

  //	private int price;	// 상태를 유지하는 필드

  	public int order(String name, int price) {
  		System.out.println("name = " + name + ", price = " + price);
  //		this.price = price;		// 이부분이 문제!

  		return price;   // void -> int로 바꾼 후 price 리턴해주기.
  	}

  //	public int getPrice() {
  //		return price;
  //	}
  }
  ```

- 리턴된 price를 아래와 같이 받아주면 된다. 지역변수라 둘이 값이 다름.

  ```java
  // Thread A: A사용자가 10000원 주문
  int userAPrice = statefulService1.order("userA", 10000);

  // Thread B: B사용자가 20000원 주문
  int userBPrice = statefulService2.order("userB", 20000);
  ```

<br>

## ✔ @Configuration과 싱글톤

`@Configuration` : 사실 싱글톤을 위해 존재하는 것임.

스프링은 클래스의 바이트코드를 조작하는 라이브러리를 사용한다.

> 💡 모든 비밀은 @Configuration 을 적용한 AppConfig에 있음.

`@Bean`이 붙은 메소드마다 이미 스프링 빈이 존재한다면, 존재하는 빈을 반환하고, 만약 없다면 생성해서 스프링 빈으로 등록하고 반환하는 코드가 동적으로 생성한다.

⇒ 덕분에 싱글톤이 보장된다.

> ✔ **정리**
>
> - `@Bean`만 사용해도 스프링 빈으로 등록되지만, 싱글톤을 보장하지는 않음.
> - 크게 고민하지 말고 스프링 설정 정보는 항상 `@Configuration` 을 사용하면 됨.
