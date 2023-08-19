# Create a class relation use matrix notation to represent a relation. 
#Include member function to check if the relation is reflexive, symmetric, anti Symmetrix, transitive. 
# Using these function check whether the given relation is POSET or equivalence function 


class RelationMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def is_reflexive(self):
        for i in range(self.size):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.size):
            for j in range(i+1, self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.size):
            for j in range(i+1, self.size):
                if self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == 1:
                    for k in range(self.size):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    def is_poset(self):
        return self.is_reflexive() and self.is_antisymmetric() and self.is_transitive()

    def is_equivalence(self):
        return self.is_reflexive() and self.is_symmetric() and self.is_transitive()


# Example usage
relation_matrix = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]

relation = RelationMatrix(relation_matrix)

print("Reflexive:", relation.is_reflexive())
print("Symmetric:", relation.is_symmetric())
print("Antisymmetric:", relation.is_antisymmetric())
print("Transitive:", relation.is_transitive())
print("Is POSET:", relation.is_poset())
print("Is Equivalence:", relation.is_equivalence())
