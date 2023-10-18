def Fib(N):
  if(N%1==0 and N>0):
    if(N==1):
      return 1
    if(N==2):
      return 2
    if(N==3):
      return 4
    else :
      Temp=Fib(N-1)+Fib(N-2)+Fib(N-3)
    return Temp
  else :
    print("!!! ENTER VALID NUMBER")
T=float((input()))
if(Fib(T)!=None):
  print(Fib(T))
