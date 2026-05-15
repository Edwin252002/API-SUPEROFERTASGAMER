from fastapi import HTTPException
import requests

BASE_URL = "[https://www.gamerpower.com/api](https://www.gamerpower.com/api)"


def get_giveaways():
    try:
        response = requests.get("https://www.gamerpower.com/api/giveaways")
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        
        raise HTTPException(status_code=502, detail=f"Error al conectar con GamerPower: {str(e)}")

def get_premium_giveaways(min_value: float = 10.0):
    """Filtra juegos que tienen un valor superior al mínimo indicado."""
    all_games = get_giveaways()
    premium_games = []
    
    for game in all_games:
        worth = game.get("worth", "0")
        
        try:
            price_value = float(worth.replace('$', '').replace('N/A', '0'))
            if price_value >= min_value or worth == "N/A":
                premium_games.append(game)
        except ValueError:
            continue
            
    return premium_games

def categorize_giveaway(game):
    worth_str = str(game.get("worth", "0"))
    try:
        price = float(worth_str.replace('$', '').replace('N/A', '0').strip())
    except:
        price = 0.0

    if price >= 50:
        return "LEGENDARIO"
    elif price >= 20 or (game.get("platforms") == "PC" and price > 10):
        return "EPICO"
    else:
        return "NORMAL"

def get_giveaways_by_quality(target_quality: str):
    all_games = get_giveaways()
    filtered = []
    
    for g in all_games:
        quality = categorize_giveaway(g)
        if quality.lower() == target_quality.lower():
            
            g["quality_rank"] = quality
            filtered.append(g)
            
    return filtered