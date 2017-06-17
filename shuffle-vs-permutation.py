
# coding: utf-8

import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Length of array
n = 10 ** np.arange(1, 10)

shuffle_elapsed = []
permutation_elapsed = []
loop_start = time.time()
for i in n:
    print(i)
    start = time.time()
    a = np.arange(i)
    np.random.shuffle(a)
    end = time.time()
    
    shuffle_elapsed.append((i, end - start))
    
    start = time.time()
    b = np.random.permutation(i)
    end = time.time()
    
    permutation_elapsed.append((i, end - start))

loop_end = time.time()
print('循环完成，耗时 {} s'.format(loop_end - loop_start))
res = {'shuffle': shuffle_elapsed, 'permutation': permutation_elapsed}

# PLot
plt.plot([n for n, _ in shuffle_elapsed], [t for  _, t in shuffle_elapsed])
plt.plot([n for n, _ in permutation_elapsed], [t for  _, t in permutation_elapsed])
plt.legend(['shuffle', 'permutation'])
plt.title('shuffle VS permutation')
plt.savefig('result.jpg', dpi=300)
print('图片保存成功')

np.save('shuffle', shuffle_elapsed)
np.save('permutation', permutation_elapsed)
print('npy 保存成功')
with open('result.pkl', 'wb') as f:
    pickle.dump(res, f)
print('pickle 保存成功')

