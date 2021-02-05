x = 89
def anil():
  x =20
  def pawan():
    global x
    x = 88
    pawan()
    print("after calling pawan()",x)

anil()
print(x)