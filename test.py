import numpy as np

s = np.array([[1,1,-1,-1,1], [-1,1,-1,-1,1], [1,-1,-1,-1,1], [1,1,1,-1,1], [1,1,-1,1,1]])
# s[0] = [1,1,-1,-1,1]
# s[1] = [-1,1,-1,-1,1]
# s[2] = [1,-1,-1,-1,1]
# s[3] = [1,1,1,-1,1]
# s[4] = [1,1,-1,1,1]

label = np.array([1, -1, -1, -1, -1])

w = [1,1,1,1,1]
count = 0
n = -1
rate = np.float64(0.5)
for i in range(100):
    if i%5 == 0:
        n += 1
        print(n)
    s_used = s[i-5*n]
    label_used = label[i-5*n]
    print(s_used)
    print(label_used)
    w = w + rate * (label_used - np.sign(np.dot(s_used, w)) ) * s_used
    print(w)
    print('\n')

# result = np.array([-1,-1,1,1,-1]) + np.float64(0.5) * np.sign(np.dot([1,1,-1,-1,1],[-1,-1,1,1,-1])) * np.array([1,1,-1,-1,1])
# print(result)

