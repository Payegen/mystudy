# vue

## 1

vue事件对象
> $event  原生得事件参数

### 基础使用

```js
//事件修饰符
@click.prevent=""
```

![image-20220123234518898](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220123234518898.png)

#### v-model指令

只能与表单元素进行数据绑定

1. input

2. select :

   ```js
   <select v-model="city">
   <option value="1">xxxxx  </....>
   ...
   <option value="n">xxxxx  </....>
   ...
   </select>
   ```

##### model指令修饰符

   ![image-20220123235829964](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220123235829964.png)

#### v-bind

用来绑定元素属性的

```js
:style{backgroud:" red" }
//简写
```

```js
v-bind: src="url"  //这里src就是我们再data中的数据了

data{
  url:"....."
}
```

#### 过滤器

```js
{{  msg | fif }}
data{
  msg: "..."
}
filters:{
 //val 就是管道前的那个值
 fif(val){
  console.log( val );
  //这样我们就可以操作msg 的值
  
  return "我们处理后的结果"
 }
}
```

#### 监听器

1. 方法监听

    ```js
    //监听器就是监听数据变化的，要监视那个数据就把它名字当作方法的名字
    data:{
        msg
    }
    watch:{
        msg(newVal,oldVal){
    //新值在前，旧值在后
    }
    }
    ```

    > 缺点：不能一进去就调用监听器

2. 对象监听器

> 方案：使用immediate:true

```vue
watch:{
 msg:{
  handler(new , old){
  
  },
  immediate:true
  //这里添加一个属性，并把方法改为一个对象。
  immediate默认为false ，为true为一进去就开始监听一次
 }
}
```

> deep

```js
data{
 info:{
  msg:"..."
 }
}

watch:{
 handler(newVal){
  
 },
 deep:true
 //深度监听器，开启后，对象中任意的属性发生了变化就回触发侦听了
}
```

#### 计算属性

```js
computed:{
 rgb:function(){
  return "结果"
 }
}
```

#### axios

一个专注网络请求的库

```js
const result = axios({
//请求方式
    method:'',
//请求地址
    url:'  ',
//用于get请求
    params:{
        id:1
    },
//用于post
    props：{}
})

result.then(function(e){
//e为请求成功后的结果
})
```

#### vue-cli

`vue create projectName`

#### 组件

三大结构：

- template

- srcipt

- style

  注意vue组件中的data必须是个函数

```js
data(){
 return {
    username : "xxx"
 }
}，
methods:{

}
```

##### 组件的使用

1. import导入

2. components声明

   ```js
   components:{
    COM1
   }
   //与data,methods平级
   ```

3. 标签的形式去使用

   ```js
   <COM1>
   ```

   > 注意 components注册的是私有组件

   再A中注册B，b就不能C中再注册了

##### 注册全局组件

再main.js中，通过Vue.component()可以注册全局组件

![image-20220124015323772](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220124015323772.png)

```js
import Me from "./components/MyCom"

Vue.component("MyCom",Me)
```

#### props

  props是自定义属性，可以通过自定义属性来定义属性 为当前 组件的初始值

```js
exprot default {
 props：['init'],
 data(){
  return {
   count:0
  }
 }
}


-------------在我们组件标签可以直接传值----------------------
<MyCom init='1' >
```

props可以直接在模板使用,

> props是只读的!

如果想修改props的值，我们可以把props的值传到data当中

```vue
<template>
<h1>{{init}}</h1> //直接显示props的值
<button @click="count +=1"> +1 </button>
</.....>


<script>
exprot default {
 props：['init'],
 data(){
  return {
   count: this.init
  }
 },
 methods:{
 
 }
}
<script>
```

##### props的默认值

```js
props:{
 //自定义属性A:{ 默认属性 }
 //自定义属性B:{ 默认属性 }

 init:{
  dafault: 0
  //如果外界没传入init属性，则为默认值0
  
  type: Number / String... 
  //type指定传入类型
  
  required:true
  //必传项校验
 }

}
```

> 就是改成了对象类型

#### *样式冲突问题（102-103）

#### ref 119

#### 动态组件

```js
<component  :is="comName"></component>


data(){
 return {
  comName: '组件名字'
 }
}
```

> 切换组件的时候回销毁

##### keep-alive

如果要保存状态需要在动态标签外面包裹一层 keep-aliveb标签

```js
<keep-alive>
 <component></component>
 //
</keep-alive>
```

生命周期函数

```js
    activated(){
 //被激活状态
    },
    deactivated(){
 //被缓存状态
    }
```

##### include属性

```js
<keep-alive include='com1,com2'>
//include指定需要被缓存的组件,exclude排除属性
```

#### 插槽

把不确定的部分，用户自定义的部分作为插槽`<slot>`

相当于一个占位符

> 插槽需要指定一个name属性名称 不指定则为默认default

```html
<template v-slot:default>
    <p> 用来替换插槽的内容 必须包裹在template标签里，v-slot与插槽的name属性一样  </p>
</template>

简写为
<template #default>
    <p>...</p>
</template>
```

插槽可以设置默认值，在组件封装的时候直接在
`<slot>这里搞默认值</slot>`

##### 具名插槽

有多个插槽的时候每个插槽提供一个name

对应我指定渲染到哪个插槽里面

##### 作用域插槽

`<slot name="comp1" msg="这是一条信息">`

```js
<template #com1="scope">

{{scope.msg}}  //这样获取我们预留在插槽的信息为作用域插槽

</template>
```

解构赋值:

```js
<slot name="comp1" msg="这是一条信息" user="xx">
<template #com1="{msg,user}">
对应名字直接拿过来用
```

#### 自定义指令 @116

### 组件之间传值

#### 兄弟组件传值

1. 创建vue实例，并导出实例

    ```js
    import Vue from 'vue'

    export default new Vue()
    ```

2. 发送方

    ```js
    import bus from './bus.js'

    bus.$emit('share',obj)
    ```

3. 接收方

    ```js
    import bus from './bus.js'

    bus.$on('share', val => {
        //val就是数据
    })
    ```

#### 子向父传值

>使用自定义事件

1. 子组件在方法中触发自定义事件

    ```js
    method:{
        add(){
            this.$emit('change',obj)
        }
    }
    ```

2. 父组件监听事件

    ```js
    <son @change="fun"></som>

    export default{
        method:{
            fun(val){
                //val就是传递的数据
            }
        }
    }
    ```

#### 父向子传值

1. 子组件

    定义props

2. 父组件

    在子标签里面对props传值
