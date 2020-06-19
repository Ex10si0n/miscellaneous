# note

## 数据库操作

### 链接数据库

```bash
mysql -uroot
mysql -uroot -p
```

### 退出数据库

```text
exit/quit/<C+d>
```

### 显示所有数据库

```text
SHOW DATABASES;
```

### 显示时间

```text
SELECT NOW();
```

### 创建数据库

```text
CREATE DATABASE <dbname>;
CREATE DATABASE <dbname> charset=utf8;
```

### 显示创建数据库的信息

```text
SHOW CREATE DATABASE <dbname>;
```

### 删除数据库

```text
DROP DATABASE <dbname>;
DROP DATABASE `<dbname>`;
```

### 查看当前数据库

```text
SELECT DATABASE();
```

### 使用数据库

```text
USE <dbname>;
```

## 数据表操作

### 查看当前数据库中所有的表

```text
SHOW TABLES;
```

### 创建数据表

```text
CREATE TABLE <tbname>(id int, name varchar(30));

CREATE TABLE <tbname>(
    id int primary key not null auto_increment,
    name varchar(30)
);

CREATE TABLE students(
    id int unsigned not null auto_increment primary key,
    name varchar(30),
    age tinyint unsigned,
    height decimal(5,2),
    gender enum("Male", "Female", "Ungiven") default "Ungiven",
    classs_id int unsigned
);
```

### 显示数据表信息

```text
DESC <tbname>;
```

### 插入数据

```text
INSERT INTO students VALUES(0, 'Steve', 18, 188.12, "Male", 0);
```

