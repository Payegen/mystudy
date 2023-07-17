# diff 虚拟dom

先看看虚拟节点的表示方式和dom的

```js
//js对象
{
    'sel':'div',
    'data':{
        "class":{ "box": true},
    },
    "children":[
        {
            'sel':'h3',
            "text":'biaoti'
        },
        {
            'sel':'li'
        }
    ]
}
//dom
<div>
	<h3/>
    <li/>
</div>
```

虚拟节点有哪些属性：

```js
{
    children: undefined
    data:{}
    elm:
    key:
    sel:""
    text:
}
```



}

snabbdom库中h函数提供讲参数渲染成虚拟节点，patch函数让虚拟节点上树，渲染到页面当中.

文档参考：[snabbdom中文文档](https://github.com/snabbdom/snabbdom/blob/master/README-zh_CN.md)

```js
//h函数的使用,可以嵌套
const vnode = h('ul',[
    h('li','苹果')，
    h('li','香蕉')，
	h('li',[
        h('div',[
            h('p','11')
            h('p','22')
        ])
    ])
]);

//创建出patch函数
const patch = init([classModule,propsModule,styleModule,eventListenersModule])

//渲染上树
patch(document.getelementbyid('app'),vnode)
```



## 虚拟dom如何被渲染



手写h函数：



## diff原理

### diff最小量更新:

1.这里插入一个li来演示

情况1，新节点会在最后面添加，这里前三个，a,b,c是不会改变的

情况2，增加的d是出现在第一个，但是后面的abc都发生了变化，每次运行patch的时候都是将`a->d`,`b->a`类推 因此这种跟新方式并不好。

```js
old = h('ul',{},[
    h('li',{},'a')
    h('li',{},'b')
    h('li',{},'c')
])
// 1。
new = h('ul',{},[
    h('li',{},'a')
    h('li',{},'b')
    h('li',{},'c')
    h('li',{},'d')
])
// 2。
new = h('ul',{},[
    h('li',{},'d')
    h('li',{},'a')
    h('li',{},'b')
    h('li',{},'c')
])
patch(old,new)
```

2.对于这种情况给每个{}添加key,此时跟新的时候根据key来判断，我们需要改变的只是添加d在a的上面

> key是节点的唯一标识，告诉diff算法，更改前后他们是同一个节点

```js
old = h('ul',{},[
    h('li',{key:'a'},'a')
    h('li',{key:'b'},'b')
    h('li',{key:'c'},'c')
])

new = h('ul',{},[
    h('li',{key:'d'},'d')
    h('li',{key:'a'},'a')
    h('li',{key:'b'},'b')
    h('li',{key:'c'},'c')
])
patch(old,new)
```

3.只有同一个虚拟节点（选择器相同，key相同），才会精细的比较，否则就会暴力删除旧的，插入新的。

```js
//此时就会移除ul,插入ol的内容到里面
old = h('ul',{},[
    h('li',{key:'a'},'a')
    h('li',{key:'b'},'b')
    h('li',{key:'c'},'c')
])

new = h('ol',{},[
    h('li',{key:'d'},'d')
    h('li',{key:'a'},'a')
    h('li',{key:'b'},'b')
    h('li',{key:'c'},'c')
])
```

4.跨层也会暴力移除，只能同层的比较。

> 最后两种正常情况不会用到，因此比较合理 

## 虚拟dom如何通过diff如何变成真正的dom