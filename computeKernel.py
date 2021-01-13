import Grid2d
class Compute_kernel():
    
    def __init__(self):
        """ Constructeur de base"""
        self.current_grid = Grid2d.Grid2d()
        self.next_grid = Grid2d.Grid2d()

    def compute_rules(self,neighs_value,local_value):
        """
        Entrée :
         - neighs_value la liste des valeurs des voisins
         - local_value la valeur de la cellule
        Sortie :
         - new_state valeur du prochain état de la cellule 
        """
        # Calcul du nombre de voisin vivant, attention il ne faut 
        #  pas tenir compte de la cellule elle-même
        neighs_alive = sum(neighs_value) - local_value
        # Par défaut le nouvel état de la cellule est 0 ('morte')
        new_state = 0
        # R1 : une cellule morte avec exactement 3 voisins vivants
        #  devient vivante
        if local_value == 0 and neighs_alive == 3:
            new_state = 1
        # R2 : une cellule vivante avec 2 ou 3 voisines vivantes
        #  reste vivante
        if local_value == 1 and (neighs_alive == 2 or neighs_alive == 3):
            new_state = 1
        # R3 : une cellule vivante avec moins de 2 voisines vivantes 
        # ou plus de 3 voisines vivantes meurt
        if local_value == 1 and (neighs_alive < 2 or neighs_alive > 3):
            new_state = 0
        return new_state
