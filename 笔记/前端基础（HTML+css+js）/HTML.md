# HTML

## 简介

本文包括了基础html内容，以及HTML5新特性。由于HTML5以及被广泛应用到开发中，主流的浏览器以及被支持。因此有必要去学习一下

## HTM5新特性

- 新元素
- 新属性
- 完全支持 CSS3
- Video 和 Audio
- 2D/3D 制图
- 本地存储
- 本地 SQL 数据
- Web 应用

## 基本标签

1. h5音频标签：`<audio>`

   - src: 音频路径 {src:''}
   - controls： 显示播放的控件
   - autoplay: 自动播放
   - loop: 循环播放

2. h5视频标签：`<video>`
    >同上

3. 列表

    |标签名|说明|
    |--|--|
    |ul|无序列表|
    |ol|有序列表|

    > ol标签只能包含li标签

    |标签名|说明|
    |--|--|
    |dl|表示这个自定义列表，用来包裹dt/dd|
    |dt|表示自定义列表的主题|
    |dd|表示每个主题的内容|

4. 表格标签
   1. 基本使用

        |标签名|说明|
        |--|--|
        |table|表格整体，可以包裹多个tr|
        |tr|表格每行，有多个td|
        |td|每个单元格|

        ```html
        <!-- 例子 -->
        <table>
            <tr>
                <td>第一列</td>
                <td>第二列</td>
            </tr>
            <tr>
                <td>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>3</td>
                <td>4</td>
            </tr>
        </table>
        <!-- 实际中使用css修改样式，这里不展开 -->
        ```

   2. 合并单元格
        |属性名|说明|
        |--|--|
        |rowspan|跨行合并，讲多行的单元格**垂直**合并|
        |colspan|跨列合并，讲多列的单元格**水平**合并|

        > 直接在单元格加属性名，值为要合并多少个单元格例如`<td rowspan="2">`

5. 表单标签
    1. `input`
        通过`type属性`展示不同的效果，常用的属性如下：
        - `text` 文本输入框
        - `password` 密码框
        - `radio` 单选框，多选一
            >可以设置相同的`name`属性来分为一组，`checked`为默认选中
        - `checkbox` 多选框
        - `file` 上传文件
            >如果需要上传多个文件需要添加`multiple`属性
        - `submit` 提交按钮
        - `rest` 重置按钮
        >提示属性`placeholder`

    2. `button`

    3. `select`
        标签组成：
        - select： 下拉菜单的整体
        - option： 每个选项

        ```html
        <select>
            <option>选项1</option>
            <option>选项2</option>
            <option selected>选项3</option>
        </select>
        <!-- seleced 默认选中 -->
        ```

    4. `textarea`

    5. `label`
        用法如下所示

        ```html
        <!-- 第一种用法 -->
        <label for="id1">
            <span>男</span>
        </label>
        <input type='radio' id="id1" name="sex">

        <!-- 第二种 直接包裹 去掉for属性-->
        <label>
            <span>女</span>
            <input type='radio' name="sex">
        </label>
        ```

6. 语义化标签
   1. `div` 块标签 独占一行
   2. `span` 一行显示多个的标签
