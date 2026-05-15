from fastapi import APIRouter
from app.services import get_giveaways, get_premium_giveaways, get_giveaways_by_quality
from typing import List
from app.schemas import Giveaway
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.get("/regalos", response_model=List[Giveaway])
def list_giveaways():
    return get_giveaways()

@router.get("/reporte-diario", response_class=PlainTextResponse)
def generate_daily_report(min_val: float = 5.0):
    games = get_premium_giveaways(min_val)
    
    report = f"RESUMEN DE JUEGOS GRATIS ({len(games)} encontrados)\n"
    report += "="*40 + "\n\n"
    
    for g in games:
        # Acceso seguro a las llaves del diccionario
        title = g.get('title', 'Sin título').upper()
        worth = g.get('worth', 'Desconocido')
        url = g.get('open_giveaway_url', 'No disponible')
        
        report += f" {title}\n Valor: {worth}\n: {url}\n"
        report += "-"*20 + "\n"
        
    return report # Debe ser un string puro

@router.get("/buscar-por-calidad")
def search_by_quality(calidad: str = "epico"):
    """
    Busca juegos por calidad: normal, epico o legendario.
    """
    results = get_giveaways_by_quality(calidad)
    return {
        "calidad_buscada": calidad,
        "cantidad": len(results),
        "juegos": results
    }