"""
Workload with cache
"""

import re
from functools import lru_cache

from pymorphy3 import MorphAnalyzer

regexp = re.compile(r"\w+")
morph = MorphAnalyzer()


@lru_cache
def get_normal_form(word: str) -> str:
    """
    Get normal form of the word

    Parameters
    ----------
    word : str
        Word for getting normal form
    
    Returns
    -------
    str
        Normal form of the word
    """
    return morph.parse(word)[0].normal_form


def process_text(text: str) -> str:
    """
    Func for process text

    Parameters
    ----------
    text : str
        Text for processing

    Returns
    -------
    str
        Processed text
    """
    return " ".join(map(lambda x: get_normal_form(str(x)), regexp.findall(text)))
