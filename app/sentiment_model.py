def analise_sentimento(text: str) -> str:
    
    positivas = ["alegre", "bom", "pra cima", "ótimo", "feliz", "excelente", "maravilhoso", "😍", "🥰", "amei", "bem"]
    negativas = ["ruim", "péssimo", "horrível", "merda", "perdi tempo", "bosta", "pra baixo", "😡", "odiei", "mal"]

    text = text.lower()

    if any(word in text for word in positivas):
        return "Positivo"
    
    if any(word in text for word in negativas):
        return "Negativo"

    return "Neutro"