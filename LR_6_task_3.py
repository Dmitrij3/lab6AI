from collections import Counter
import pandas as pd

data = [
    {"День": "D1", "Прогноз": "Сонячно", "Вологість": "Висока", "Вітер": "Слабкий", "Гра": "Ні"},
    {"День": "D2", "Прогноз": "Сонячно", "Вологість": "Висока", "Вітер": "Сильний", "Гра": "Ні"},
    {"День": "D3", "Прогноз": "Хмарно", "Вологість": "Висока", "Вітер": "Слабкий", "Гра": "Так"},
    {"День": "D4", "Прогноз": "Дощ", "Вологість": "Висока", "Вітер": "Слабкий", "Гра": "Так"},
    {"День": "D5", "Прогноз": "Дощ", "Вологість": "Нормально", "Вітер": "Слабкий", "Гра": "Так"},
    {"День": "D6", "Прогноз": "Дощ", "Вологість": "Нормально", "Вітер": "Сильний", "Гра": "Ні"},
    {"День": "D7", "Прогноз": "Хмарно", "Вологість": "Нормально", "Вітер": "Сильний", "Гра": "Так"},
    {"День": "D8", "Прогноз": "Сонячно", "Вологість": "Висока", "Вітер": "Слабкий", "Гра": "Ні"},
    {"День": "D9", "Прогноз": "Сонячно", "Вологість": "Нормально", "Вітер": "Слабкий", "Гра": "Так"},
    {"День": "D10", "Прогноз": "Дощ", "Вологість": "Нормально", "Вітер": "Слабкий", "Гра": "Так"},
    {"День": "D11", "Прогноз": "Сонячно", "Вологість": "Нормально", "Вітер": "Сильний", "Гра": "Так"},
    {"День": "D12", "Прогноз": "Хмарно", "Вологість": "Висока", "Вітер": "Сильний", "Гра": "Так"},
    {"День": "D13", "Прогноз": "Хмарно", "Вологість": "Нормально", "Вітер": "Слабкий", "Гра": "Так"},
    {"День": "D14", "Прогноз": "Дощ", "Вологість": "Висока", "Вітер": "Сильний", "Гра": "Ні"},
]

print(pd.DataFrame(data))

play_yes_count = sum(1 for row in data if row["Гра"] == "Так")
play_count = len(data)
play_yes_prob = play_yes_count / play_count
print("\n\nЙмовірність того, що гра відбувається: {0}/{1} = {2}".format(play_yes_count, play_count, round(play_yes_prob, 3)))

overcast_yes_count = sum(1 for row in data if row["Гра"] == "Так" and row["Прогноз"] == "Хмарно")
overcast_yes_prob = overcast_yes_count / play_yes_count
print("Ймовірність хмарності під час гри: {0}/{1} = {2}".format(overcast_yes_count, play_yes_count, round(overcast_yes_prob, 3)))

humidity_high_yes_count = sum(1 for row in data if row["Гра"] == "Так" and row["Вологість"] == "Висока")
humidity_high_yes_prob = humidity_high_yes_count / play_yes_count
print("Ймовірність високої вологості під час гри: {0}/{1} = {2}".format(humidity_high_yes_count, play_yes_count, round(humidity_high_yes_prob, 3)))

wind_strong_yes_count = sum(1 for row in data if row["Гра"] == "Так" and row["Вітер"] == "Сильний")
wind_strong_yes_prob = wind_strong_yes_count / play_yes_count
print("Ймовірність сильного вітру під час гри: {0}/{1} = {2}".format(wind_strong_yes_count, play_yes_count, round(wind_strong_yes_prob, 3)))

overall_probability = play_yes_prob * overcast_yes_prob * humidity_high_yes_prob * wind_strong_yes_prob
print("\nЙмовірність того, що гра відбувається з умовами Хмарно, Висока Вологість, Сильний Вітер:"
      " \n{:.3f} * {:.3f} * {:.3f} * {:.3f} = {:.4f}".format(play_yes_prob, overcast_yes_prob, humidity_high_yes_prob, wind_strong_yes_prob, overall_probability))
