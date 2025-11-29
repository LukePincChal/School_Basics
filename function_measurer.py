class function:
    def __init__(self, arr=None):
        if arr is not None:
            self.x = arr
        else: 
            x = int(input("Grade of the equation: "))
            self.x = []
            for i in range (x+1):
                if i == (x):        value = float(input(f'Value of the constant: '))
                else:               value = float(input(f'Value of the {i+1}º coefficient: '))
                self.x.append(value)

    def plot(self, value=0):
        term = 0
        x = self.x[::-1]
        for power, item in enumerate(x):
            term+= item*value**power
        return term

    def derivative(self, value=None):
        x = self.x[::-1]
        if value == None:
            for power, item in enumerate(x):
                x[power] = power*item
            x.pop(0)
            return x[::-1]
        else:
            for power, item in enumerate(x):
                if power > 0:
                    x[power] = power*item*value**(power-1)
            x.pop(0)
            return sum(x)


    def roots(self):
        roots = []
        for i in range(len(self.x)+1):

            n=0
            irreal = False
            if len(roots) >= len(self.x)-2:
                term = 1
                for i in roots:
                    term*=i
                valor = (((self.x[-1])**2)**0.5)/(term+0.001)
                if (i%2)!=0: valor*=-1
            else: valor = (-1)**i*i**(8/10)

            while round(self.plot(valor), 6)!=0:
                valor -= self.plot(valor)/self.derivative(valor)
                if n>1001:
                    irreal = True
                    break
                n+=1
            if irreal is True:
                for i in range(20):
                    valor -= self.plot(valor*1j)/self.derivative(valor)
            try:
                roots.append(round(valor, 5))
            except:
                roots.append(valor)
        return f"The root(s) is(are):{set(roots)}"
    
    def integral(self, up=None, down=0):
        x = self.x[::-1]
        if up == None:
            for power, item in enumerate(x):
                x[power] = item/power
            return x[::-1]
        else:
            for power, item in enumerate(x):
                x[power] = (item/(power+1))*up**(power+1) - (item/(power+1))*down**(power+1)
            return sum(x)
    
    def mean_value(self, x0=0, x1=1):
        return (self.derivative(x0)-self.derivative(x1))/(x0-x1)
tipo = int(input("What do you want to do? \n1. - Plot the function's value \n2. - Get the function's derivative \n3 - Get function's area(Integral)\n4. - Get function's roots\n>>: "))
if tipo==1:
  number = float(input("What is your selected value?"))
  print(function().plot(value=number))
elif tipo == 4:
  print(function().roots())
elif tipo == 2:
    number = input("If you want to select a value, digit it, if no, press Enter: ")
    try:
        number = float(number)
        print(function().derivative(value=number))
    except:   
        print(function().derivative())
else:
  up = input("If you want to select the up part of the integral, digit, if no, Enter:")
  if up is None: print(function().integral())
  else:
    down = input("Digit the down part of the integral:")
    up, down = float(up), float(down)
    print(function().integral(down=down, up=up))
