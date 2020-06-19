# JSP-Learn

## `server: Apache Tomcat`

**Installation & StartUp:**

```bash
brew install tomcat
brew services start tomcat
```

**HTTP Webapps root Directory** `/usr/local/Cellar/tomcat/9.0.35/libexec/webapps/ROOT`

## Codes

```text
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="UTF-8" import="java.util.*"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>Hello World</title>
    </head>
    <body>
        <%
            List<String> words = new ArrayList<String>();
            words.add("today");
            words.add("is");
            words.add("a");
            words.add("great");
            words.add("day");
        %>
        <table width="200px" align="center" border="1" cellspacing="0">
            <%for (String word: words) { %>
            <tr>
                <td><%=word%></td>
            </tr>
        <%}%>
        </table>
    </body>
</html>
```

