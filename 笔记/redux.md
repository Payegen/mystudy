## redux

### **actions**

1. **同步action**：

   用来创建一个根据用户输入在应用程序中发生的事件，并触发状态更新

   ```js
   //action返回的应该为一个obj
   const addAction = (data) => { data: data,type: 'add'}
   ```

   

2. **异步action**:

   延迟的动作不想交给组件自身，交给action来完成异步操作

   ```js
   //1.添加中间件 redux-thunk，配置到store中
   import {createStore,applyMiddleware} from 'redux'
   import thunk from 'redux-thunk'
   
   createStore(Rdeucer,applyMiddleware(thunk))
   
   //2. 创建异步action返回的不是一个对象，而是一个函数，在函数中写异步任务
   const AsyncAction = (data,time) => {
       return ()=>{
           setTimeout(()=>{
             
           },time)
       }
   }
   
   //3.异步任务有结果后分发一个同步的action去真正操作数据
   const AsyncAction = (data,time) => {
       return ()=>{
           setTimeout(()=>{
               store.dispatch(addAction(data))
           },time)
       }
   }
   ```

   

### react-redux

react-redux中提供了connect来进行UI组件和数据的结合

```js
connect(mapStateToProps,mapDispatchToProps)(Component)
/*
*1.第一个括号传入两个函数
*2.第二个传入组件
/
```



**mapStateToProps**函数的key就是传递给UI组件props的key，value就是props的value--状态

```js
function mapStateToProps(state){
    return {count:state}
}

//在组件中使用
function Count(props){
    return (
    	<h1> {this.props.count } </h1>
    )
}
```

**mapDispatchToProps**函数的key就是传递给UI组件props的key，value就是props的value--操作状态的方法

```js
//addAction为action
function mapDispatchToProps(dispatch){
    return {
        add: data => dispatch( addAction(data) )
    }
}


//简写方式：
function mapDispatchToProps(dispatch){
    return {
        add:  addAction
    }
}
```



## react-router

1.一级路由

```js
import {NavLink,Routes,Route} from 'react-router-dom'

fun App(){
    return (
    	//路由链接
        <NavLink className='' to='/about'>about </NavLink>
    	<NavLink className='' to='/home'>home </NavLink>
        
        
        //注册路由
        <Routes>
        	<Route path='/about' element={<About/>}>
        	<Route path='/home' element={<Home/>}>
        </Routes>
    )
}
```

2.重定向Navigate

```js
import {NavLink,Routes,Route,Navigate} from 'react-router-dom'

<Navigate to='/about' replace={ true|false } />
//只要渲染组件就会引起重定向
//to表示重定向的路径 ，replace 表示是否覆盖
    
//因为是组件所以可以在Route中使用
<Route path='/' element={<Navigate to='/about'/>}>  
```

3.点击高亮

```js
className={ (isActive)=> isActive ? 'x1': 'x2'}
```



4.路由表：
将Routes,Route写成配置表

```js
import {NavLink,useRoutes} from 'react-router-dom'


fun App(){
    const elements = useRoutes([
        {
            path:'about',
            element: <About/>
        },
        {
            path:'home',
            element: <Home/>
        }
    ])
	
    return (
    	//路由链接
        <NavLink className='' to='/about'>about </NavLink>
    	<NavLink className='' to='/home'>home </NavLink>
        
        //匹配的组件
        {elements}
    )
}
```

5.嵌套路由

```jsx
//1.
<Routes>
    <Route path='/fu' element={<Fu/>}>
        <Route path='/zi' element={<Zi/>}>
    </Route>
</Routes>
    
//2.路由表方式
    
import {Outlet} from 'react-router-dom' //占位组件
const elements = useRoutes([
        {
            path:'about',
            element: <About/>,
            chidlen:[
                {}
            ]
        }
    ]) 
使用 <Outlet/>占位


```



6.传参数

6.1 parms参数：

```jsx
//1.传参
<Link to = {`zi/${id}/${msg}`} ></Link>
//2.路由表定义参数
{
    path:'/',
    element:</Fu>,
    children:[
        {
            path:'zi/:id/:msg',
    		element:</Fu>,
        }
    ]
}

//3.接收参数
import {useParams} from 'react-router-dom'
function Zi(){
    
    const {id,msg} = useParams() 
    return (
        <h1>{id}-{msg}</h1>
    )
}
```

6.2 search参数

```jsx

//1.url传参
link to='zi?id=${msg}&msg=${msg}'

//2.获取参数
import {useSearchParams} from 'react-router-dom'
function Zi(){
    
    const [search,setSearch] = useSearchParams() 
    //search.get获取参数，setSearch用来更新参数（用的不多）
    const id = search.get('id')
    const msg = search.get('msg')
    
    return (
        <h1>{id}-{msg}</h1>
    )
}

```

6.3state

```jsx
//1.传参
<Link to='zi' state = { {id:'01',msg:'msg'} }>zi</Link>

//2.获取参数
import {useLocation} from 'react-router-dom'
function Zi(){
    
    const {state} = useLocation() 
    
    return (
        <h1>{state.id}-{state.msg}</h1>
    )
}
```

7.编程式导航

```jsx
import {useNavigate} from 'react-router-dom'

fun Zi(){
	const navigate = useNavigate()
    
    function go(){
        //第一个参数为路径，第二个为配置对象可以携带参数（可选）
        naviagate('path',{
            replace:false,
            state:{}
        })
        
        //前进|后退
        naviagate（ 1 | -1 ）
    }
}
```

8.其他路由hook

- useInRouterContext : 返回是否在路由上下文中
- useNavigationType : 返回如何来到当前页面的 `pop(刷新页面)`,`push`,`replace`
- useResolvedPath(): 给一个URL解析其中的：path,search,hash值