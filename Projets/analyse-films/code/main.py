print(df.isnull().sum())

# convertir la colonne release_date en datetime
df['release_date'] = pd.to_datetime(df['release_date'])
print(df.info('release_date'))

# Analyse des données
# Genre les plus populaire
genres = df['genres'].str.split('|').explode()
genres_counts= Counter(genres)
print(genres_counts.most_common(10))

# Films les plus rentrables
df['profit']=df['revenue'] - df['budget']
top_profit_movies= df.sort_values(by='profit', ascending=False).head(10)[['title', 'profit']]
print(top_profit_movies)

# corélation entre budget et receettes

sns.scatterplot(data=df, x='budget', y='revenue')
plt.title('Corrélation entre budget et recettes')
print(plt.show())

correlation = df['budget'].corr(df['revenue'])
print(f"La correlation entre le budget et les receettes est de {correlation:.2f}")

# Visualiser les données 
# les genres les plus populaire 
sns.barplot(x=list(genres_counts.keys())[:10], y=list(genres_counts.values())[:10])
plt.title('Genres les plus populaires')
plt.xticks(rotation=45)
plt.show()

# Les votes au fil du temps
df['release_year'] = df['release_date'].dt.year
avg_vote_by_year = df.groupby('release_year')['vote_average'].mean()
sns.lineplot(x=avg_vote_by_year.index, y=avg_vote_by_year.values)
plt.title('Évolution des votes moyens par année')
plt.show()

