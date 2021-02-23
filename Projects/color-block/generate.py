import random

ROWS = 50
CONTRAST = 0

start_html = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

    <title>Random Color</title>
  </head>
  <body>
  <div class="container-fluid">
'''
def rand_color(bias=0):
    ret = ""
    for i in range(6):
        dig = random.randint(0+bias, 15-bias)
        if dig == 10:
            dig = 'A'
        elif dig == 11:
            dig = 'B'
        elif dig == 12:
            dig = 'C'
        elif dig == 13:
            dig = 'D'
        elif dig == 14:
            dig = 'E'
        elif dig == 15:
            dig = 'F'
        dig = str(dig)
        ret += dig
    return ret
        
    

html = ''

fi = open('color.html', 'w')

for row in range(ROWS):
    html += '<div class="row">'
    for col in range(12):
        hcolor = rand_color(CONTRAST)
        html += '<div class = "col-md-1" style="background-color: #' + hcolor + '"> &nbsp&nbsp&nbsp </div>'
    html += '</div>'

start_html += html
start_html += '</div></body></html>'

fi.write(start_html)
    
