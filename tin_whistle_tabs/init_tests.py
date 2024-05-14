import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

# y is pushed up one to not clip first circle
plt.scatter ([1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], marker ='o', s=1000, facecolors='none', edgecolors='k')
plt.ylim(0, 7)

print('end')