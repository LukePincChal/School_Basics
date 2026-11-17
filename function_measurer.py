class function:
    def __init__(self, arr=None):
        if arr is not None:
            self.x = arr
        else: 
            x = int(input("Degree of the function(for example ax^3+bx^2+c will be degree 3): "))
            self.x = []
            for i in range (x+1):
                if i == (x):        value = float(input(f'Value of the constant: '))
                else:               value = float(input(f'Value of the {i+1}º coefficient: '))
                self.x.append(value)

    def plot(self, arr=None, value=0):

        term = 0
        if arr== None: x = self.x[::-1]
        else: x = arr[::-1]

        for power, item in enumerate(x):
            term+= item*value**power
        return term

    def derivative(self, arr=None, value=None):
        if arr ==None: x = self.x[::-1]
        else: x = arr[::-1]


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




    def roots(self, factor=0, precision=13):
        if len(self.x)==1:
            return f"The equation has NO roots"

        if len(self.x) == 2:
            return f"The equation's root is: {-self.x[1]/self.x[0]}" 

        if len(self.x) == 3:
            x_opt = -self.x[1]/(2*self.x[0])
            delta = (x_opt**2 - self.x[2]/self.x[0])**0.5
            return f"The equation's root(s) is(are): {set( [x_opt-delta, x_opt+delta] )}"  

        #Solving method

        def solve(function, roots):

            equation_roots = []
            total_answers = []

            #All possible root points
            for root in roots:
                total_answers.append(root+10**factor)
                total_answers.append(root-10**factor)

                total_answers.append( 1j*(root+10**factor) )
                total_answers.append( 1j*(root-10**factor) )


            for point in total_answers:
                x = point
                difference = [x, None, None]

                x = x - self.plot(function, x)/self.derivative(function, x); difference[1] = x
                x = x - self.plot(function, x)/self.derivative(function, x); difference[2] = x


                if not abs(difference[1]-difference[0]) >= abs(difference[2]-difference[1]):
                    continue

                for i in range(250):
                    x = x - self.plot(function, x)/self.derivative(function, x)

                equation_roots.append(x)

            for pos, root in enumerate(equation_roots):
                if isinstance(root, complex):

                    if round(root.imag, precision) == 0: rounded_root = round(root.real, precision)
                    else: rounded_root = round(root.real, precision) + 1j*round(root.imag, precision)
                        
                    equation_roots[pos] = rounded_root


                else: equation_roots[pos] = round(root, precision)
            


            return list(set(sorted(equation_roots, key=abs)))
        ###############

        if abs(factor) > 1: factor = 0

        necessary_functions = [self.x]
        actual_function = self.x

        for i in range(len(self.x)-3):

            actual_function = self.derivative(actual_function, value=None)
            necessary_functions.append(actual_function)

        necessary_functions = necessary_functions[::-1]

        for pos, function in enumerate(necessary_functions):
            if pos == 0:
                x_opt = -self.x[1]/(2*self.x[0])
                delta = (x_opt**2 - self.x[2]/self.x[0])**0.5
                roots = [x_opt-delta, x_opt+delta]

            else:
                roots = solve(function, roots)


        return f"The equation's root(s) is(are): {set(roots)}"


    def integral(self, up=None, down=0):
        
        if up == None: x = self.x; x.append("C");x = x[::-1]
        else: x = self.x[::-1] 

        if up == None:
            for power, item in enumerate(x):
                if not power == 0:
                    x[power] = item/power
            return x[::-1]
        else:
            for power, item in enumerate(x):
                x[power] = (item/(power+1))*up**(power+1) - (item/(power+1))*down**(power+1)
            return sum(x)
    

    def tangent(self, x0=0):
        fx = self.derivative()
        fa = []

        for i in fx:
            fa.append(-x0*i)

        fx.append(self.plot(x0))
        
        for pos, i in enumerate(fa):
            fx[pos+1] += i
        return fx
        

    def line(self, x0=0):
        line = []
        f = self.derivative(value=x0)
        line.append(f)
        line.append(-f*x0+self.plot(value=x0))
        return line


    def _polynomise(self, arr):
        pol_string = ""

        for i in range(len(arr)):

            if arr[i] == 0: continue
            elif i==0: pol_string += str(arr[i])
            else: pol_string = str(arr[i])+f"x^{i} + "+pol_string

        return pol_string



if __name__ == "__main__":
    whised_input = True
    polynomial = function()
    print(f"The function will be: {polynomial._polynomise(polynomial.x[::-1])}")

    while whised_input != 0:

        print("\n")
        whised_input = int(input("What would you like to do? \n\n1. - Plot the function's value \n2. - Get the function's derivative \n3. - Get function's area(Integral)\n4. - Get function's roots \n5. - Get a function's tangential line point \n0. - End program \n>>: "))
        print("\n")


        if whised_input==1:
          number = float(input("What is your selected value? >>:"))
          print(polynomial.plot(value=number))


        elif whised_input == 2:
            number = input("If you want to select a value, digit it, if not, press Enter >>:")

            try:
                number = float(number)
                print(polynomial.derivative(value=number))
            except:

                result = polynomial.derivative()[::-1]
                prepared_result = polynomial._polynomise(result)
                print(prepared_result)



        elif whised_input == 3:

          up = input("If you want to select the up part of the integral, digit, if no, Enter >>:")
          if up is None or up == "": 
            result = polynomial.integral()[::-1]
            print(polynomial._polynomise(result))

          else:
            down = input("Digit the down part of the integral:")
            up, down = float(up), float(down)
            print(polynomial.integral(down=down, up=up))


        elif whised_input == 4:
          factor = float(input("What is the wished factor? (It is a number between -1 and 1 that adjusts the algorithm to find the roots easier) >>:"))
          precision = int(input("What is the wished precision? (It determinates the decimal rounding; if too low, the roots might get inaccurate, if it is too high, the roots might be repeated) >>:"))
          print(polynomial.roots(factor=factor, precision=precision))


        elif whised_input == 5:
            number = int(input("What is the wished x-value to be tangent point between the line and the function?>>"))
            result = polynomial.line(number)
            print(polynomial._polynomise(result))
