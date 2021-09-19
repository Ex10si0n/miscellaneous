# Redis Learning Notes

## Keywords

### SET
```redis
# Mappings & Lists
SET myKey myVal
MSET a 10 b 20 c 30
LPUSH myList A

# Hashes
HMSET user:1000 username antirez birthYear 1977 verfied 1

# Sets
SADD mySet 1 2 3

# Sorted Sets
ZADD hackers 1940 "Alan Kay"
ZADD hackers 1957 "Sophie Wilson"
ZADD hackers 1953 "Richard Stallman"
ZADD hackers 1949 "Anita Borg"
ZADD hackers 1965 "Yukihiro Matsumoto"
ZADD hackers 1914 "Hedy Lamarr"
ZADD hackers 1916 "Claude Shannon"
ZADD hackers 1969 "Linus Torvalds"
ZADD hackers 1912 "Alan Turing"
```

### INCR DECR
```redis
# Mappings & Lists
SET counter 100
INCR counter         # 101
INCRBY counter 30    # 131

# Hashes
HMSET user:1000 username antirez birthYear 1977 verfied 1
HINCRBY user:1000 birthYear 10
HGET user:1000 birthYear    # 1987
```

### GET
```redis
# Mappings & Lists
GET myKey
MGET a b c
LRANGE myList 0 -1

# Hashes
HGETALL user:1000
HMGET user:1000 username birthYear
HGET user:1000 username

# Sets
SMEMBERS mySet
SISMEMBER mySet 3    # 1 -> True
SISMEMBER mySet 30   # 0 -> False

# Sorted Sets
ZRANGE hackers 0 -1
ZREVRANGE hackers 0 -1
ZRANGE hackers 0 -1 WITHSCORES
```

### DEL
```redis
DEL myList
```

### EXISTS
```redis
SET myKey helloWorld
EXISTS myKey
DEL myKey
EXISTS myKey
# Notes: Case Sensitive

SET myKey x
TYPE myKey    # string
KEYS my*      # key LIKES finding
DEL myKey
KEYS my*
TYPE myKey    # none

RANDOMKEY
```

### MISC
```redis
RENAME myList newList
DBSIZE               # return size of the redis instance

# expire
SET key value
EXPIRE key 10
GET key              # run immediately -> value
GET key              # run 10s later   -> (nil)

SET key 100 EX 30    # expire in 30s
TTL key              # time to leave of key

FLUSHDB              # flush current database
FLUSHALL             # flush all databases
```

## Time Complexity

| Data Structures |      Add       |      Del      |      Test      |
|-----------------|----------------|---------------|----------------|
| Sets            | O(1)           | O(1)          | O(1)           |
| Sorted Sets     | O(log(N))      | O(log(N))     | O(log(N))      |
