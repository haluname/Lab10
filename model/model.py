from database.dao import DAO
import networkx as nx
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        self.G = nx.Graph()
        dao = DAO()
        filiali = dao.get_all_filiali()
        self.G.add_nodes_from(filiali)

        data = dao.get_data(threshold)
        for el in data:
            self.G.add_edge(el["nomeP"], el["nomeD"], weight=el["media"])

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        return  self.G.number_of_edges()


    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """

        return self.G.edges(data=True) #funzione che ritorna tutti i collegamenti sottoforma di lista di tuple
