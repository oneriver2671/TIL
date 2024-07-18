# 빈 생명주기 콜백

데이터베이스 커넥션 풀이나, 네트워크 소켓처럼 애플리케이션 시작 시점에 필요한 연결을 미리 해두고, 애플리케이션 종료 시점에 연결을 모두 종료하는 작업을 진행하려면, 객체의 초기화와 종료 작업이 필요하다.

> 스프링 빈은 간단하게 다음과 같은 라이프사이클을 가진다. <br>
**객체 생성 ⇒ 의존관계 주입**

스프링 빈은 객체를 생성하고, 의존관계 주입이 다 끝난 다음에야 필요한 데이터를 사용할 수 있는 준비가 완료된다. 그래서 초기화 작업은 의존관계 주입이 모두 완료되고 세팅이 다 끝난 후에 호출해야 한다. 그런데, 개발자가 의존관계 주입이 모두 완료된 시점을 어떻게 알 수 있을까?

**스프링은 의존관계 주입이 완료되면 스프링 빈에게 콜백 메서드를 통해서 초기화 시점을 알려주는 다양한 기능을 제공**한다.

또한 **스프링은 스프링 컨테이너가 종료되기 직전에 소멸 콜백을 준다.** 따라서 안전하게 종료 작업을 진행할 수 있다.

> **스프링 빈의 이벤트 라이프사이클 💡** <br>
스프링 컨테이너 생성 → 스프링빈생성 → 의존관계주입 → 초기화 콜백 → 사용 → 소멸전 콜백 → 스프링 종료

> 📌 참고 : **객체의 생성과 초기화를 분리**하자.
생성자 안에서 무거운 초기화 작업을 함께 하는 것보다는 **객체를 생성하는 부분과 초기화 하는 부분을 명확하게 나누는 것**이 유지보수 관점에서 좋다. 

<br>

### **스프링의 빈 생명주기 콜백 지원방법 3가지**

1. 인터페이스(InitializingBean, DisposableBean)
2. 설정 정보에 초기화 메서드, 종료 메서드 지정
3. `@PostConstruct`, `@PreDestroy` 어노테이션 지원

<br>

## 인터페이스 InitializingBean, DisposableBean

- `InitializingBean` 은 `afterPropertiesSet()` 메서드로 초기화를 지원한다.
- `DisposableBean` 은 `destroy()` 메서드로 소멸을 지원한다.

🔽 예제 (test/../lifecycle/NetworkClient.java)  

```java
@Override
	public void afterPropertiesSet() throws Exception {		// 의존관계 주입이 끝나면 초기화하겠다는 메서드.
		connect();
		call("초기화 연결 메시지");
		
	}

	@Override
	public void destroy() throws Exception {
		disconnect();
		
	}
```


**초기화, 소멸 인터페이스 단점**

- 이 인터페이스는 스프링 전용 인터페이스이므로 코드가 스프링 전용 인터페이스에 의존한다.
- 초기화, 소멸 메서드의 이름을 변경할 수 없다.
- 내가 코드를 고칠 수 없는 외부 라이브러리에 적용할 수 없다.

> 📌 참고 : 인터페이스를 사용하는 초기화, 종료 방법은 스프링 초창기에 나온 방법들이고 지금은 다음의 더 나은 방법들이 있어서 거의 사용하지 않는다.

<br>

## 빈 등록 초기화, 소멸 메서드

```java
@Bean(initMethod = "init", destroyMethod = "close")
	// 여기서 "init", "close"는 내가 만든 메서드 이름임.
```

🔽 예제의 테스트 코드에서 사용 (test/../lifecycle/BeanLifeCycleTest.java)  

```java
public class BeanLifeCycleTest {
	
	@Test
	public void lifeCycleTest() {
		ConfigurableApplicationContext ac = new AnnotationConfigApplicationContext(LifeCycleConfig.class);
		NetworkClient client = ac.getBean(NetworkClient.class);
		ac.close();		// 이 close() 메소드를 쓰기 위해 ConfigurableApplicationContext를 사용함.
		
	}
	
	@Configuration
	static class LifeCycleConfig{
		
		@Bean(initMethod = "init", destroyMethod = "close")		// 빈 등록 '초기화, 소멸' 메서드 사용
		public NetworkClient networkClient() {
			NetworkClient networkClient = new NetworkClient();
			networkClient.setUrl("http://hello-spring.dev");   // 그냥 가짜로 아무거나 씀.
			return networkClient;
		}
	}

}
```

### **설정 정보 사용의 장점**

- 메서드 이름을 자유롭게 줄 수 있다.
- 스프링 빈이 스프링 코드에 의존하지 않는다.
- 코드가 아니라 설정 정보를 사용하기 때문에 **코드를 고칠 수 없는 외부 라이브러리에도 초기화, 종료 메서드를 적용할 수 있다. ★**


### 종료 메서드의 추론 기능 ★

⇒ *`@Bean`으로 등록했을 때만 발생한다.*

- `@Bean`의 `destroyMethod` 속성에는 아주 특별한 기능이 있다.
- `@Bean`의 `destroyMethod` 는 기본값이 (inferred-추론)으로 등록되어 있다.
- 이 추론 기능은 `close` , `shutdown` 라는 이름의 메서드를 자동으로 호출해준다.
- **따라서, 직접 스프링 빈으로 등록하면 종료 메서드는 따로 적어주지 않아도 잘 동작한다.**

(추론 기능을 사용하기 싫으면 `destroyMethod=""` 처럼 빈 공백을 지정하면 됨)

<br>

## ✔ 어노테이션 @PostConstruct, @PreDestroy

> 결론부터 말하자면, **그냥 이걸 쓰면 된다.** 스프링에서도 권장하는 방법 ★

예제에 `@PostConstruct`, `@PreDestory` 추가 (test/../lifecycle/NetworkClient.java) 🔽 

```java
@PostConstruct
public void init() {		// 의존관계 주입이 끝나면 초기화하겠다는 메서드.
	System.out.println("init");
	connect();
	call("초기화 연결 메시지");	
}

@PreDestroy
public void close()  {
	System.out.println("close");
	disconnect();
}
```

**`@PostConstruct`, `@PreDestroy` 애노테이션의 특징**

- 이 두 애노테이션을 사용하면 가장 편리하게 초기화와 종료를 실행할 수 있다.
- 최신 스프링에서 가장 권장하는 방법으로 애노테이션 하나만 붙이면 되므로 매우 편리하다.
- 패키지를 보면 `javax.annotation.PostConstruct` 이다.스프링에 종속적인 기술이 아니기 때문에 스프링이 아닌 다른 컨테이너에서도 동작한다.
- 유일한 단점💡: 외부 라이브러리에는 적용하지 못한다는 것. 외부 라이브러리를 초기화, 종료 해야하면 위의 2번째 방법인 `@Bean`의 initMethod , destroyMethod를 사용하자.