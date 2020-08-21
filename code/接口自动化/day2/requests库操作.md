#### requests库易错点回顾
1. requests.post方法：data和json参数的区别
- params参数，如果传入的是字典，自动编码为表单。--一般get请求需要。
- data参数，如果传入的是字典，自动编码为表单。
- data参数，如果传入的是字符串，按原格式发布出去。
- json参数，如果传入的是字典，自动编码为json字符串。
- json参数，如果传入的是字符串，按原格式基础上添加双引号发布出去。
- headers参数，传递的是字典格式。
- data=json.dumps(dictPayload) 等同于 json=dictpayload

2. requests库响应消息体四种格式 
 
|返回格式|说明|用处|    
|----|----|----|  
|r.text:文本响应内容| 返回字符串类型 | 获取网页Html时用|   
|r.content:字节响应内|返回字节类型|下载图片或文件时使用|  
|r.json():Json解码响应内容|返回字典格式|**明确服务器返回json数据才能用**|  
|r.raw:原始响应内容|返回原始格式||  

3.接口关键性名词透析  

3.1. Cookie
    - cookie是分站点的，站点和站点之间的Cookie是相互独立的
    - 浏览器的Cookies是保存在浏览器的某个位置的  
    - 服务器可以通过：响应头中的set-Cookie参数，对客户端的Cookie进行管理
    - 浏览器的每次请求，都会把该站点的Cookie发送给服务器
    - 实现登录:Cookie + Session 配合使用
    
3.2. Cookie & sessionId合作
    - 快速理解：用户登录成功服务器创建session，返回给客户端，客户端浏览器把session保存在它的cookie中。
    - 过程描述：
        - 登录成功服务器立马创建session，并通过【响应头】中的set-Cookie属性把session返回给客户端。
        - 浏览器把响应头中的set-cookie内容存起来，存在浏览器自己的cookie中。
        - 以后浏览器每次发送请求时，都会把该站点的全部cookie通过请求头传递给服务器。
        
3.3. token-令牌
    - token也是由服务器产生的，存在服务器的内存或硬盘中
    - 有一套产生规则，会涉及到加密算法
    - **用token实现登录**
        - 开发提供一个获取token接口，根据用户名+密码，获取一个token值返回一个token(字符串)
        - token值服务器通过什么给客户端呢？
        1. 通过响应头给客户端的。---次要
        2. 通过响应消息体传给客户端。---主要
        3. 通过Cookie传递给客户端。---很少
   

