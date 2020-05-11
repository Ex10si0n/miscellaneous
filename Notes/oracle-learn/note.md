# Oracle 数据库学习笔记
启动
```bash
$ sqlplus <usrname>/<passwd>
```

## 表空间及数据文件
### 默认表空间
#### DBA_TABLESPACES
```sql
SQL> SELECT TABLESPACE_NAME FROM DBA_TABLESPACES;

TABLESPACE_NAME
------------------------------
SYSTEM --管理任何其他表空间。它包含数据字典，有关数据库管理信息的表和视图，编译的存储对象（如触发器，过程等）。
SYSAUX --辅助表空间。
UNDOTBS1 --撤销表空间。存储的是撤销信息，可以用于恢复操作。
TEMP --临时表空间。可用于排序操作等。
USERS --存储用户的表和索引数据。
```

#### DBA_USERS
一个用户只能分配一个表空间，一个表空间可以被多个用户使用。
```sql
SQL> SELECT DEFAULT_TABLESPACE, USERNAME FROM DBA_USERS;
SQL> SELECT DEFAULT_TABLESPACE, USERNAME FROM DBA_USERS WHERE USERNAME='SYSTEM';
SQL> SELECT * FROM USER_TABLES; --查询一个用户全部数据表
```

### 表空间的管理
#### 创建
```sql
SQL> CREATE TABLESPACE TP1; --表空间名
     DATAFILE 'tp1.dbf' --数据文件名
     SIZE 1M; --表空间大小

SQL> CREATE SMALLFILE TABLESPACE TP2
     DATAFILE 'tp2.dbf'
     SIZE 10M AUTOEXTEND ON NEXT 1M MAXSIZE 20M --创建的数据文件的大小是 10M，当数据文件充满时，会自动扩大 1M，最大为 20M。
     EXTENT MANAGEMENT LOCAL AUTOALLOCATE --默认
     SEGMENT SPACE MANAGEMENT AUTO; --默认
```

#### 更改 
##### 重命名
```sql
SQL> ALTER TABLESPACE TP2 RENAME TO NEW_TP;
```

##### 设置读写状态
```sql
SQL> ALTER TABLESPACE TP1 READ ONLY;
SQL> ALTER TABLESPACE TP1 READ WRITE;
```

##### 设置可用状态
```sql
SQL> ALTER TABLESPACE TP1 OFFLINE NORMAL;
SQL> ALTER TABLESPACE TP1 ONLINE;
```

##### 调整表空间大小 
```sql
SQL> ALTER DATABASE DATAFILE 'tp1.dbf' RESIZE 2M;
SQL> ALTER TABLESPACE TP1 ADD DATAFILE 'tp1_02,dbf' SIZE 1M;
SQL> SELECT T.NAME TNAME, D.NAME DNAME, D.BYTES FROM V$TABLESPACE T JOIN V$DATAFILE D USING(TS#) WHERE T.NAME LIKE 'TP1'; --查看表空间的数据文件和大小
```

#### 删除
```sql
SQL> DROP TABLESPACE TP1 INCLUDING CONTENTS AND DATAFILES;
SQL> DROP TABLESPACE TP1 INCLUDING CONTENTS CASCADE CONSTRAINTS; --存在外键关系，删除表空间完整性
```

### 临时表空间
#### 创建
```sql
SQL> CREATE TEMPORARY TABLESPACE TMP_SP1 TEMPFILE 'tmp_sp1.dbf' SIZE 10M;
SQL> SELECT TABLESPACE_NAME FROM DBA_TEMP_FILES; --查看临时表空间
```

#### 设置为默认
```sql
SQL> ALTER DATABASE DEFAULT TEMPORARY TABLESPACE TMP_SP1;
```

#### 临时表空间组
```sql
SQL> ALTER TABLESPACE TMP_SP1 TABLESPACE GROUP TMPGROUPS;
SQL> SELECT * FROM DBA_TABLESPACE_GROUPS;
```

### 数据文件
#### 重命名&移动
```sql
SQL> CREATE TABLESPACE MVDATA DATAFILE 'mvdata.dbf' SIZE 5M;
SQL> ALTER TABLESPACE MVDATA ADD DATAFILE 'mvdata2.dbf' SIZE 5M;
SQL> ALTER DATABASE MOVE DATAFILE 'mvdata.dbf' to 'new_mvdata.dbf';
```
#### 查看
```sql
SQL> SELECT NAME FROM V$DATAFILE;
```
#### 删除
```sql
ALTER TABLESPACE MVDATA DROP DATAFILE 'mvdata2.dbf';
```

## 表
### 数据类型
字符串: `VARCHAR2(20)`
数字: `NUMBER, NUMBER(4, 2), INT, FLOAT`
日期: `DATE()`
大文本数据: `GLOB`
[More](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/Data-Types.html#GUID-A3C0D836-BADB-44E5-A5D4-265BA5968483)

### 创建表
#### 普通创建
```sql
SQL> CREATE TABLE STU(
     ID NUMBER,
     NAME VARCHAR2(20),
     AGE NUMBER(3),
     BIRTHDAY DATE DEFAULT SYSDATE,
     NOTE GLOB
);
SQL> DESC STU; --显示表结构
SQL> INSERT INTO STU(ID, NAME, AGE, BIRTHDAY, NOTE) VALUES(1, 'Steve', 19, TO_DATE('2001-01-12', 'yyyy-mm-dd'), 'Hello world'); --插入数据
SQL> SELECT * FROM STU; --查看
```

#### 通过查询结果创建
```sql
SQL> CREATE TABLE DUP_STU AS SELECT * FROM STU WHERE NAME='Steve';
```

### 重命名表
```sql
SQL> RENAME STU TO STUDENTS;
SQL> SELECT * FROM USER_TABLES; --查询全部数据表
```

### 修改表结构
```sql
SQL> DESC STU; --查看表结构
```
#### 增加列
```sql
SQL> ALTER TABLE STU ADD(ADDRESS VARCHAR2(50) DEFALUT 'none');
SQL> ALTER TABLE STU ADD(EMAIL VARCHAR2(50));
```

#### 修改表中数据列
```sql
SQL> ALTER TABLE STU MODIFY(NAME VARCHAR2(30));
SQL> ALTER TABLE STU MODIFY(EMAIL DEFAULT 'No Email');
--只有新增数据才能应用更改的内容
```

#### 重命名列
```sql
SQL> ALTER TABLE STU RENAME COLUMN ADDRESS TO ADDRESS_CHANGE;
```

#### 删除列
```sql
SQL> ALTER TABLE STU DROP(ADDRESS_CHANGE);
SQL> ALTER TABLE STU DROP COLUMN ADDRESS_CHANGE;
--删除索引
SQL> ALTER TABLE STU SET UNSED(EMAIL):
SQL> ALTER TABLE STU DROP UNUSED COLUMNS;
```
#### 复制表结构
```sql
SQL> CREATE TABLE STU_DUP AS SELECT * FROM STU WHERE 1==2;
```

### 约束
#### 类型
##### NOT NULL
```sql
SQL> CREATE TABLE STU(ID NUMBER, NAME VARCHAR2(20) NOT NULL);
SQL> INSERT INTO STU(ID) VALUES(2);
ORA-01400: 无法将 NULL 插入 ("SYSTEM"."TECH"."NAME")
```

##### UNIQUE
```sql
SQL> ALTER TABLE STU ADD(EMAIL VARCHAR2(30) UNIQUE);
```
##### PRIMARY
```sql
SQL> ALTER TABLE STU ADD CONSTRAINTS PK_ID PRIMARY KEY(ID);
```

##### CHECK
```sql
SQL> ALTER TABLE STU ADD(SEX VARCHAR2(10), CONSTRAINTS CHK_SEX CHECK(SEX='male' OR SEX='female'));
SQL> ALTER TABLE STU ADD(AGE NUMBER(3), CONSTRAINTS CHK_AGE CHECK(AGE BETWEEN 5 AND 200));
```

##### FOREIGN

```sql
SQL> CREATE TABLE CLASS_CATE(
     CID NUMBER(5) PRIMARY KEY;
     NAME VARCHAR2(30)
);
SQL> CREATE TABLE CLASSES(
     ID NUMBER(10) PRIMARY KEY,
     NAME VARCHAR2(30),
     CID NUMBER(5),
     CONSTRAINTS FK_CATE FOREIGN KEY(CID) REFERENCES CLASS_CATE(CID) ON DELETE CASCADE
);
SQL> INSERT INTO CLASS_CATE(CID, NAME) VALUES(1, 'cate1');
SQL> INSERT INTO CLASSES(ID, NAME, CID) VALUES(1, 'course1', 1);
SQL> INSERT INTO CLASSES(ID, NAME, CID) VALUES(2, 'course2', 2); --报错: CID在CLASS_CATE中没有CID=2的数据

```
#### 删除约束
```sql
SQL> ALTER TABLE STU DROP CONSTRAINT CHK_SEX;
```

### 删除
#### 删除表内容
```sql
SQL> COMMIT; --设置还原点
SQL> DELETE FROM STU;
```
-> STU表内容清空
```sql
SQL> ROLLBACK; --恢复为还原点
```
-> STU表内容恢复
```sql
SQL> TRUNCATE TABLE STU; --无法恢复
```
#### 删除表
```sql
SQL> DROP TABLE STU;
SQL> DROP TABLE CLASS_CATE CASCADE CONSTRAINTS; --删除带有约束的父表
```

## SQL
### 查询
| 操作符               | 释义                       |
| -------------------- | -------------------------- |
| `=`                  | 等于                       |
| `<>`                 | 不等于                     |
| `!=`                 | 不等于                     |
| `>`                  | 大于                       |
| `>=`                 | 大于等于                   |
| `<`                  | 小于                       |
| `<=`                 | 小于等于                   |
| `BETWEEN ... AND...` | 检查值的范围               |
| `IN`                 | 检查是否在一组值中         |
| `NOT IN`             | 检查一个值是否不在一组值中 |
| `IS NULL`            | `NULL` 值测试              |
| `IS NOT NULL`        | `NOT NULL` 值测试          |
| `LIKE`               | 模式匹配                   |
| `NOT LIKE`           | 否定匹配                   |

```sql
SQL> col s_name for a20 --设置显示s_name的宽度
SQL> SELECT * FROM STUDENT WHERE S_AGE BETWEEN 20 AND 50;

  S_ID S_NAME               S_SEX  S_AGE
------ -------------------- ------ ------
  1002 shiyanlou1002        female 20
  1004 shiyanlou1004        female 40
```
**通配符**
用于`LIKE`有`%`和`_`两个
```sql
SQL> SELECT * FROM STUDENT WHERE S_NAME LIKE '%2';
```
**函数**
```sql
MAX(), MIN(), SUM(), AVG()
CONCAT(char1, char2)
```
```sql
SQL> SELECT CONCAT(CONCAT(s_name,'''s sex is '),s_sex) "sex" FROM student WHERE s_id=1001;

sex
-------------------------------------------------------------------
shiyanlou1001's sex is man
```
**分组排序**
```sql
GROUP BY
HAVING
ORDER BY
```
```sql
--排序
SQL> SELECT s_id, COUNT(*) FROM sc GROUP BY s_id;

      S_ID   COUNT(*)
---------- ----------
      1001          3
      1002          3
      1003          1

--多列排序
SQL> SELECT s_id,grade, SUM(grade) FROM sc GROUP BY s_id,grade;

      S_ID      GRADE SUM(GRADE)
---------- ---------- ----------
      1002        100        100
      1003         75         75
      1001         70         70
      1001         96         96
      1002         80        160
      1001         20         20

6 rows selected.

--数据过滤
SQL> SELECT s_id, sum(grade) FROM sc GROUP BY s_id HAVING SUM(grade)>100;

      S_ID SUM(GRADE)
---------- ----------
      1001        186
      1002        260

--筛选出总成绩>100的分组，根据总成绩降序排列
SQL> SELECT s_id,sum(grade) AS sum_grade FROM sc GROUP BY s_id HAVING sum(grade)>100 ORDER BY sum(grade) DESC;

      S_ID  SUM_GRADE
---------- ----------
      1002        260
      1001        186
```
**嵌套查询**
```sql
SQL> SELECT s_id, s_age FROM student WHERE s_id IN(SELECT s_id FROM ssc WHERE c_id=1);
```
**表的连接**
```sql
SQL> SELECT sc.s_id, sc.c_id, s_name, c_name, grade FROM student, course, sc WHERE student.s_id=sc.s_id AND course.c_id=sc.c_id;

      S_ID       C_ID S_NAME          C_NAME          GRADE
---------- ---------- --------------- ---------- ----------
      1001          3 shiyanlou1001   c                  70
      1001          1 shiyanlou1001   java               20
      1001          4 shiyanlou1001   spark              96
      1002          1 shiyanlou1002   java              100
      1002          2 shiyanlou1002   python             80
      1002          4 shiyanlou1002   spark              80
      1003          3 shiyanlou1003   c                  75

7 rows selected.
```
**视图**
创建一个可以快速调用的SELECT条件
```sql
SQL> CREATE VIEW all_info AS SELECT sc.s_id,sc.c_id,s_name,c_name,grade,s_age,s_sex,c_time FROM student,course,sc WHERE student.s_id=sc.s_id AND course.c_id=sc.c_id;
SQL> desc all_info;
SQL> select * from all_info;
```
在数据字典`user_views`看到它
```sql
SQL> select view_name from user_views where view_name='ALL_INFO';

VIEW_NAME
----------------------
ALL_INFO

--调用视图
SQL> select * from all_info where grade>80;

--删除视图
SQL> DROP VIEW all_info;
```

