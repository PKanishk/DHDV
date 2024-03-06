import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Science', 'English', 'History']
corr_matrix = np.array([[1.0, 0.8, 0.6, 0.4],
                        [0.8, 1.0, 0.7, 0.5],
                        [0.6, 0.7, 1.0, 0.3],
                        [0.4, 0.5, 0.3, 1.0]])

sns.heatmap(corr_matrix, 
            xticklabels=subjects, yticklabels=subjects,  
            cmap='coolwarm', annot=True, fmt=".2f") 

plt.title('Correlation Matrix Heatmap')

plt.show()
