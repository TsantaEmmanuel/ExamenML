
1. Distribution des cibles
print("Distribution x_wins:")
print(df['x_wins'].value_counts())

print("\nDistribution is_draw:")
print(df['is_draw'].value_counts())

 Visualisation
 
fig, axes = plt.subplots(1, 2, figsize=(10,4))

sns.countplot(x='x_wins', data=df, ax=axes[0])
axes[0].set_title("Distribution x_wins")

sns.countplot(x='is_draw', data=df, ax=axes[1])
axes[1].set_title("Distribution is_draw")

plt.show()

2. Dataset équilibré ?


x_ratio = df['x_wins'].mean()
draw_ratio = df['is_draw'].mean()

print(f"% X gagne : {x_ratio:.2f}")
print(f"% Match nul : {draw_ratio:.2f}")






model_draw = LogisticRegression(max_iter=1000)
model_draw.fit(X_train, y_draw_train)

y_pred_draw = model_draw.predict(X_test)
print("=== MODELE DRAW ===")
print("Accuracy:", accuracy_score(y_draw_test, y_pred_draw))
print("F1 Score:", f1_score(y_draw_test, y_pred_draw))

cm = confusion_matrix(y_draw_test, y_pred_draw)

sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title("Confusion Matrix - Draw")
plt.show()
print("Comparaison:")
print("X_wins F1:", f1_score(y_win_test, y_pred_win))
print("Draw F1:", f1_score(y_draw_test, y_pred_draw))
import numpy as np

def plot_coefficients(model, title):
    coefs = model.coef_[0]
    
    x_coefs = coefs[::2]   # X
    o_coefs = coefs[1::2]  # O
    
    x_grid = np.array(x_coefs).reshape(3,3)
    o_grid = np.array(o_coefs).reshape(3,3)
    
    fig, axes = plt.subplots(1, 2, figsize=(10,4))
    
    sns.heatmap(x_grid, annot=True, cmap='coolwarm', ax=axes[0])
    axes[0].set_title(f"{title} - X positions")
    
    sns.heatmap(o_grid, annot=True, cmap='coolwarm', ax=axes[1])
    axes[1].set_title(f"{title} - O positions")
    
    plt.show()
    plot_coefficients(model_win, "X Wins Model")
plot_coefficients(model_draw, "Draw Model")


