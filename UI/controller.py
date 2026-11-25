import flet as ft
from numpy.distutils.fcompiler import none

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        importo = self._view.importo_medio_minimo.value
        print(importo)
        if importo == "" or int(importo) <= 0:
            self._view.show_alert("INSERIRE UNA SOGLIA VALIDA")
            return

        self._model.costruisci_grafo(importo)
        nFiliali = self._model.get_num_nodes()
        nEdges = self._model.get_num_edges()
        i = 0
        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di filiali : {nFiliali}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Collegamenti : {nEdges}"))
        collegamenti = self._model.get_all_edges()
        for c in collegamenti:
            i += 1
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{i}) {c[0]} -> {c[1]} => importo medio per bonifico : {c[2]['weight']}"))

        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO
