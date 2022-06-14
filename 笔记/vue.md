vue事件对象

```
$event  原生得事件参数
```

#### 事件修饰符

```
@click.prevent=""
```

![image-20220123234518898](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220123234518898.png)

#### v-model指令

只能与表单元素进行数据绑定

1. input

2. select : 

   ```
   <select v-model="city">
   <option value="1">xxxxx  </....>
   ...
   <option value="n">xxxxx  </....>
   ...
   </select>
   ```

   ##### model指令修饰符：

   ![image-20220123235829964](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220123235829964.png)

   

#### v-bind

用来绑定元素属性的



```
:style{backgroud:" red" }
//简写
```



```
v-bind: src="url"  //这里src就是我们再data中的数据了

data{
  url:"....."
}
```

#### 过滤器

```
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



**方法监听**

```
监听器就是监听数据变化的，要监视那个数据就把它名字当作方法的名字
data:{
	msg
}
watch:{
	msg(newVal,oldVal){
		//新值在前，旧值在后
	}
}
```

> 缺点：  不能一进去就调用监听器



**对象监听器**

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

```
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

```
computed:{
	rgb:function(){
	 	return "结果"
	}
}
```



#### axios

一个专注网络请求的库

```
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

**详情看视频和官方文档进一步学习**



#### vue-cli

vue create projectName





#### 组件

三大结构：

- template

- srcipt

- style

  注意vue组件中的data必须是个函数

```
data(){
	return {
		username : "xxx"
	}
}，
methods:{
	
}
```

##### 组件的使用：

1. import导入

2. components声明 

   ```
   components:{
   	COM1
   }
   //与data,methods平级
   ```

3. 标签的形式去使用

   ```
   <COM1>
   ```

   > 注意 components注册的是私有组件

   再A中注册B，b就不能C中再注册了

##### 注册全局组件

再main.js中，通过Vue.component()可以注册全局组件

![image-20220124015323772](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220124015323772.png)

```
import Me from "./components/MyCom"

Vue.component("MyCom",Me)
```



#### props

  props是自定义属性，可以通过自定义属性来定义属性 为当前 组件的初始值

```
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

```
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