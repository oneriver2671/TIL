# 의존관계 자동주입

### **의존관계 주입의 4가지 방법**

1. **생성자 주입**
2. **수정자 주입(setter 주입)**
   - Setter 메서드 기반
3. **필드 주입**

   > ⇒ 코드가 간결해서 많은 개발자들을 유혹하지만 외부에서 변경이 불가능해서 테스트 하기 힘들다는 **치명적인 단점**이 있다. 사용하지 말자. <br>
   > (애플리케이션의 실제 코드와 관계 없는 **테스트 코드**나,
   > 스프링 설정을 목적으로 하는 @Configuration 같은 곳에서만 특별한 용도로 사용.)

4. **일반 메서드 주입**
   - 일반 메서드를 통해서 주입 받을 수 있다.
   - 한번에 여러 필드를 주입 받을 수 있다.
   - 일반적으로 잘 사용하지 않는다.

<br>

### 생성자 주입

- 생성자 호출 시점에 **딱 1번만 호출되는 것이 보장된다.** <br>
  (그 때 값을 세팅하고 그 다음부터는 세팅을 건들지 못하게 막을 수 있음)
- **불변, 필수 의존관계**에서 사용함.

> **생성자가 딱 1개만 있으면, `@Autowired`를 생략해도 자동 주입이 된다.**
> 물론 스프링 빈에만 해당.

> `final` 붙여 만든 필드는 '필수' 요소

<br>

### 수정자 주입

setter라 불리는 필드의 값을 변경하는 수정자 메서드를 통해서 의존관계를 주입하는 방법이다.

- 특징
  - **선택, 변경 가능성이 있는 의존관계**에 사용함.
  - 자바빈 프로퍼티 규약의 수정자 메서드 방식을 사용하는 방법이다.

```java
@Component
public class OrderServiceImpl implements OrderService {

    private MemberRepository memberRepository;
    private DiscountPolicy discountPolicy;

    @Autowired
    public void setMemberRepository(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
    @Autowired
    public void setDiscountPolicy(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
```

> 📌 참고: `@Autowired` 의 기본 동작은 주입할 대상이 없으면 오류가 발생한다. 주입할 대상이 없어도 동작하게하려면 `@Autowired(required = false)` 로 지정하면 된다.

> 📌 참고: **의존관계 자동 주입**은 스프링 컨테이너가 관리하는 스프링 빈이어야 동작한다.
> 스프링 빈이 아닌 Member 같은 클래스에서 `@Autowired` 코드를 적용해도 아무 기능도 동작하지 않는다.
> (아래 '옵션 처리'에서 예제로 다뤄보자.)

<br>

## 옵션 처리

---

주입할 스프링 빈이 없어도 동작해야 할 때가 있다.
그런데 @Autowired 만 사용하면 required 옵션의 기본값이 true 로 되어 있어서 자동 주입 대상이 없으면 오류가 발생한다.

- **자동 주입 대상을 옵션으로 처리하는 방법**
  1. `@Autowired(required=false)` : 자동 주입할 대상이 없으면, 수정자 메서드 자체가 호출이 안됨
  2. `org.springframework.lang.@Nullable` : 자동 주입할 대상이 없으면, null이 입력됨
  3. `Optional<>` : 자동 주입할 대상이 없으면, Optional.empty가 입력된다. (Java 8 지원 문법)

🔽 예제 (test/../autowired/AutowiredTest.java)

```java
public class AutowiredTest {
	@Test
	void AutowiredOption() {
		ApplicationContext ac = new AnnotationConfigApplicationContext(TestBean.class);
	}

	static class TestBean{
		@Autowired(required = false)	  // 아예 호출 자체가 안되게.
		public void setNoBean1(Member noBean1) {	// Spring 컨테이너와 관련없는 Member를 넣어봄.
			System.out.println("noBean1 = " + noBean1);
		}

		@Autowired
		public void setNoBean2(@Nullable Member noBean2) {
			System.out.println("noBean2 = " + noBean2);		// 호출은 되는데, null로 값이 들어옴.
		}

		@Autowired
		public void setNoBean3(Optional<Member> noBean3) {
			System.out.println("noBean3 = " + noBean3);     // Optional.empty 출력.
		}
	}
}
```

<br>

## 생성자 주입을 선택해야 하는 이유

---

1. **불변**
   - 대부분의 의존관계 주입은 한번 일어나면, 애플리케이션 종료시점까지 의존관계를 변경할 일이 없다.
     생성자 주입은 객체를 생성할 때 딱 1번만 호출되므로 이후에 호출되는 일이 없다. 따라서 불변하게 설계할 수 있다.
2. **누락**
   - 프레임없이 순수 자바 코드로 단위 테스트를 진행하는 경우가 생각보다 많다. 이 때, '수정자 주입'을 사용하면 테스트에서 의존관계 누락이 발생하기 쉽다. 의존관계가 한눈에 보이지 않기 때문.
3. **final 키워드**

   - 생성자 주입을 사용하면 **필드에 `final` 키워드를 사용할 수 있다.** 생성자에서 혹시라도 값이 설정되지 않는 오류를 컴파일 시점에 막아준다.

     ```java
     @Component
     public class OrderServiceImpl implements OrderService {
         // final 사용
         private final MemberRepository memberRepository;
         private final DiscountPolicy discountPolicy;

         @Autowired
         public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
             this.memberRepository = memberRepository;
             this.discountPolicy = discountPolicy;
         }
         .
         .
     ```

     ⇒ 이럴 경우, 실수로 생성자에서 값을 설정해주지 않으면 `final` 키워드로 인해 컴파일 오류가 발생함.

> 📌 참고 : 수정자 주입을 포함한 나머지 주입 방식은 모두 생성자 이후에 호출되므로, 필드에 final 키워드를 사용할 수 없다.
> **오직 생성자 주입 방식만** final 키워드를 사용할 수 있다.

> **항상 생성자 주입을 선택해라! 그리고 가끔 옵션이 필요하면 수정자 주입을 선택해라. 필드 주입은 사용하지 않는게 좋다.**

<br>

## 롬복

---

**롬복이란?**

- `getter` `setter` 메서드를 자동으로 만들어준다.  `@Getter`, `@Setter` 어노테이션만 있으면 편하게 사용 가능)
- 생성자 관련한 부분도 편리하게 사용 가능. ⇒ `@RequiredArgsConstructor`를 사용하면 밑에 생성자 부분 자동으로 만들어줌.
- 실무에서 정말 많이 사용함.
- OrderServiceImple 기존 세팅 🔽

  ```java
  @Component
  public class OrderServiceImpl implements OrderService {

  	// 1) 인터페이스에만 의존하도록 변경
  	private final MemberRepository memberRepository;
  	private final DiscountPolicy discountPolicy;

  	// 2) 생성자 생성
  	@Autowired    // 생성자 주입
  	public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
  		super();
  		this.memberRepository = memberRepository;
  		this.discountPolicy = discountPolicy;
  	}
  ```

> 참고: Spring Boot 만드는 start.io에서, 롬복 의존성 추가 선택 가능함.

> 이클립스나 인텔리제이나 사용하려면 추가 설정이 필요함.

<br>

## 조회 빈이 2개 이상이 되버리는 경우

---

> `@Autowired`는 **타입**으로 조회한다. 📌

DiscountPolicy 인터페이스의 하위 타입인 FixDiscountPolicy , RateDiscountPolicy 둘 다를 스프링 빈으로 선언해보면 어떻게 될까?

```java
@Component
  public class FixDiscountPolicy implements DiscountPolicy {}
```

```java
@Component
  public class RateDiscountPolicy implements DiscountPolicy {}
```

⇒ `NoUniqueBeanDefinitionException` 예외가 발생한다.

이와 같은 문제가 생길 경우, 의존 관계 자동 주입에서 해결하는 여러 방법이 있다.

- **조회 대상 빈이 2개 이상일 때 해결 방법 3가지**

  1. `@Autowired` 필드명 매칭

     ```java
     // 기존
     @Autowired
     private DiscountPolicy discountPolicy
     ```

     ```java
     // 변경 후
     @Autowired
     private DiscountPolicy rateDiscountPolicy
     ```

  2. `@Qualifier`를 `@Qualifier`끼리 매칭 → 빈 이름 매칭

     @Qualifier 는 추가 구분자를 붙여주는 방법이다. 주입시 추가적인 방법을 제공하는 것이지, 빈 이름을 변경하는 것은 아니다.

     > 헷갈리니, 그냥 '@Qualifier는 @Qualifier를 사용하는 애들이랑만 쓰는게 좋다' 정도만 기억하자.

  3. `@Primary` 사용

     - 편하고 자주 사용함.
     - Primary 는**우선순위**를 정하는 방법이다. @Autowired 시에 여러 빈이 매칭되면 @Primary가 우선권을 가진다.

     ```java
     @Component
     @Primary
     public class RateDiscountPolicy implements DiscountPolicy {}
     ```

<br>

## 조회한 빈이 모두 필요할 때. List와 Map

🔽 예제 (test/../autowired/AllBeanTest.java) ★★

> 이 예제는 반복 학습 필요 💡

```java
// 조회한 빈이 모두 필요할 때 (List, Map)
public class AllBeanTest {

	@Test
	void findAllBean() {
		ApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class, DiscountService.class);


		DiscountService discountService = ac.getBean(DiscountService.class);
		Member member = new Member(1L, "userA", Grade.VIP);

		// 첫번째 테스트
		int discountPrice = discountService.discount(member, 10000, "fixDiscountPolicy");
		Assertions.assertThat(discountService).isInstanceOf(DiscountService.class);  // 당연히 받아졌겠지만, 그냥 만들어봄.
		Assertions.assertThat(discountPrice).isEqualTo(1000);

		// 두번째 테스트
		int rateDiscountPrice = discountService.discount(member, 20000, "rateDiscountPolicy");
		Assertions.assertThat(rateDiscountPrice).isEqualTo(2000);
	}


	// 테스트용으로 임의로 만든 클래스
	static class DiscountService {
		private final Map<String, DiscountPolicy> policyMap;
		private final List<DiscountPolicy> policies;

		@Autowired  // 참고로 생성자가 1개니 @Autowired 생략 가능.
		public DiscountService(Map<String, DiscountPolicy> policyMap, List<DiscountPolicy> policies) {
			this.policyMap = policyMap;
			this.policies = policies;
			// 아래와 같이 찍어보면, 여러개가 담겨 나오는걸 확인 가능.
			// (DiscountPolicy를 구현하는 클래스 2개가 다 @Component 처리가 되어 컨테이너에 담겨있기 때문)
			System.out.println("policyMap = " + policyMap);
			System.out.println("policies = " + policies);
		}

		// 아래 로직 ★
		public int discount(Member member, int price, String discountCode) {
			DiscountPolicy discountPolicy = policyMap.get(discountCode);

			return discountPolicy.discount(member, price);
		}
	}

}
```

### ✔️ 로직 분석

- `DiscountService`는 Map으로 모든 `DiscountPolicy`를 주입받는다.
- 이때 `fixDiscountPolicy`, `rateDiscountPolicy`가 주입된다.
- `discount()` 메서드는 `discountCode`로 `fixDiscountPolicy`가 넘어오면 map에서 `fixDiscountPolicy` 스프링 빈을 찾아서 실행한다. 물론 `rateDiscountPolicy`가 넘어온다면 `rateDiscountPolicy` 스프링 빈을 찾아서 실행한다.

### ✔️ 주입 분석

- `Map<String, DiscountPolicy>` : map의 키에 스프링 빈의 이름을 넣어주고, 그 값으로 `DiscountPolicy` 타입으로 조회한 모든 스프링 빈을 담아준다.
- `List<DiscountPolicy>` : `DiscountPolicy` 타입으로 조회한 모든 스프링 빈을 담아준다. 만약 해당하는 타입의 스프링 빈이 없으면, 빈 컬렉션이나 Map을 주입한다.

❓**새로 만든 `DiscountService`가 스프링 빈에 어떻게 담기지??**

<br>

### 수동 빈 등록은 언제 사용하면 좋을까?

애플리케이션은 크게 업무 로직과 기술 지원 로직으로 나눌 수 있다.

- **업무 로직 빈:** 웹을 지원하는 컨트롤러, 핵심 비즈니스 로직이 있는 서비스, 데이터 계층의 로직을 처리하는 리포지토리등이 모두 업무 로직이다. 보통 비즈니스 요구사항을 개발할 때 추가되거나 변경된다.
- **기술 지원 빈:** 기술적인 문제나 공통 관심사(AOP)를 처리할 때 주로 사용된다. 데이터베이스 연결이나, 공통 로그 처리 처럼 업무 로직을 지원하기 위한 하부 기술이나 공통 기술들이다.
- 업무 로직은 숫자도 매우 많고, 한번 개발해야 하면 컨트롤러, 서비스, 리포지토리 처럼 어느정도 유사한 패턴이 있다. 이런 경우 자동 기능을 적극 사용하는 것이 좋다. 보통 문제가 발생해도 어떤 곳에서 문제가 발생했는지 명확하게 파악하기 쉽다.
- 기술 지원 로직은 업무 로직과 비교해서 그 수가 매우 적고, 보통 애플리케이션 전반에 걸쳐서 광범위하게 영향을 미친다. 그리고 업무 로직은 문제가 발생했을 때 어디가 문제인지 명확하게 잘 들어나지만, 기술 지원로직은 적용이 잘 되고 있는지 아닌지 조차 파악하기 어려운 경우가 많다.

  > 그래서 이런 기술 지원 로직들은 가급적 수동 빈 등록을 사용해서 명확하게 들어내는 것이 좋다. 애플리케이션에 광범위하게 영향을 미치는 기술 지원 객체는 수동 빈으로 등록해서 딱! 설정 정보에 바로 나타나게 하는 것이 유지보수 하기 좋다.

- **정리** ✔
  - 편리한 자동 기능을 기본으로 사용하자.
  - 직접 등록하는 기술 지원 객체는 수동 등록하자.
  - 다형성을 적극 활용하는 비즈니스 로직은 수동 등록을 고민해보자.
