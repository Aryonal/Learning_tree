# Learning Tree

> using MongoDB and WebSocket
>
> ```sh
> $ ./init_db.py
> $ ./start -h localhost -p 3000
> ```

[TOC]

## API

### 1. 获取大类

Client emit Event **"Classes"**, json =

```json
{
    "userId": "u123"
}
```

Server response Event **"rClasses"**, json =

```json
{
    "data": {
        "pages": 2,
        "classNames": ["Python基础", "Python进阶"]
    }
}
```

### 2. 获取大类中的节点 

Client emit Event **"Nodes"**, json =

```json
{
    "userId": "u123",
    "class": "Python入门"
}
```

Server response Event **"rNodes"**, json =

````json
{
    "data": {
        "nodes": 5,
        "nodeNames": ["if", "else", "elif", "比较运算符", "布尔运算"]
    }
}
````

### 3. 获取节点详细信息

Client emit Event **"NodeInf"**, json =

```json
{
    "userId": "u123",
    "node": "if",
    "class": "Python入门"
}
```
Server response Event **"rNodeInf"**, json =

```json
{
    "data": {
        "index": 1,
        "prior": [0],
        "name": "if",
        "title": "if 条件",
        "psg": "如果条件成立的话\n条件会有是否两种状态.."
    }
}
```

### 4. 错误信息

Server response Event **"*Error"**, 比如 **"rClassesError"**, json =

```json
{
    "msg": "return Class Names error"
}
```

### TODO

1. 根据 "userId" 字段定制用户学习树
4. 根据节点 "prior" 字段，定义树状学习路径

## DataBase

### 1. 大类

大类保存为MongoDB中的Collection, 大类中Doc依"index"升序排序。


### 2. 节点

节点保存为MongoDB中Collection下的Document

每个节点的结构为

```json
{
    "index": 1,
    "prior": [0],
    "name": "**",
    "title": "***",
    "psg": "********"
}
```

