# webpack相关

## 基础部分

简介：

5大核心概念：入口（entry），输出（output），加载器(loader)，插件(plugin)，模式(mode)

### 1.安装webpack

```
`npm ``install` `webapck webpack-cli --save-dev`
```

webpack 是打包代码时依赖的核心内容，而 webpack-cli 是一个用来在命令行中运行 webpack 的工具。

 webpack-cli 是用来处理命令行参数，并通过参数构建 compiler 对象，然后才是对代码进行打包的过程。**webpack-cli对于文件打包不是必需的**



### 2.搭建webpack服务器

> 开发模式是在内存当中进行的

启动webpack服务器

`npm i webpack-dev-server`

```js
devServer:{
    host:""
    port:""
    open:true //自动打开浏览器
}
```

### 3.**样式处理**

1. 使用预处理less或者sass需要相关的loader来处理，这里使用less 因此引入的为less-loader

2. css需要对兼容性问题进行处理，使用`psctcss`，`postcss-loader`,`postcss-preset-env`(css预制环境)。

> 这里默认打包会由js生产内联样式

3. 然后引入css样式处理 `css-loader`

4. 最后对样式进行处理的`style-loader`

   ```js
   {
   	test: /\.less$/,
       use: [
          "style-loader",
          "css-loader",
   		// 引入postcss
           // 类似于babel，把css语法转换兼容旧版浏览器的语法
           {
              loader: "postcss-loader",
              options:{
                   postcssOptions: {
                       plugins: [
                           // 浏览器兼容插件
                       	"postcss-preset-env",
                       ]
                  }
              }
            },
            "less-loader"
         ],
        exclude:/node_modules/
   }
   ```

5. css压缩使用插件 `css-nimizer-webpack`



### 4.处理静态资源：

处理图片

```js
{
    test:/\.jpe?g|png|gif|webp|svg/,
    type:"asset",
    parser:{
    	dataUrlCondition:{
            maxsize: 10*1024
        }        
	},
    generator:{
    //[hash:10]哈希值取前十位
    filename:"路径/img/[hash:10][ext][query]"
	}
}
```

其他资源：

```js
{
    test: /|.(woff2?|ttf)/,
    type:"asset:resource"，
    generator:{
    //[hash:10]哈希值取前十位
    filename:"路径/other/[hash:10][ext][query]"
}
}
```

> 区别：asset可以转变为base64 ，asset:resource则是故原封不动

### 5.js打代码处理

1.eslint

简介：用来代码规范

使用：

各种配置看文档吧，太长了。

2.babel

**简介**：用来处理es6语法兼容问题

配置文件类型：`babel.config.(js|json)`,`.babelrc.(js|json)`,或者在package中配置

**具体配置：**

```js
module.exprot = {
    //预设，就是来拓展Babel功能的插件
    presets:[]
}
```

![1663601955514](C:\Users\Linkys\AppData\Roaming\Typora\typora-user-images\1663601955514.png)



使用：

1. 下载

2. 在rules中添加规则：

   ```js
   {
       test:/\.js$/,
       loader:"babel-loader",
       options:{
           //可以写在这里预设，也可以写在Babel的配置文件里面
           presets:[]
       }
   }
   ```

   

### 生产模式的配置

区分一下不同环境的配置文件名：

`webpack.dev.js`  `webpack.prod.js`

mode属性要改一下

调试命令：

`"dev":webpack server --config ./config/webpack.dev.js`

`"build":webpack --config ./config/webpack.prod.js`

>  --config 参数后接配置文件使用那个配置文件

css文件的处理

1. 打包处理：提取css文件到单独文件，使用minicssextractplugin插件将css的rule中所有 style-loader 替换成minicssextractplugin.loader在插件的数组中 要创建实例

2. 兼容性处理：postcss-preset-env
3. 压缩插件 cssminimizerwebpackplugin

### 补充：

#### 1.）封装:

重复的配置可以封装成一个函数：

```js
getloader(){
	return [{
        内容
    }]
}

rule:{
    ...
    use: getloader()
}
```

#### 2.）`@`符号在webpack中的配置

```js
//与module等平级

resolve:{
    alias:{
        '@':path.join(__dirname,'./src/')
    }
}
```

#### 3.）修改输出文件目录

output中路径是所有的文件打包的位置

修改图片的输出路径位置:例子参考第4小节

```js
//在rule中，test同级中添加
generator:{
    //[hash:10]哈希值取前十位
    filename:"路径/img/[hash:10][ext][query]"
}
```



## 优化部分

### 1.SourceMap（线上代码排错）

**是什么**：

用来生成映射源代码和构建代码的方案

**怎么用：**

生产模式下，缺点打包慢

devtool:"source-map"

开发模式，打包快，值包含行映射

devtool:"cheap-module-source-map"

### 2.提高打包速度

#### 2.1热模块HMR

用来**提升打包速度**

在开发环境就可以了

```js
devserver:{

	hot:true;//开启HMR，默认开启

}
```

参考官网（vue,react..）提供的打包loader工具



#### 2.2oneOf 

提升打包速度

每个文件只能被一个loader命中

#### 2.3include/exclude

排除，或者只检查部分文件，处理文件更少，速度更快

#### 2.4cache

简介：对eslint,babel处理结果缓存。让第二次打包速度更快

使用：在处理js的rule中

```js
{
    test:/\.js$/,
        ...
    options:{
        cacheDirectory:true, //开启Babel缓存
        cacheCompression:false //关闭缓存文件压缩
    }
}
```

在插件eslintplugin中开启缓存:

cache:true,

cachelocation:'path'

#### 2.5多线程打包

happypack

### 3.减少代码体积优化

#### 3.1tree shaking

了解一下，默认开启

#### 3.2@babel/plugin-transform-runtime

#### 3.3图片压缩

imagemin-gifsicle /-jpegtran /-

分为无损压缩和有损压缩，直接百度把

（需要翻墙，网不好）

### 4.优化运行

#### 4.1code slipt（优化运行）

##### 1.)多入口文件情况：

```js
entry：{
    //多个入口文件
	app:'./app.js',
	main:'./main.js'
}

output:{
    path: path.reslove(__dirname,"dist")
	filename: "[name].js" //这样写不冲突
}

plugin:[
    new htmlwebpackplugin({
        template: ...
    })
]
```

> 每个入口文件就是一个chunk,打包完的就是bound

1.提取公共模块

我们可以将重复得模块抽取出来打包，比如a,b同时引用了c。在打包的时候如果不分割就会出现a,b的都有c得代码。如果开启了就会将公共其抽取成单独文件

```js
optimization:{
    //代码分割配置，详细查阅文档
    sliptChunks:{
        chunk:"all"//开启所以模块进行分割，并启用默认值
        ...
    },
    cacheGroups:{
 		...
        default:{
            minsize: 最小体积
            minChunks: 引用次数
        }        
    }
}
```

2.按需加载（动态加载）

```js
/*
*例如
*/
getelementbyid('btn').onclick = ()=>{
    //import 动态导入： 会将动态导入得文件分割（拆成单独模块），在需要的时候自动加载
    import('./count').then(res =>{  
    	//succful
    }).catch( err =>{
        //失败
    })
}
```

##### 2.)单页面：

1.开启代码分割

2.使用import动态加载

3.给动态导入的文件取名

```js
// 1. /* webpackChunkName: "math" */webpack魔法命名
import(/* webpackChunkName: "math" */ "./count")

// 2. 在output中
chunkFilename: 'static/js/[name].chunk.js'
```

#### 4.2preload/prefetch

![1663347416032](C:\Users\Linkys\AppData\Roaming\Typora\typora-user-images\1663347416032.png)

preload: 让浏览器立即加载

prefetch: 空闲的时候加载

> 兼容性差，can i use 查询兼容性

使用：

下载npm包`npm i preload-webpack-plugin -D`

```js
//在插件里注册
new preloadwebpackplugin({
	rel: preload //prefetch 没有as
	as: 'script'
})

<>
```

#### 4.3corejs

专门处理代码中es6+语法，promise，async,await 等低版本浏览器不支持的语法进行处理。让不兼容的浏览器也能使用该特性

怎么使用：

1. 全部引用

   在main.js引入，`import 'core.js'`

2. 按需加载

   在noed_moudle中找core中提供的包，例如`import 'core-js/es/promise'`

3. 最优方案

   用Babel自动配置好core.js

   ```js
   presets:[
       [
           "@babel/preset-env",
           {
               useBuiltIns:"usage",//按需加载自动引入
               corejs:3
           }
       ]
   ]
   //可以写在单独的webpack的配置文件的rule中，例
   use:[
       {
          loader: "babel-loader",
          // 设置babel
          options:{ presets:[] }
       }
   ]
   ```

   

### loader

#### loader概念：

1. 分类
   1. pre:前置
   2. normal：普通
   3. inline： 内联loader
   4. post: 后置
2. 执行顺序：依次1234 ，同级的从右到左，从下到上。



#### 开发loader

loader就是一个函数，当我们需要调用它的时候就会运行。

loader接受到文件内容作为参数，返回内容出去。