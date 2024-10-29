class arithmetic_op:
    def sum(self):
        x=56
        y=78
        return x+y
    def mul(self):
        a=20
        b=5
        return a*b
    def sub(self):
        p=156
        q=49
        return p-q
    def div(self):
        e=58
        d=26
        return e/d
    def mod(self):
        g=96
        n=456
        return g//n
    def even_odd(self):
        g=5
        if g%2==0:
         return "even"
        else:
            return "odd"
    def pos_negative(self):
        g=46
        if g<0:
          return "negativenumber"
        else:
            return "postivenumber"
    def fact(self):
        n=10
        fact=1
        for i in range(1,n+1):
            fact=fact*i
            return f"factorial of {n}is:{fact}"
    def prime_no(self):
        n=5
        prime= False
        if n==0 or n==1:
            return f"give number{n}prime number is {prime}"
        elif n>1:
            for i in range(2,n):
                if n% i ==0:
                    prime=True
                    if prime:
                        return f"give number {n} prime number is {prime}"
                    else:
                        return f"give number {n} prime number is {prime}"
    def mobile_no_validation(self):
        ph=8179277278
        if len(ph)==10:
            return "Give phone number is valid"
        elif len(ph)<5:
            return "Given phone number is not valid because the given length of number is less than 5"
        else:
            return "Given phone number is not valid"




