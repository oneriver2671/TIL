###22.08.01(월)
- public 폴더의 image 사용할 경우, `process.env.PUBLIC_URL`을 붙여주자.

```jsx
{/**public의 img 사용 시 */}
<img src={process.env.PUBLIC_URL + '/logo192.png'} width="80%"></img>
```

###22.07.30(토)
## onChange / onInput

- `v-on:change`와 같은 기능인가보다.
- 이벤트 핸들링 : 30개 정도나 되니, 다 외우긴 어렵고 그때 그때 찾아쓰기

### 이벤트 버블링 / 이벤트 캡처링

- 이벤트 버블링: 자식 요소에서 발생한 이벤트가 부모 요소로 전파하는 것
- 이벤트 캡처링: 자식 요소에서 발생한 이벤트가 부모 요소부터 시작하여 이벤트를 발생시킨 자식 요소까지 도달하는 것
- `e.stopPropagation()` : 이벤트 버블링을 막아주는 코드.
  


## class를 사용하는 옛날 React 문법

```jsx
class Modal2 extends React.Component {
  // 채워야 할 3가지: constructor, super, render
  constructor(props){
    super(props);
    this.state = {
      name: 'kim',
      age: 20
    }
  }
  render(){
    return (
      <div>안녕 {this.state.name}, {this.state.age}
        <button onClick={()=>{
          this.setState({age: 21})
        }}>나이 수정 버튼</button>
      </div>
    )
  }
}
```