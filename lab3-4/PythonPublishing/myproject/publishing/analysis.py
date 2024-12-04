# analysis.py
import pandas as pd
from .models import Author

def analyze_author_publications():
    authors = Author.objects.all()
    data = {
        'first_name': [author.first_name for author in authors],
        'last_name': [author.last_name for author in authors],
        'number_of_publications': [author.number_of_publications for author in authors]
    }
    df = pd.DataFrame(data)

    # Обчислення статистичних показників
    mean = df['number_of_publications'].mean()
    median = df['number_of_publications'].median()
    minimum = df['number_of_publications'].min()
    maximum = df['number_of_publications'].max()

    return {
        'mean': mean,
        'median': median,
        'minimum': minimum,
        'maximum': maximum
    }
