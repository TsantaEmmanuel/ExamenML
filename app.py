import streamlit as st
import joblib
import numpy as np

# --- 1. CHARGEMENT DES MODÈLES ---
# Assurez-vous que les chemins sont corrects sur votre machine
try:
    model_wins = joblib.load('ressources/ia_model_wins.pkl')
    model_draw = joblib.load('ressources/ia_model_draw.pkl')
except:
    st.error("Erreur : Impossible de charger les modèles .pkl. Vérifiez les chemins.")

st.set_page_config(page_title="Morpion", layout="centered")
st.title("Morpion ")

# --- 2. INITIALISATION DE L'ÉTAT DU JEU ---
if 'board' not in st.session_state:
    st.session_state.board = ["Vide"] * 9
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'active_player' not in st.session_state:
    st.session_state.active_player = "X" # X commence toujours

# --- 3. LOGIQUE IA ---

def preparer_donnees(plateau):
    """Transforme le plateau en 18 features (9 pour X, 9 pour O)"""
    x_features = [1 if c == "X" else 0 for c in plateau]
    o_features = [1 if c == "O" else 0 for c in plateau]
    return np.array(x_features + o_features).reshape(1, -1)

def evaluer_position(plateau):
    """Score heuristique basé sur vos modèles ML"""
    data = preparer_donnees(plateau)
    prob_x_wins = model_wins.predict_proba(data)[0][1]
    prob_draw = model_draw.predict_proba(data)[0][1]
    # Score : plus il est haut, mieux c'est pour O (l'IA)
    # On inverse le score de X_wins car l'IA joue O
    return (1 - prob_x_wins) + (0.5 * prob_draw)

def check_win(b):
    lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for l in lines:
        if b[l[0]] == b[l[1]] == b[l[2]] != "Vide":
            return b[l[0]]
    if "Vide" not in b: return "Nul"
    return None

def minimax(board, depth, alpha, beta, is_maximizing):
    result = check_win(board)
    if result == "X": return -10
    if result == "O": return 10
    if result == "Nul": return 0
    
    if depth == 0:
        return evaluer_position(board)

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "Vide":
                board[i] = "O"
                score = minimax(board, depth - 1, alpha, beta, False)
                board[i] = "Vide"
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha: break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "Vide":
                board[i] = "X"
                score = minimax(board, depth - 1, alpha, beta, True)
                board[i] = "Vide"
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha: break
        return best_score

def jouer_ia(mode):
    best_score = -float('inf')
    move = None
    board_copy = list(st.session_state.board)
    
    for i in range(9):
        if board_copy[i] == "Vide":
            board_copy[i] = "O"
            if mode == "IA (ML)":
                score = evaluer_position(board_copy)
            else: # Hybride
                score = minimax(board_copy, 3, -float('inf'), float('inf'), False)
            board_copy[i] = "Vide"
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        st.session_state.board[move] = "O"
        st.session_state.active_player = "X" # Redonne la main à l'humain

# --- 4. INTERFACE UTILISATEUR ---

st.sidebar.header("Paramètres")
mode = st.sidebar.selectbox("Configuration", ["vs Human", "IA (ML)", "IA (Hybride)"])

if st.sidebar.button("Nouvelle Partie"):
    st.session_state.board = ["Vide"] * 9
    st.session_state.winner = None
    st.session_state.active_player = "X"
    st.rerun()

st.write(f"### Tour du joueur : **{st.session_state.active_player}**")

# Grille de jeu
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        content = st.session_state.board[i]
        label = " " if content == "Vide" else content
        
        # Bouton désactivé si la case est prise ou si le jeu est fini
        if st.button(label, key=f"cell_{i}", use_container_width=True, 
                     disabled=(content != "Vide" or st.session_state.winner is not None)):
            
            # Action du joueur actuel (X ou O)
            current = st.session_state.active_player
            st.session_state.board[i] = current
            
            # Vérification immédiate
            win_status = check_win(st.session_state.board)
            
            if win_status:
                st.session_state.winner = win_status
            else:
                # Changement de tour
                if mode == "vs Human":
                    st.session_state.active_player = "O" if current == "X" else "X"
                else:
                    # Contre l'IA, l'IA joue immédiatement après X
                    st.session_state.active_player = "O"
                    jouer_ia(mode)
                    st.session_state.winner = check_win(st.session_state.board)
            
            st.rerun()

# Affichage des résultats
if st.session_state.winner:
    if st.session_state.winner == "Nul":
        st.info("🤝 Match nul !")
    else:
        st.success(f"🎉 Le joueur **{st.session_state.winner}** a gagné !")

# --- 5. VISUALISATION DES MODÈLES (Optionnel pour le projet) ---
with st.expander("Probabilités des modèles ML (Position actuelle)"):
    data = preparer_donnees(st.session_state.board)
    p_win = model_wins.predict_proba(data)[0][1]
    p_draw = model_draw.predict_proba(data)[0][1]
    st.progress(p_win, text=f"Probabilité victoire X : {p_win:.2%}")
    st.progress(p_draw, text=f"Probabilité Match Nul : {p_draw:.2%}")