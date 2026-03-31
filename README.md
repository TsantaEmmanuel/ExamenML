 ISPM : https://ispm-edu.com/index.php 


  - NOM du groupe : Coder 
  - Nom des membres du groupe : 
    RANDRIANARISON Nomenjanahary Judicael , IGGLIA 4A N° 47 
    RAJAONARISON Tsanta Emmanuël          , IGGLIA 4A N° 34
    RAKOTONARIVO Nomenjanahary Faneva     ,  IGGLIA 4A N° 48

  - Description du projet: 
   ce projet consiste à développer une intelligence artificielle de Morpion en utilisant des techniques de Machine Learning. Les données sont générées automatiquement grâce à l’algorithme Minimax, puis transformées en variables pour entraîner des modèles capables de prédire l’issue d’une partie.Une interface interactive permet ensuite de jouer au Morpion en mode joueur contre joueur, contre une IA basée sur le Machine Learning, ou en mode hybride combinant Minimax et apprentissage automatique.

  - Structure du repository :

  Morpion_ML_Hackathon/
   ├── app.py                          # Interface Streamlit (Étape 4)
   ├── generator.py                    # Script Minimax pour créer le CSV (Étape 0)
   ├── notebook.ipynb                  # Analyse EDA et modèles (Étapes 1, 2, 3)
   ├── requirements.txt                # Liste des bibliothèques à installer 
   ├── README.md                       # Rapport final et réponses aux questions Q1-Q4 
   ├── ressources/                     # Dossier pour les données et modèles 
   │   │── dataset.csv                 # Le dataset généré (Livrable 2) 
   │   ├── ia_model_wins.pkl           # Modèle pour la victoire de X 
   │   └── ia_odel_draw.pkl            # Modèle pour le match nul 
   └── interface/                      # Assets/images


  - Réponses aux questions (voir 5.) : 

   Q1 — Analyse des coefficients
   Pour chaque modèle (x_wins et is_draw), quelles cases du plateau — et quelles occupations (X ou O) — ont les coefficients les plus élevés en valeur absolue ? La case centrale est-elle particulièrement influente ? En quoi est-ce cohérent avec la stratégie humaine ?

   Réponse
   Pour le modèle x_wins, les cases les plus influentes sont la case centrale c4_x et les angles c0_x, c2_x, c6_x, c8_x pour X
   Pour le modèle is_draw, certaines cases occupées par O (c1_o, c3_o, c5_o, c7_o) ont un impact notable
   Les positions occupées par X influencent surtout la victoire, celles occupées par O influencent la probabilité de nulle
   La case centrale est cruciale : contrôler le centre maximise les lignes gagnantes possibles et reflète la stratégie humaine classique du Morpion

   Q2 — Déséquilibre des classes
   Le dataset est-il équilibré entre x_wins = 1 et x_wins = 0 ? Même question pour is_draw. Quelle métrique privilégiez-vous en conséquence (Accuracy, F1, AUC…) et pourquoi ?

   Réponse
   x_wins est légèrement déséquilibré, avec plus de positions gagnantes que perdues
   is_draw est une classe minoritaire, donc rare
   La métrique F1-Score est préférable car elle combine précision et rappel, adaptée aux classes déséquilibrées
   AUC peut aussi être utilisée pour comparer la capacité du modèle à distinguer les classes

   Q3 — Comparaison des deux modèles
   Lequel des deux classificateurs obtient le meilleur score ? Pourquoi l’un est-il plus difficile à apprendre que l’autre ? Dans quels types de positions vos modèles se trompent-ils le plus ?

   Réponse
   Le modèle x_wins obtient généralement un meilleur score que le modèle is_draw
   Prédire une victoire est plus simple que de détecter une nulle rare et complexe
   Les erreurs fréquentes surviennent dans les positions où plusieurs lignes sont possibles ou quand la différence entre un état perdant et une nulle est subtile

   Q4 — Mode hybride
   En mode Hybride, observez-vous une différence de comportement par rapport au mode IA-ML pur ? Le joueur hybride évite-t-il mieux les pièges ? Décrivez qualitativement

   Réponse
   Le mode hybride (Minimax + ML) évite mieux les pièges car Minimax empêche la perte immédiate
   L’IA utilise le modèle ML pour évaluer les positions et accélérer la recherche
   Le joueur hybride agit plus “humainement” en bloquant efficacement les lignes gagnantes adverses et en choisissant des positions favorables

    lien vers la vidéo de présentation : 

