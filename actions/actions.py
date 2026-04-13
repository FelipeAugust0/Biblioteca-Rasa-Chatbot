from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionBuscarPorTitulo(Action):

    def name(self) -> Text:
        return "action_buscar_por_titulo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        titulo = tracker.get_slot("titulo")

        url = f"https://openlibrary.org/search.json?title={titulo}"
        response = requests.get(url).json()

        if response["docs"]:
            livro = response["docs"][0]
            titulo_livro = livro.get("title", "Não encontrado")
            autor = livro.get("author_name", ["Desconhecido"])[0]

            dispatcher.utter_message(
                text=f"Livro encontrado:\nTítulo: {titulo_livro}\nAutor: {autor}"
            )
        else:
            dispatcher.utter_message(text="Nenhum livro encontrado.")

        return []


class ActionBuscarPorAutor(Action):

    def name(self) -> Text:
        return "action_buscar_por_autor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        autor = tracker.get_slot("autor")

        url = f"https://openlibrary.org/search.json?author={autor}"
        response = requests.get(url).json()

        if response["docs"]:
            livros = response["docs"][:3]

            mensagem = "Livros encontrados:\n"
            for livro in livros:
                mensagem += f"- {livro.get('title', 'Sem título')}\n"

            dispatcher.utter_message(text=mensagem)
        else:
            dispatcher.utter_message(text="Nenhum livro encontrado.")

        return []


class ActionBuscarPorAssunto(Action):

    def name(self) -> Text:
        return "action_buscar_por_assunto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        assunto = tracker.get_slot("assunto")

        url = f"https://openlibrary.org/search.json?subject={assunto}"
        response = requests.get(url).json()

        if response["docs"]:
            livros = response["docs"][:3]

            mensagem = f"Livros sobre {assunto}:\n"
            for livro in livros:
                mensagem += f"- {livro.get('title', 'Sem título')}\n"

            dispatcher.utter_message(text=mensagem)
        else:
            dispatcher.utter_message(text="Nenhum livro encontrado.")

        return []