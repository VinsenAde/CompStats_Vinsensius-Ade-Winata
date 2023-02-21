from scipy import stats
import statistic as s

nilai = [70, 80, 70, 70, 90, 100]

value_mode = stats.mode(nilai)
modus = s.mode(nilai)
print(modus)
print(value_mode)
print(value_mode.mode)