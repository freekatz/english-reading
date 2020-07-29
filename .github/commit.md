### 提交规范

>  注："(<>)" 中的内容都可省略，可使用 && 连接多类提交内容，如 cho && doc: …

1. ref(refactor)：重构代码文件和项目结构

   > ref(<重构内容的目录或代码位置或名称>): 重构的具体内容
   >
   > 如：
   >
   > ref(src/test/): 合并 test 目录中的 a.rs 和 b.rs

2. fix(fix)：修复 bug 或 error

   > fix(<修复的源文件名称或者功能的昵称>): 修复的具体内容、
   >
   > 如：
   >
   > fix(test.rs): 修复函数 a 的返回值错误

3. fea(feature)：新的特性或新的功能

   > fea(<新的功能或特性缩略>): 具体介绍
   >
   > 如：
   >
   > fea(GitHub 评论支持): 评论系统添加 GitHub 账号接入支持

4. wip(working in process)：新的进展

   > wip(<功能模块昵称/xx%>): 进展介绍
   >
   > 如：
   >
   > wip(时光轴功能/50%): 完成时光轴界面模板及后端数据库接口

5. doc(document)：文档更新

   > doc(<添加或修改的文档位置或名称>): 添加的文档内容概述
   >
   > 如：
   >
   > doc(doc/test/test.md): 完成项目测试流程的介绍文档

6. cho(chore)：杂项更新

   > cho(<杂项内容的位置或名称>): 更新的内容
   >
   > 如：
   >
   > cho(.gitingore): 排除临时文件夹
   
7. test(tests)：测试更新

   > cho(<修改的测试文件或者进行的测试内容>): 更新的内容
   >
   > 如：
   >
   > cho(test.rs): 测试文档更改监听功能