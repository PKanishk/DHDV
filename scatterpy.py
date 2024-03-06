import matplotlib.pyplot as plt
hours_studied = [3, 5, 7, 2, 8, 6, 4, 9]
exam_scores = [65, 80, 85, 60, 90, 75, 70, 95]
plt.scatter(hours_studied, exam_scores, color='blue')
plt.title('Relationship between Hours Studied and Exam Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.show()
