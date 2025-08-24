# Markdown使用文档
1. **Markdown的VScode插件**
   - Markdown Preview Enhanced
   - Markdown All in One
> 不推荐使用Markdown PDF

2. **Markdown的基本语法**
   - 采用`**xx**`包裹来加粗字体，效果是**这样**。
   - 采用`1. `来表示有序嵌套列表，效果是
        1. xx  
   - 采用`-`,`*`或者`+`表示无序列表，效果是
        - xx
   - todolist，可以实现复选框效果，采用`- [ ] xx`，效果是
        - [ ] xx
   -  表格,采用
        ```
         |a|b|c|
        |:-|:--:|--:|
        |a14|b27|c32|
        ```
        > 第二行表示左对齐、居中对齐、右对齐

        效果为
        |a|b|c|
        |:-|:--:|--:|
        |a14|b27|c32|
    - 字体
        采用`**xx**`表示加粗，效果为**这样**；
        采用`*xx*`表示斜体，效果为这样*这样*；
        采用`~~xx~~`表示删除线，效果是~~这样~~；
        采用`==xx==`显示高亮，效果是==这样==；
        采用`***xx***`表示斜粗体，效果是***这样***;
        采用HTML语法实现下划线`<u>下划线</u>`，效果是<u>这样</u>
        采用`脚注[^1]`表示脚注，效果是这样[^1]；
        > 注意，脚注必须在后面注明解释才能正常解析和渲染
        
        采用`[^1]: 这是解释`来解释脚注，效果在最后

    - 超链接
        网址可以直接被识别
        也可以：`[点击链接][bilibili链接]`，效果是这样
        [点击链接][bilibili链接]，在后面要加上这个超链接的定义，定义是这样`[bilibili链接]: https://www.bilibili.com/`；
        > 定义放在最后，角标解释之后，且至少空一行。
    - 图片
        可以用网址 imgse.com 上传图片生成图片代码。
        <a href="https://imgse.com/i/pVsI6rn"><img src="https://s21.ax1x.com/2025/08/24/pVsI6rn.png" alt="pVsI6rn.png" border="0" /></a>
        可以采用HTML代码，类似
        ```
        <a href="https://imgse.com/i/pVsI6rn"><img src="https://s21.ax1x.com/2025/08/24/pVsI6rn.png" alt="pVsI6rn.png" border="0" /></a>
        ```
    - 导出PDF
          右击 Open In Browser；

[^1]: 这是解释

[bilibili链接]: https://www.bilibili.com/
        
      
        

        