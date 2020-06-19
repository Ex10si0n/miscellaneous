# Oracle 数据库学习笔记

启动

```bash
$ sqlplus <usrname>/<passwd>
```

## 表空间及数据文件

### 默认表空间

#### DBA\_TABLESPACES

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

#### DBA\_USERS

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

**重命名**

```sql
SQL> ALTER TABLESPACE TP2 RENAME TO NEW_TP;
```

**设置读写状态**

```sql
SQL> ALTER TABLESPACE TP1 READ ONLY;
SQL> ALTER TABLESPACE TP1 READ WRITE;
```

**设置可用状态**

```sql
SQL> ALTER TABLESPACE TP1 OFFLINE NORMAL;
SQL> ALTER TABLESPACE TP1 ONLINE;
```

**调整表空间大小**

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

字符串: `VARCHAR2(20)` 数字: `NUMBER, NUMBER(4, 2), INT, FLOAT` 日期: `DATE()` 大文本数据: `GLOB` [More](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/Data-Types.html#GUID-A3C0D836-BADB-44E5-A5D4-265BA5968483)

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

**NOT NULL**

```sql
SQL> CREATE TABLE STU(ID NUMBER, NAME VARCHAR2(20) NOT NULL);
SQL> INSERT INTO STU(ID) VALUES(2);
ORA-01400: 无法将 NULL 插入 ("SYSTEM"."TECH"."NAME")
```

**UNIQUE**

```sql
SQL> ALTER TABLE STU ADD(EMAIL VARCHAR2(30) UNIQUE);
```

**PRIMARY**

```sql
SQL> ALTER TABLE STU ADD CONSTRAINTS PK_ID PRIMARY KEY(ID);
```

**CHECK**

```sql
SQL> ALTER TABLE STU ADD(SEX VARCHAR2(10), CONSTRAINTS CHK_SEX CHECK(SEX='male' OR SEX='female'));
SQL> ALTER TABLE STU ADD(AGE NUMBER(3), CONSTRAINTS CHK_AGE CHECK(AGE BETWEEN 5 AND 200));
```

**FOREIGN**

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

-&gt; STU表内容清空

```sql
SQL> ROLLBACK; --恢复为还原点
```

-&gt; STU表内容恢复

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

| 操作符 | 释义 |
| :--- | :--- |
| `=` | 等于 |
| `<>` | 不等于 |
| `!=` | 不等于 |
| `>` | 大于 |
| `>=` | 大于等于 |
| `<` | 小于 |
| `<=` | 小于等于 |
| `BETWEEN ... AND...` | 检查值的范围 |
| `IN` | 检查是否在一组值中 |
| `NOT IN` | 检查一个值是否不在一组值中 |
| `IS NULL` | `NULL` 值测试 |
| `IS NOT NULL` | `NOT NULL` 值测试 |
| `LIKE` | 模式匹配 |
| `NOT LIKE` | 否定匹配 |

```sql
SQL> col s_name for a20 --设置显示s_name的宽度
SQL> SELECT * FROM STUDENT WHERE S_AGE BETWEEN 20 AND 50;

  S_ID S_NAME               S_SEX  S_AGE
------ -------------------- ------ ------
  1002 shiyanlou1002        female 20
  1004 shiyanlou1004        female 40
```

**通配符** 用于`LIKE`有`%`和`_`两个

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

SQL> SELECT id, name, people_num
     FROM employee, department
     WHERE employee.in_dpt = department.dpt_name
     ORDER BY id;
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

**视图** 创建一个可以快速调用的SELECT条件

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

## PL/SQL

### PL/SQL结构

```text
DECLARE      --声明部分。例如定义常量，变量，引用的函数或过程等。
BEGIN        --执行部分。包含变量赋值，过程控制等。
EXCEPTION    --处理异常。包含错误处理语句。
END;         --结束部分。
/            /*添加这个斜杠来执行 PL/SQL 语句块。*/
```

### Hello World

```text
SET SERVEROUTPUT ON;
BEGIN
    DBMS_OUTPUT.put_line('Hello World');
END;
/
```

### 变量声明

全局变量可以在内部语句块中访问，内部变量在语句块外面访问不到.

```text
DECLARE
    v_tell varchar2(20);
BEGIN
    v_name := 'Hello World';
    DBMS_OUTPUT.put_line('System Output: ' || v_tell);
END;
/
```

### 常量声明

```text
DECLARE
    v_num CONSTANT NUMBER := 1;
    v_bool CONSTANT BOOLEAN := FALSE;
BEGIN
    NULL;
END;
/
```

### 键盘输入

```text
DECLARE
    v_sid student.s_id%TYPE;
    v_sname student.s_name%TYPE;
BEGIN
    v_sid := &studentid;
    SELECT s_name INTO v_name FROM student WHERE s_id = v_sid;
    DBMS_OUTPUT.put_line('Student''s name is : ' || v_sname);
END;
/
```

### 运算符

赋值运算符 := 连接运算符 \|\|

| 分类 | 运算符 | 说明 |
| :--- | :--- | :--- |
| 简单关系运算符 | &gt;， &lt;， &gt;= ，&lt;=， =， !=， &lt;&gt; | 大于，小于，大于等于，小于等于，等于。`!=` 和 `<>` 都表示不等于。 |
| 判断空值 | `IS NULL` ，`IS NOT NULL` | 判断某列内容是否是 NULL |
| 范围查询 | `BETWEEN` 最小值 `AND` 最大值 | 在指定的最小值和最大值的范围内查找 |
| 范围查询 | `IN` | 指定查询的范围 |
| 模糊查询 | `LIKE` | 模糊查询 |

```text
DECLARE
  v_a NUMBER :=1;
  v_b NUMBER :=2;
  v_c NUMBER;
  v_d VARCHAR2(20);
BEGIN
  IF v_a<v_b THEN     --判断 v_a 是否小于 v_b
    DBMS_OUTPUT.put_line(v_a || ' < ' || v_b);
  END IF;
  IF v_c IS NULL THEN   --判断 v_c 是否为空
    DBMS_OUTPUT.put_line('v_c is null');
  END IF;
  IF v_b BETWEEN 1 AND 3 THEN    --判断 v_b 是否在 1 到 3 之间
    DBMS_OUTPUT.put_line('v_b is between 1 and 3');
  END IF;
  IF v_b IN(1,2,3) THEN      --判断 v_b 是否在 （1，2，3）里
    DBMS_OUTPUT.put_line('v_b is : ' || v_b);
  END IF;
  IF v_d LIKE 'shi%' THEN     --判断 v_d 是否是 shi 开头
    DBMS_OUTPUT.put_line(v_d);
  END IF;
END;
/
```

输出

```text
1 < 2
v_c is null
v_b is between 1 and 3
v_b is : 2
```

### 数据类型

标量类型（scala data type）：用来保存单个值。例如：数字，字符串，布尔值，日期等。

* NUMBER
* BINARY\_INTEGER, PLS\_INTEGERBINARY
* BINARY\_DOUBLE, BINARY\_FLOAT
* **CHAR, VARCHAR2**
  * CHAR 以定长方式保存字符串。若赋值长度不足其定义长度，会以空格补充。
  * VARCHAR2 变长字符串。若不足定义长度，不会补充内容。
* NCHAR, NVARCHAR2
* **LONG, LONG RAW**
  * LONG 保存变长字符串。
  * LONG RAW 保存变长二进制数据。
* ROWID, UROWID
* DATE
  * 获取系统时间 `sys_date DATE := SYSDATE/SYSTIMESTAMP;`

复合类型（coposite data type）：保存多种类型数值。例如：索引表，可变数组，嵌套表等。 引用类型（reference data type）：用来指向另一个不同的对象。 LOB 类型：大数据类型，主要用来处理二进制数据，最多可以存储 4G 的信息。

```text
DECLARE
    p1 PLS_INTEGER := 2147483647;
    p2 PLS_INTEGER := 1;
    n NUMBER;
BEGIN
    n:= p1 + p2;
END;
/

--ERROR: 数字溢出
```

```text
DECLARE
  v_timezone TIMESTAMP WITH TIME ZONE := SYSTIMESTAMP;
  v_localtime TIMESTAMP WITH LOCAL TIME ZONE := SYSTIMESTAMP;
BEGIN
  DBMS_OUTPUT.PUT_LINE(v_timezone);
  DBMS_OUTPUT.PUT_LINE(v_localtime);
END;
/
```

### 流程控制语句

IF ... THEN ... ELSIF ... ELSE ...

```text
DECLARE
  v_name student.s_name%TYPE;
  v_sex student.s_sex%TYPE;
BEGIN
  SELECT s_name,s_sex INTO v_name,v_sex FROM student WHERE s_id=1003;
  CASE v_sex
    WHEN 'man' THEN
      DBMS_OUTPUT.put_line(v_name|| ' is man');
    WHEN 'woman' THEN
      DBMS_OUTPUT.put_line(v_name ||'is woman');
    ELSE
      DBMS_OUTPUT.put_line('dont know');
    END CASE;
END;
/
```

WHILE ... LOOP ...; END LOOP;

```text
DECLARE
    v_i NUMBER := 1;
BEGIN
    WHILE(v_i <= 5) LOOP
        DBMS_OUTPUT.put_line(v_i);
        v_i := v_i+1;
    END LOOP;
END;
/
```

FOR ... IN 1 .. N Loop ...; END LOOP;

```text
DECLARE
    v_i NUMBER := 1;
BEGIN
    FOR v_i IN 1 .. 5 LOOP
        DBMS_OUTPUT.put_line(v_i);
    END LOOP;
END;
/
```

`exit; # break`

`CONTINUE;`

`GOTO flag; <<falg>>`

异常

```text
EXCEPTION
EXCEPTION
  WHEN '异常类型' | '用户自定义异常' | '异常代码' | OTHERS THEN
    '异常处理语句';
```

捕获异常

```text
DECLARE
  v_a NUMBER := 1;
  v_b NUMBER := 0;
BEGIN
  v_a := v_a/v_b;
EXCEPTION
  WHEN ZERO_DIVIDE THEN   --捕获除数为 0 的异常
    DBMS_OUTPUT.put_line('zero divide');
    DBMS_OUTPUT.put_line(SQLCODE);  --输出异常编号
    DBMS_OUTPUT.put_line(SQLERRM);  --输出异常详情
END;
/
```

