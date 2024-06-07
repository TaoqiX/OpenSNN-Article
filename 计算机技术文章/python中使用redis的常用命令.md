
# python中使用redis的常用命令

> 在Python中使用Redis，可以通过`redis-py`库来执行各种Redis命令。以下是一些常用的Redis命令及其在`redis-py`中的实现示例：
> 安装：`pip install redis`或者`conda install redis-py`, 安装完成后，就可以使用`import redis`来导入库了。

### 1. 连接到Redis服务器

```python
import redis

# 创建一个Redis连接
r = redis.Redis(host='localhost', port=6379, password='123456', db=0)
```

### 2. 键值操作

#### 设置键值

```python
r.set('key', 'value')
```

#### 获取键值

```python
value = r.get('key')
print(value)  # 输出: b'value'
```

#### 删除键

```python
r.delete('key')
```

#### 检查键是否存在

```python
exists = r.exists('key')
print(exists)  # 输出: 0 或 1
```

### 3. 字符串操作

#### 增加数值键

```python
r.incr('counter')
```

#### 减少数值键

```python
r.decr('counter')
```

### 4. 列表操作

#### 左推入

```python
r.lpush('mylist', 'value1')
```

#### 右推入

```python
r.rpush('mylist', 'value2')
```

#### 获取列表元素

```python
values = r.lrange('mylist', 0, -1)
print(values)  # 输出: [b'value1', b'value2']
```

#### 弹出左侧元素

```python
value = r.lpop('mylist')
print(value)  # 输出: b'value1'
```

#### 弹出右侧元素

```python
value = r.rpop('mylist')
print(value)  # 输出: b'value2'
```

### 5. 哈希操作

#### 设置哈希字段

```python
r.hset('myhash', 'field1', 'value1')
```

#### 获取哈希字段

```python
value = r.hget('myhash', 'field1')
print(value)  # 输出: b'value1'
```

#### 获取所有哈希字段和值

```python
fields = r.hgetall('myhash')
print(fields)  # 输出: {b'field1': b'value1'}
```

#### 删除哈希字段

```python
r.hdel('myhash', 'field1')
```

### 6. 集合操作

#### 添加成员

```python
r.sadd('myset', 'member1')
```

#### 获取所有成员

```python
members = r.smembers('myset')
print(members)  # 输出: {b'member1'}
```

#### 删除成员

```python
r.srem('myset', 'member1')
```

### 7. 有序集合操作

#### 添加成员和分数

```python
r.zadd('myzset', {'member1': 1.0})
```

#### 获取成员的分数

```python
score = r.zscore('myzset', 'member1')
print(score)  # 输出: 1.0
```

#### 获取成员的范围

```python
members = r.zrange('myzset', 0, -1)
print(members)  # 输出: [b'member1']
```

### 8. 事务操作

#### 使用事务

```python
with r.pipeline() as pipe:
    pipe.set('key1', 'value1')
    pipe.set('key2', 'value2')
    pipe.execute()
```

### 9. 发布/订阅

#### 订阅频道

```python
def message_handler(message):
    print(f"Received message: {message['data']}")

pubsub = r.pubsub()
pubsub.subscribe(**{'mychannel': message_handler})
pubsub.run_in_thread(sleep_time=0.001)
```

#### 发布消息

```python
r.publish('mychannel', 'Hello, World!')
```

### 10. 键过期

#### 设置键过期时间

```python
r.setex('key', 60, 'value')  # 60秒后过期
```

#### 获取剩余过期时间

```python
ttl = r.ttl('key')
print(ttl)  # 输出: 剩余时间（秒）
```

### 总结

这些是一些在Python中使用Redis的常用命令。`redis-py`库提供了一个简单而强大的接口来执行Redis的各种操作。你可以根据需要选择合适的命令来操作Redis数据结构。



######

-----

【转载自:】**开思通智网** ---- “一起来o站，玩转AGI！”  
【官网:】[https://www.opensnn.com/](https://www.opensnn.com/)  
【原文链接:】[https://www.opensnn.com/os/article/10000794](https://www.opensnn.com/os/article/10000794)

##### 结束
