#### 动态组件

```
<component  :is="comName"></component>


data(){
	return {
		comName: '组件名字'
	}
}
```

>  切换组件的时候回销毁

##### keep-alive

如果要保存状态需要在动态标签外面包裹一层 keep-aliveb标签

```
<keep-alive>
	<component></component>
	//
</keep-alive>
```

**生命周期函数**

```
activated(){
	//被激活状态
},
deactivated(){
	//被缓存状态
}
```

##### include属性

```
<keep-alive include='com1,com2'>
指定需要被缓存的组件
exclude排除属性
```



#### 插槽

把不确定的部分，用户自定义的部分作为插槽**<slot>** 

相当于一个占位符

> 插槽需要指定一个name属性名称 不指定则为默认default

```xml
<template v-slot:default>
    <p> 用来替换插槽的内容 必须包裹在template标签里，v-slot与插槽的name属性一样  </p>
</template>


简写为
<template #default>
	<p>...</p>
</template>
```

插槽可以设置默认值，在组件封装的时候直接在

<slot> 这里搞默认值 </slot>

##### 具名插槽

有多个插槽的时候每个插槽提供一个name 

对应我指定渲染到哪个插槽里面

##### 作用域插槽

```
<slot name="comp1" msg="这是一条信息">
```

```
<template #com1="scope">

{{scope.msg}}  //这样获取我们预留在插槽的信息为作用域插槽

</template>
```

解构赋值:

```
<slot name="comp1" msg="这是一条信息" user="xx">
<template #com1="{msg,user}">
对应名字直接拿过来用
```

#### 自定义指令 @116