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
   添加mode ,entry ,output 

6. 在package.json添加
   `srcpit:{ dev : "webpack"}`

7. 处理样式的loader
   `npm install css-loader@5.2.6 style-loader@3.0.0 -D`
   在家匹配规则

   ```josn
    module: {
        rules:[
            //定义不同模块的对应的loader
            { test:/\.css$/,use: ['style-loader','css-loader']}
        ]
    }
   ```

8. babel
   `npm install -D babel-loader @babel/core @babel/preset-env webpack`
   添加Babel的配置文件babel.config.js