#!C:\Users\arvafik\AppData\Local\Programs\Python\Python39
import cgi, cgitb 
form = cgi.FieldStorage()

decimal = form.getvalue('decimal')
valorBit = form.getvalue('valorBit')
posicion = form.getvalue('posicion')

binario = format(decimal, "b")
bit = (decimal>>valorBit) & 1
pos = binario[(-1*posicion)]

result = "El binario es = {} El valor del bit es =  {} La posicion es = {}".format(binario, bit, posicion)
print("Content-Type: text/html")
print()  
print("<TITLE>Conversion a binario</TITLE>")
print("<H1>Conversion</H1>")
print(result)