import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# print(sns.get_dataset_names())

# car_crashes 데이터 가져오기 (데이터프레임 형태)
car_crashes = sns.load_dataset('car_crashes')
print(car_crashes)

"""
total : 전체 사고 건수
speeding : 과속 비율
alchohol : 음주 비율
not_distracted : 이전에 사고가 없었던 운전자 비율
no_previous : 자동차 보험료
ins_losses : 운전자 1인당 충돌사고로 보험사가 입은 손해
abbrev : 미국 주 약자
"""

plt.figure(figsize=(15, 10))

sns.barplot(data=car_crashes, x='abbrev', y='total')
plt.show()