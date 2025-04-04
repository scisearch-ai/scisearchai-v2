import spacy
from typing import Dict

nlp = spacy.load("pt_core_news_sm")

class PICOAnalyzer:
    def __init__(self):
        self.templates = {
            'P': {
                'patterns': ['dor no joelho', 'osteoartrite', 'artrose'],
                'default': 'pacientes com dor musculoesquelética'
            },
            'I': {
                'patterns': ['exercício', 'yoga', 'fisioterapia'],
                'default': 'intervenção não especificada'
            }
        }

    def analyze_question(self, question: str) -> Dict[str, str]:
        doc = nlp(question.lower())
        pico = {
            'P': self._extract_component(doc, 'P'),
            'I': self._extract_component(doc, 'I'),
            'C': 'placebo/controle',
            'O': 'melhora clínica'
        }
        return pico

    def _extract_component(self, doc, component: str) -> str:
        for token in doc:
            if any(pattern in token.text for pattern in self.templates[component]['patterns']):
                return token.text
        return self.templates[component]['default']