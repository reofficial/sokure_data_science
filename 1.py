import pandas as pd

# df = pd.read_json('sokureplays.json')
df = pd.read_pickle('sokureplays.pkl')

# print(df) 

count = 0

# for index, row in df.iterrows():
#     print(f"currently on id {row['id']}")
#     if row['server_country'] == "ph" or row['client_country'] == "ph":
#         print(f"ph games count so far: {count}")
#         count = count + 1

# print(f"ph games count: {count}")

# country_frequency = (df['server_country']+' ' + df['client_country']).str.lower().str.split().explode().value_counts()
# print(country_frequency)

# reimu_players = pd.DataFrame({'Player': []})

# for index, row in df.iterrows():
#     print(f"currently on id {row['id']}")
#     if row['server_character'] == "reimu":
#         new = {'Player': row['server_nick']}
#         reimu_players = reimu_players._append(new, ignore_index=True)
#     if row['client_character'] == "reimu":
#         new = {'Player': row['server_nick']}
#         reimu_players = reimu_players._append(new, ignore_index=True)

# reimu_players.drop_duplicates()
# reimu_players.to_pickle('reimu_players.pkl')

# reimu_players = pd.read_pickle('reimu_players.pkl')
# reimu_players = reimu_players.drop_duplicates(subset=['Player'])
# reimu_players.to_pickle('reimu_players.pkl')
# print(reimu_players[:30])

