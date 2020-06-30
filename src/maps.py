from folium import Map, Marker, Icon, FeatureGroup, LayerControl, Choropleth
from folium.plugins import HeatMap


def mapa(coord):
    """
    Crea un mapa a partir de latitud y longitud
    """
    m = Map(location=coord,zoom_start=14)
    for i, row in data.iterrows():
        Marker(
            location=row[["latitude","longitude"]],
            tooltip=row["name"],
        ).add_to(m)
    return m