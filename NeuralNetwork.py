from tabulate import tabulate
import math
numberOfVectors = int(input("Enter number for vector : "))
lengthList = []
d_output = []
obseravtionAllVector = int(input("Enter the observationNo, : "))
vectorsDic = {}
for i in range(numberOfVectors):
    vectorsDic['v'+str(i+1)] = [float(input('v'+str(i+1)+'x'+str(k+1)+': '))
                                for k in range(obseravtionAllVector)]
for i in range(numberOfVectors):
    d_output.append(float(input('Enter D_Erorr for v'+str(i+1)+" : ")))
wights = []

for i in range(obseravtionAllVector):
    wights.append(float(input('Enter wight-'+str(i+1)+" :")))
bais = float(input('Enter bias : '))
baisWight = float(input('Enter biasWight : '))
totalBias = bais*baisWight
u = float(input('Enter the miu : '))
print("""choose the activation function
[1] step function
[2] sign function
[3] sigmoid function
""")
whichMethod = int(input('Enter your choice : '))
neuronDic = {}
Erorr = {}
for vector, values in vectorsDic.items():
    sum = totalBias
    for i, k in zip(values, wights):
        sum += k*i

    neuronDic[vector] = sum

print("Table1: vectors and it's D_output")
print(tabulate((vectorsDic.items(), d_output),
               tablefmt='fancy_grid', floatfmt='.2f'))
print("Table2: weights respectively")
print(tabulate([wights], tablefmt='fancy_grid', floatfmt='.2f'))
print("Table3: Neuron Values")
print(tabulate(neuronDic.items(), tablefmt='fancy_grid', floatfmt='.4f'))


def step(x, t):
    if x >= t:
        return 1
    elif x < t:
        return 0


def sign(x):
    if x >= 0:
        return 1
    elif x < 0:
        return -1


def sigmoid(x):
    e = math.e
    return 1/(1+(e**-x))


if whichMethod == 1:
    for (vectroname, neuron), D_error in zip(neuronDic.items(), d_output):
        Erorr[vectroname] = D_error - step(neuron, 0)
    print("Table4: Error value (notice : repeat this algorithm after first change from 0)")
    print(tabulate(Erorr.items(), tablefmt='fancy_grid', floatfmt='.2f'))
elif whichMethod == 2:
    for (vectroname, neuron), D_error in zip(neuronDic.items(), d_output):
        Erorr[vectroname] = D_error - sign(neuron)
    print("Table4: Error value (notice : repeat this algorithm after first change from 0)")
    print(tabulate(Erorr.items(), tablefmt='fancy_grid', floatfmt='.2f'))
elif whichMethod == 3:
    for (vectroname, neuron), D_error in zip(neuronDic.items(), d_output):
        Erorr[vectroname] = D_error - sigmoid(neuron)
    print("Table4: Error value (notice : repeat this algorithm after first change from 0)")
    print(tabulate(Erorr.items(), tablefmt='fancy_grid', floatfmt='.2f'))


newW = {}
for name, erorrValue in Erorr.items():
    o = 0
    if erorrValue != 0:

        for weight, valuInObservation in zip(wights, vectorsDic[name]):
            o += 1
            newW[name+'W'+str(o)+'New'] = weight + \
                (u*erorrValue*valuInObservation)
        newW['baisNew'] = baisWight+(u*erorrValue*bais)
print("Table5 : New weigth (which will be used for the next iteration if exsit)")
print(tabulate(newW.items(), tablefmt='fancy_grid', floatfmt='.4f'))
