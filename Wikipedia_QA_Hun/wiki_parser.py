import wikipedia
import squad

wikipedia.set_lang("hu")


def parse_entity(doc):
    
    texts = []

    for ent in doc.ents:    
        try:
           texts.append(wikipedia.page(wikipedia.search(ent.text)[0]).content)
        except wikipedia.exceptions.DisambiguationError:
            pass
        except IndexError:
            return texts

    return texts
