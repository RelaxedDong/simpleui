# 安装

本项目是依赖django-simpleui，在simpleui基础之上，封装更多的方法、组件等， 以扩展出更多的能力。

安装：

```python
pip install simpleui-admin
```

# 扩展能力

- actions layer 增加点击后disabled属性，以利于耗时任务用户会多次点击的情况
- SIMPLEUI_CONFIG 配置项，支持自定义的菜单栏权限，自定义页面权限更灵活，例如：

```python
{
    'name': '我是自定义页面',
    'icon': 'fas fa-code',
    'url': 'https://xxxxxx',
    'newTab': False,
    # permission 是新增的字段，使用 django 默认的权限管理系统. 
    # 刷新页面会获取当前登录用户所有的权限，无权限则不展示改菜单
    'permission': 'auth.xxxxxx'
}
```
- 增加是否展示面包屑控制, settings.SIMPLEUI_NO_BREADCRUMBS