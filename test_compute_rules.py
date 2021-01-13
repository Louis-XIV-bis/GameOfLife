from computeKernel import * 
import unittest
class Test_compute_rules(unittest.TestCase):
    """Tests unitaires sur la méthode compute_rules"""
    # exemple R1
    # [1  0  0]
    # [0 (0) 1]
    # [0  1  0]
    # valeur cellule locale 0  : 0
    # valeurs cellule voisines : [1,0,0,0,0,1,0,1,0] 
    # resultat : vie -> 1 
    def test_R1_1(self):
        n_value = [1,0,0,0,0,1,0,1,0]
        l_value = 0
        res = Compute_kernel().compute_rules(neighs_value=n_value,
                                             local_value=l_value)
        self.assertEqual(res,1)

    # exemple R2 1
    # [1  0  0]
    # [0 (1) 0]
    # [0  1  0]
    # valeur cellule locale 0  : 1
    # valeurs cellule voisines : [1,0,0,0,1,0,0,1,0]
    # resultat : vie -> 1 
    def test_R2_1(self):
        n_value = [1,0,0,0,1,0,0,1,0]
        l_value = 1
        res = Compute_kernel().compute_rules(neighs_value=n_value,
                                             local_value=l_value)
        self.assertEqual(res,1)
        

        
if __name__ == '__main__':
    unittest.main()                   