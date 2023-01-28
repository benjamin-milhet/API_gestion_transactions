class Personne:

    name = ""
    solde = 0
    transactions = {}

    def __init__(self, _name, _solde):
        self.name = _name
        self.solde = _solde
        self.transactions = {}

    def __str__(self):
        res = "name: " + self.name + " - solde: " + str(self.solde) + "\n"
        for i in self.sortTransactionsParDate(self.transactions):
            res += str(i[1]) + "\n"
        return res

    def sortTransactionsParDate(self, transactions):
        return sorted(transactions.items(), key=lambda x: x[1][2])

