# Error Set

## 1

- 问题

    新建蓝图 email.py 文件， 报错

- 错误信息

    ```bash
    ImportError: cannot import name Blueprint
    ```

- 原因

    email.py 与 Python 自带的 email 模块命令冲突了，把 email.py 修改其他不冲突的文件名

## 2

- 问题

    路由地址为 `http://127.0.0.1/mail/`，请求方法为`POST`，请求返回`500`状态码

- 错误信息

    ```bash
    FormDataRoutingRedirect: A request was sent to this URL (http://127.0.0.1:8080/mail) but a redirect was issued automatically by the routing system to "http://127.0.0.1:8080/mail/".  The URL was defined with a trailing slash so Flask will automatically redirect to the URL with the trailing slash if it was accessed without one.  Make sure to directly send your POST-request to this URL since we can't make browsers or HTTP clients redirect with form data reliably or without user interaction.
    ```

- 原因

    访问的 URL 为 `http://127.0.0.1/mail`，没有对于的路由，路由重定向到 `http://127.0.0.1/mail/`，`POST` 请求不支持这种重定向，所以报异常 `FormDateRoutingRedirect`

- [参考](https://stackoverflow.com/questions/20293372/formdataroutingredirect-exception-from-a-url-without-trainling-slash)