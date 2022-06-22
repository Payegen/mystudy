# 初始化项目

1. 创建一个默认项目
   `npm init --yes`

2. 安装vue
   `npm install -S vue`

3. 安装webpack
   `npm install -D webpack webpack-cli webpack-dev-server`
   `npm install html-webpack-plugin@5.3.2 -D`

   > `-D`将webpack放在dev环境下

4. 添加src目录，创建一个vue入口
    app.vue
    index.js

5. 添加webpack配置文件
   添加mode ,entry ,output...

6. 在package.json添加
   `srcpit:{ dev : "webpack"}`

## 样式处理

1. 使用预处理less或者sass需要相关的loader来处理，这里使用less 因此引入的为less-loader

2. css需要对兼容性问题进行处理，使用`psctcss`，`postcss-loader`,`postcss-preset-env`(css预制环境)。
    > 这里默认打包会由js生产内联样式

3. 然后引入css样式处理 `css-loader`

4. 最后对样式进行处理的`style-loader`

## ts文件处理

这里介绍一个`core.js`解决一个兼容性问题 ，可以让老版本浏览器使用js新特性。提供它运行环境
先引入 `ts-loader` 解释ts 编译成js文件
然后使用Babel将新版本js打包成旧版本，此时Babel要进行单独配置所以使用对象心事配置，解决兼容问题

```js
 // 配置babel
                    {
                        // 指定加载器
                        loader: "babel-loader",
                        // 设置babel
                        options: {
                            // 设置预定义的环境
                            presets: [
                                [
                                    // 指定环境的插件
                                    "@babel/preset-env",
                                    // 配置信息
                                    {
                                        // 要兼容的目标浏览器
                                        targets: {
                                            "chrome": "58",
                                            "ie": "11"
                                        },
                                        // 指定corejs的版本
                                        "corejs": "3",
                                        // 使用corejs的方式 "usage" 表示按需加载
                                        "useBuiltIns": "usage"
                                    }
                                ]
                            ]
                        }
                    }
```
