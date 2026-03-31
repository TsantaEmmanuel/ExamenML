print("Distribution x_wins:")
print(df['x_wins'].value_counts())

print("\nDistribution is_draw:")
print(df['is_draw'].value_counts())



1. Distribution des cibles
print("Distribution x_wins:")
print(df['x_wins'].value_counts())

print("\nDistribution is_draw:")
print(df['is_draw'].value_counts())
📉 Visualisation
fig, axes = plt.subplots(1, 2, figsize=(10,4))

sns.countplot(x='x_wins', data=df, ax=axes[0])
axes[0].set_title("Distribution x_wins")

sns.countplot(x='is_draw', data=df, ax=axes[1])
axes[1].set_title("Distribution is_draw")

plt.show()
⚖️ 2. Dataset équilibré ?
x_ratio = df['x_wins'].mean()
draw_ratio = df['is_draw'].mean()

print(f"% X gagne : {x_ratio:.2f}")
print(f"% Match nul : {draw_ratio:.2f}")
