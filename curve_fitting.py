import numpy as np
import math

def sumx_or_y(l):
    return round(sum(l),4)


def sumxy(l,m):
    xy = 0
    i = 0
    while i < len(l):
        xy += l[i]*m[i]
        i += 1
    return round(xy, 4)
    
def sumx2y(l,m):
    x2y = 0
    i = 0
    while i < len(l):
        x2y += pow(l[i], 2)*m[i]
        i += 1
    return round(x2y,4)
    
def sumx2(l):
    x2 = 0
    i = 0
    while i < len(l):
        x2 += pow(l[i], 2)
        i += 1
    return round(x2,4)
    
def sumx3(l):
    x3 = 0
    i = 0
    while i < len(l):
        x3 += pow(l[i], 3)
        i += 1
    return round(x3,4)
    
def sumx4(l):
    x4 = 0
    i = 0
    while i < len(l):
        x4 += pow(l[i], 4)
        i += 1
    return round(x4, 4)

# To fit a parabola of form y = a + bx + cx^2
def abxcx2():
   print("The normal equations are:")
   print('(',len(x_values),')a + (',table_values['x'],')b + (',table_values['x^2'],')c = ',table_values['y'])
   print('(',table_values['x'],')a + (',table_values['x^2'],')b + (',table_values['x^3'],')c = ',table_values['xy'])
   print('(',table_values['x^2'],')a + (',table_values['x^3'],')b + (',table_values['x^4'],')c = ',table_values['x^2.y'])
   coeff_list = [len(x_values),table_values['x'],table_values['x^2'],table_values['x'],table_values['x^2'],table_values['x^3'],table_values['x^2'],table_values['x^3'],table_values['x^4']]
   val_list = [table_values['y'],table_values['xy'],table_values['x^2.y']]
   coeff_list = np.array(coeff_list).reshape((3,3))
   val_list= np.array(val_list)
   sol = np.linalg.inv(coeff_list).dot(val_list)
   print('a = ',round(sol[0], 4))
   print('b = ',round(sol[1], 4))
   print('c = ',round(sol[2], 4))
   print('Equation -> y = (',round(sol[0], 4),') + (',round(sol[1], 4),')x + (',round(sol[2], 4),')x^2')

# To fit a parabola of form y = ax^2+bx+c
def ax2bxc():
   print("The normal equations are:")
   print('(',table_values['x^2'],')a + (',table_values['x'],')b + (',len(x_values),')c = ',table_values['y'])
   print('(',table_values['x^3'],')a + (',table_values['x^2'],')b + (',table_values['x'],')c = ',table_values['xy'])
   print('(',table_values['x^4'],')a + (',table_values['x^3'],')b + (',table_values['x^2'],')c = ',table_values['x^2.y'])
   coeff_list = [table_values['x^2'],table_values['x'],len(x_values),table_values['x^3'],table_values['x^2'],table_values['x'],table_values['x^4'],table_values['x^3'],table_values['x^2']]
   val_list = [table_values['y'],table_values['xy'],table_values['x^2.y']]
   coeff_list = np.array(coeff_list).reshape((3,3))
   val_list= np.array(val_list)
   sol = np.linalg.inv(coeff_list).dot(val_list)
   print('a = ',round(sol[0], 4))
   print('b = ',round(sol[1], 4))
   print('c = ',round(sol[2], 4))
   print('Equation -> y = (',round(sol[0], 4),')x^2 + (',round(sol[1], 4),')x + (',round(sol[2], 4),')')

# To fit a straight line of form y = ax + b
def st_line():
    print('The normal equations are :')
    print('(',table_values['x^2'],')a + (',table_values['x'],')b = ',table_values['xy'])
    print('(',table_values['x'],')a + (',len(x_values),')b  = ',table_values['y'])
    coeff_list = [table_values['x^2'],table_values['x'],table_values['x'],len(x_values)]
    val_list = [table_values['xy'],table_values['y']]
    coeff_list = np.array(coeff_list).reshape((2,2))
    val_list= np.array(val_list)
    sol = np.linalg.solve(coeff_list, val_list)
    print('a = ',round(sol[0],4))
    print('b = ',round(sol[1],4))
    print('Equation -> y = (',round(sol[0,4]),')x + (',round(sol[1],4),')')

# To fit a curve of form y = ax^b
def axb():
    x, y, xy, x2 = 0, 0, 0, 0
    k = 0
    for i in x_values:
        x += math.log(i)
    for i in y_values:
        y += math.log(i)
    while k < len(x_values):
        xy += math.log(x_values[k])*math.log(y_values[k])
        x2 += pow(math.log(x_values[k]), 2)
        k += 1
    print('x : ',x)
    print('y :',y)
    print('xy :',xy)
    print('x^2 :',x2)
    print('The normal equations are :')
    print('(',len(x_values),')A + (',x,')b  = ',y)
    print('(',x,')A + (',x2,')b = ',xy)
    coeff_list = [len(x_values),x,x,x2]
    val_list = [y,xy]
    coeff_list = np.array(coeff_list).reshape((2,2))
    val_list= np.array(val_list)
    sol = np.linalg.solve(coeff_list, val_list)
    print('A = ',round(sol[0],4))
    print('As we know log a = A. Therefore, a = e^A')
    print('a = ',math.exp(round(sol[0],4)))
    print('b = ',round(sol[1],4))
    print('Equation -> y = (',round(math.exp(round(sol[0],4)),4),')x ^ (',round(sol[1],4),')')


def display_all():
    [print(key,':',value) for key, value in table_values.items()]

def display():
    print('x : ',table_values['x'])
    print('y :',table_values['y'])
    print('xy :',table_values['xy'])
    print('x^2 :',table_values['x^2'])


# Driver Code
if __name__ == "__main__":
print('Choose the equation to fit: 1. a + b.x + c.x^2   2. a.x^2 + b.x + c  3. y = ax + b  4. y = a.x^b')
ch = int(input('Enter the type of eqn (1/2/3/4) :'))
x_values = [float(x) for x in input("Enter the values of x: ").split()]
y_values = [float(x) for x in input("Enter the values of y: ").split()]
table_values = {   'x': sumx_or_y(x_values),
                    'y': sumx_or_y(y_values), 
                    'xy': sumxy(x_values, y_values), 
                    'x^2.y': sumx2y(x_values, y_values),
                    'x^2' : sumx2(x_values),
                    'x^3' : sumx3(x_values),
                    'x^4' : sumx4(x_values)
}
if ch == 1:
    display_all()
    abxcx2()
elif ch == 2:
    display_all()
    ax2bxc()
elif ch == 3:
    display()
    st_line()
elif ch == 4:
    axb()
else:
    print('Invalid Choice')