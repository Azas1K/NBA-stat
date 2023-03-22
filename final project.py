import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme()

# importing data base into the code
data = pd.read_csv("all_seasons.csv")
print(data.head())
print()
print(data.dtypes)


def rounding(number):
    number = round(number)
    return number


data["player_weight"] = data["player_weight"].apply(rounding)
data["player_height"] = data["player_height"].apply(rounding)

# average height player of NBA
average_hight = data["player_height"].mean()
print(average_hight)

# median age of player of NBA
median_weight = data["player_weight"].median()
print(median_weight)

# std of player of NBA weight
print(data["age"].std())
print()


# number of players in each season
fig, ax = plt.subplots()


def countres(country):
    if country == "USA":
        return country
    else:
        return "Non American"


players = data
players["country"] = players["country"].apply(countres)

americans = players[players["country"] == "USA"]
non_american = players[players["country"] == "Non American"]

number_of_people = sns.scatterplot(x=data["season"].value_counts(), y=data["season"].unique(), ax=ax, label="All")
sns.scatterplot(x=americans["season"].value_counts(), y=americans["season"].unique(),
                ax=ax, label="Americans", color="r")
sns.scatterplot(x=non_american["season"].value_counts(), y=non_american["season"].unique(),
                ax=ax, label="Non Americans", color="g")

number_of_people.axes.set_title("Number of player in each season", fontsize=16)
number_of_people.set_xlabel("Number of people", fontsize=14)
number_of_people.set_ylabel("Season №", fontsize=14)
plt.legend()
plt.show()

# соотношение кто сколько отыграл сезонов
# number_of_seasons_played = data["player_name"].value_counts()
# plt.hist(number_of_seasons_played)
# plt.title("Players/played seasons")
# plt.xlabel('Number of seasons')
# plt.ylabel('Number of people')
# plt.show()
#
# # игрок в среднем собирающий трипл-дабл за сезон (>10 очков, подборов и ассистирующих передач в среднем в каждом матче)
# best_tripple_double = data[data["ast"] >= 10]
# best_tripple_double = best_tripple_double[best_tripple_double["pts"] >= 10]
# best_tripple_double = best_tripple_double[best_tripple_double["reb"] >= 10]
# print(best_tripple_double["player_name"].value_counts())
#
#
# #
# # количество игроков из америки и других стран (уникальных и всего за все время)
# #
# fig1, ax1 = plt.subplots(2, 1)
#
#
# def countres(country):
#     if country == "USA":
#         return country
#     else:
#         return "Non American"
#
#
# players = data
# players["country"] = players["country"].apply(countres)
#
# ax1[0].pie(players["country"].value_counts(), labels=players['country'].unique(), autopct='%0.1f%%', startangle=90)
#
# players = data.drop_duplicates(subset=["player_name"])
# ax1[1].pie(players["country"].value_counts(), labels=players['country'].unique(), autopct='%0.1f%%', startangle=90)
# plt.title("over all seasons \n "
#           "THE DOMINATION OF ONE NATION \n"
#           "over unique players")
# plt.show()
#
#
# # количество задрафтованных и незадрафтаванных от страны
# def countres(country):
#     if country == "USA":
#         return country
#     else:
#         return "Non American"
#
#
# def draft_to_int(data):
#     if data == "Undrafted":
#         data = "0"
#     return int(data)
#
# def int_to_str(data):
#     if data == 0:
#         data = "Undrafted"
#     return str(data)
#
#
# only_unique = data.drop_duplicates(subset=["player_name"])
#
# only_unique["country"] = only_unique["country"].apply(countres)
# only_unique["draft_round"] = only_unique["draft_round"].apply(draft_to_int)
# only_unique = only_unique[only_unique["draft_round"] < 3]
# only_unique["draft_round"] = only_unique["draft_round"].apply(int_to_str)
#
# americans = only_unique[only_unique["country"] == "USA"]["draft_round"]
# non_american = only_unique[only_unique["country"] == "Non American"]["draft_round"]
#
# draft_numbers = only_unique["draft_round"].value_counts()
#
# americans.hist(color="green", label='Americans')
# non_american.hist(color="red", label='Non Americans')
# plt.title("American and non american player's draft")
# plt.xlabel('Draft round')
# plt.ylabel('number of people')
# plt.legend()
# plt.show()
#
#
# # соотношение роста и веса игроков
# barplot = sns.lineplot(data=data, y="player_weight", x="player_height")
# barplot.axes.set_title("Weight/height", fontsize=16)
# barplot.set_xlabel("Height", fontsize=14)
# barplot.set_ylabel("Weight", fontsize=14)
# plt.show()


## количество очков от возраста
# between20 = data[18 < data["age"] <= 30]
# between30 = data[30 < data["age"] <= 40]
# between40 = data[40 < data["age"] <= 50]
#
# bar_width = 0.25
# x = np.arange(len(data["age"].unique()))
#
# fig, ax = plt.subplots(figsize=(12, 12))
# sns.barplot(x=between20["age"], y=between20["pts"], width=bar_width, label='18-20')
# sns.barplot(x=between30["age"], y=between30["pts"], width=bar_width, label='20-30')
# sns.barplot(x=between40["age"], y=between40["pts"], width=bar_width, label='18-20')
# ax.set_xticks(x + bar_width / 2)
# plt.show()

# подборы от роста
rebounds = data[data["reb"] > 4]
boxplot = sns.boxplot(data=rebounds, x="player_height", y="reb")
boxplot.axes.set_title("Dependence of rebounds from player's height", fontsize=16)
boxplot.set_xlabel("Height", fontsize=14)
boxplot.set_ylabel("Rebounds", fontsize=14)
plt.show()
