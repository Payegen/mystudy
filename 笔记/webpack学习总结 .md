# **webpack基础配置**

首先安装在项目安装webpack

```bash
npm init -y  #初始化一个package.json
npm install webpack webpack-cli -D    #本地安装最新版`webpack`,`webpack-cli`
npm info webpack   #查看webpack历史版本信息（当要安装特定版本时）
```

webpack.config.js在这个文件里面去配置，这是webpack定义的一个默认的配置文件名，webpack运行时会检查是否有这个配置文件，有这个配置文件时，会使用其中的配置来覆盖默认配置。

## 1入口entry和输出output

```js
//webpack.config.js
const path = require('path'); //引入nodejs中path模块，帮助设置路径

module.exports = {
    //entry:"./src/index.js",   #入口文件路径配置 ，下面采用的是对象模式配置的
    
    entry:{   #入口文件配置可以使用字符串模式也可以使用对象模式
        main:'./src/index.js'
    },
    
    output:{     #输出文件路径配置
        filename:'bundle.js',   #输出文件名
        //output的path需要是绝对路径
        path:path.resolve(__dirname,'dist')  #输出文件路径，绝对路径，使用node.js的path模块来解析为绝对路径，这里设置为根目录下的dist目录
    },
}
```

## 2加载器loader

webpack默认只能识别JS模块，其他模块是不识别的。 而loader就是帮助webpack来识别并解析除了JS的其他模块的。针对各种各样的模块， webpack中不只有JS的模块时，需要配置对应的loader。比如："less-loader"，css-loader等

 loader是一个声明式函数。监测对应的模块格式，使用对应的loader处理。loader的配置主要在module.rules中进行，这是一个数组，里面是各种loader的规则。

安装命令：npm i file-loader -D

#### loader的主要工作机制：

1. 识别文件类型，确定具体处理该模块的loader（rule.test）

2. 使用对应的loader，对文件进行相关操作转换（rule.use）
    loader的在配置文件中的设置：

3. 

4. ```js
   //webpack.config.js
   const path = require('path');
   module.exports = {
       entry:{
           main:'./src/index.js'
       },
       output:{
           filename:'bundle.js',
           path:path.resolve(__dirname,'dist')
       },
       //不认识的模块（不是js)的配置
       module:{
           rules:[
               {
                   test:/\.xxx$/,    //表示匹配规则，是一个正则表达式
                   use:{     //表示针对匹配文件将使用处理的loader
                       loader:"xxx-loader",
                       options:{   //loader的可配置项，有时间需要，有时间不需要
                       }
                   }
               }
           ]
       },
   }
   ```



#### 常用的loader列举及资源模块分析：

##### 处理静态文件：

file-loader、url-loader、raw-loader

file-loader

```ruby
        rules:[
            {
                test:/\.(jpe?g|png|gif)$/,
                use:{
                    loader:"file-loader",
                    options:{
  //[]表示占位符（placeholder），name表示源文件的名字，ext是源文件的后缀，还可以连接hash：[name]-[hash].[ext]，很多loader都有一个叫做placeholder（占位符）的概念，可以有不同的占位符，比如名称、后缀、hash等。
                        name:"[name]-[hash].[ext]",
                        outputPath:"images/",    #配置输出位置，大部分需要输出位置的都会有这个配置
                    }
                }
          ]
```

url-loader

url-loader可以做file-loader可以做的所有事情，多出来的功能是：默认把静态资源转成base64格式并打包到bundle.js（最终的打包文件），可以使用limit选项来设置是否转译范围。大于limit范围的不转译，可以重新配置要打包图片的体积，一般是8kb。用url-loader可以减少请求数，但是图片大的时候，这样会增大打包文件的体积，所以需要有个度，可以使用options中的limit字段来设置文件是否转base64的限制，在限制范围内，就转译base64并打包到最终打包文件bundle.js，否则，就直接执行file-loader的功能，直接移动到输出目录。

##### 处理样式模块：

style-loader、css-loader、sass-loader、less-loader、postcss-loader

1. css-loader工作机制：处理css模块，识别合并css模块

2. style-loader工作机制：把合并的css模块放到html中头的style标签中。

3. #### 注意执行顺序，执行顺序：从下到上，从右到左

4. ```ruby
       module:{
           rules:[
               {
                   test:/\.css$/,
                   use: [   #执行顺序：从下到上，从右到左
                       'style-loader',   #把合并的css放到style标签
                       'css-loader',    #先识别css并合并为一个css
                     ],
               },
           ]
       },
   ```

postcss-loader

一般来说开发之中还会对样式模块的loader增加一个处理：自动给样式增加前缀（-webkit-,-o-等浏览器兼容前缀），这样就不用自己一个个的写了。 postcss-loader可以自定识别需要增加前缀的样式，自动给他们增加前缀代码。

##### 其他模块

处理数据文件：csv-loader、xml-loader

处理模块语言：html-loader、markdown-loader

处理测试模块：mocha-loader、eslint-loader

## 3Plugins

Plugins是开始打包时，在某个时刻，帮助我们处理一些什么事情的机制，它是事件驱动的，本身是一个类。
一种插件就是一种函数，通过传入不同的参数，可以实现不同的功能。

#### html-webpack-plugin

HtmlWebpackPlugin是在打包后的时刻，自动帮你生成一个引入了打包后的JS的html，并放到输出目录下的一个插件。

```tsx
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');//需要现在webpack中引入
const CleanWebpackPlugin = require('clean-webpack-plugin');
module.exports = {
    entry:"./src/index.js",
    output:{ },
    mode:"development",
    //不认识的模块（不是js)的配置
    module:{
        rules:[]   
    },
    //配置插件，是个数组，里面的项是插件的实例
    plugins:[
        //自动生成html，并移到输出目录
         new CleanWebpackPlugin(),//有些只需要引入，具体内部配置，看情况而定
        new HtmlWebpackPlugin({
            title:'html模板',  
            filename:'index.html',
            template:"./index.html"     #生成html的模板路径
        }),
        new hhhhhh() //有些只需要引入，具体内部配置，看情况而定
    ],

}
```

#### **clean-webpack-plugin** 

我们每次在打包时，文件都是已覆盖已有的，不删除多余的。所以dist目录如果不手动删除，就会有很多多余文件，因此我们可以使用一个插件帮助我们执行删除dist目录的操作，CleanWebpackPlugin插件是在打包之前，自动帮我们删除dist目录，以免污染打包环境。例子如上

#### 自动导出css，mini-css-extract-plugin

如果不想让css放在style标签中，我们可以使用插件来帮我们抽离css并打包输出到dist目录，MiniCssExtractPlugin可以帮我们代替style-loader，抽离css，并输出到dist目录



## 4本地服务器：devServer

#### webpack-dev-server

前端开发离不开这个利器：本地服务器，可以配置devServer并配合插件实现修改代码浏览器同步刷新，实时查看修改效果。

修改package.json

```bash
  "scripts": {
    "server": "webpack-dev-server",
  },
```

```tsx
const path = require('path');
module.exports = {
    entry:"./index.js",
    output:{},
    devServer:{
        contentBase:'./dist',    //服务器启动的目录
        open:true,   //自动打开浏览器
        proxy:{    //设置代理，可用于本地mock数据，本地自己启动另外一个服务
            "/api":{
                target:"http://localhost:9092"
            }
        },
        port:8080, //指定端口号
        hot:true,   //开启HMR(Hot Module Replacement)热模块替换,由于是webpack自带的，所以要引入webpack ，监控并更新js模块的工作vue等框架自己做了，否则需要自己手动监控 
        hotOnly:true
    },
    //不认识的模块（不是js)的配置
    module:{
        rules:[]
    },
    plugins:[],
    
    
    devtool:'inline-source-map',//打包后的文件映射
    mode:"development"//去掉警告，开发模式
}
```

```
typescript配置
`"clean-webpack-plugin": "^4.0.0",`

`"css-loader": "^6.7.1",`
`"html-webpack-plugin": "^5.5.0`

`"less": "^4.1.3",`
`"less-loader": "^11.0.0",`

`"postcss": "^8.4.16",`
`"postcss-loader": "^7.0.1",`
`"postcss-preset-env": "^7.8.2",`
`"style-loader": "^3.3.1",`

`"ts-loader": "^9.3.1",`
`"typescript": "^4.8.3",`

`"webpack": "^5.74.0",`
`"webpack-cli": "^4.10.0",`
`"webpack-dev-server": "^4.11.0"
```

`

