import redis
#创建连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
#pylist:['pythonweb','socket','pybase','pylist']
r.lpush('pylist','pybase','socket','pythonweb')
#pylist:['spider','pythonweb','socket','pybase','pylist']
r.linsert('pylist','before','pythonweb','spider')
#4
print(r.llen('pylist'))

print(r.lrange('pylist',0,-1))
#b'pybase'
print(r.lpop('pylist'))
#[b'spider',b'pythonweb']
print(r.ltrim('pylist',0,1))



while True:
    #如果列表为空时，返回None
    result=r.brpop('pylist',1)
    if result:
        print(result)
    else:
        break
r.delete('pylist')




















