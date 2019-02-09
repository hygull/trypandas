import pandas as pd 

data = pd.read_csv('hw.csv')
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', 2000)

print(data)
#           SCHOOL Class         CODER              Activity
# 0  Boston School    XI          WY G  Learning Programming
# 1      CG School   XII    Malinikesh          Enjoying PHP
# 2   Model School     X     Rishikesh       Enjoying Python
# 3  Boston School     X     Tiny Ojha         Learning Java
# 4      CG School   XII  Pinky Markus          Enjoying PHP
# 5  Boston School   XII          WY G       Learning Python
# 6   Model School    XI     Rishikesh            Enjoying C
# 7  Boston School   XII          WY G         Learning Java
# 8   Model School     X     Raghvndra            Enjoying C

print(pd.get_dummies(data, columns=['SCHOOL']))
#   Class         CODER              Activity  SCHOOL_Boston School  SCHOOL_CG School  SCHOOL_Model School
# 0    XI          WY G  Learning Programming                     1                 0                    0
# 1   XII    Malinikesh          Enjoying PHP                     0                 1                    0
# 2     X     Rishikesh       Enjoying Python                     0                 0                    1
# 3     X     Tiny Ojha         Learning Java                     1                 0                    0
# 4   XII  Pinky Markus          Enjoying PHP                     0                 1                    0
# 5   XII          WY G       Learning Python                     1                 0                    0
# 6    XI     Rishikesh            Enjoying C                     0                 0                    1
# 7   XII          WY G         Learning Java                     1                 0                    0
# 8     X     Raghvndra            Enjoying C                     0                 0                    1

data1 = pd.get_dummies (data, columns=['SCHOOL','Class','CODER','Activity'])
print(data1)
#    SCHOOL_Boston School  SCHOOL_CG School  SCHOOL_Model School  Class_X  Class_XI  Class_XII  CODER_Malinikesh  CODER_Pinky Markus  CODER_Raghvndra  CODER_Rishikesh  CODER_Tiny Ojha  CODER_WY G  Activity_Enjoying C  Activity_Enjoying PHP  Activity_Enjoying Python  Activity_Learning Java  Activity_Learning Programming  Activity_Learning Python
# 0                     1                 0                    0        0         1          0                 0                   0                0                0                0           1                    0                      0                         0                       0                              1                         0
# 1                     0                 1                    0        0         0          1                 1                   0                0                0                0           0                    0                      1                         0                       0                              0                         0
# 2                     0                 0                    1        1         0          0                 0                   0                0                1                0           0                    0                      0                         1                       0                              0                         0
# 3                     1                 0                    0        1         0          0                 0                   0                0                0                1           0                    0                      0                         0                       1                              0                         0
# 4                     0                 1                    0        0         0          1                 0                   1                0                0                0           0                    0                      1                         0                       0                              0                         0
# 5                     1                 0                    0        0         0          1                 0                   0                0                0                0           1                    0                      0                         0                       0                              0                         1
# 6                     0                 0                    1        0         1          0                 0                   0                0                1                0           0                    1                      0                         0                       0                              0                         0
# 7                     1                 0                    0        0         0          1                 0                   0                0                0                0           1                    0                      0                         0                       1                              0                         0
# 8                     0                 0                    1        1         0          0                 0                   0                1                0                0           0                    1                      0                         0                       0                              0                         0
