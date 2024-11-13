import folium
from datetime import datetime

def create_match_map(opponent, match_datetime, is_home_game, away_location=None):
    """
    Creates a map showing Carrick Rangers match location(s)
    
    Parameters:
    opponent (str): Name of the opposing team
    match_datetime (datetime): Date and time of the match
    is_home_game (bool): Whether it's a home game
    away_location (tuple): (latitude, longitude, venue_name) for away games
    """
    
    # Carrick Rangers home ground (Taylor's Avenue) coordinates
    home_coords = (54.7147, -5.8055)
    
    # Create map centered on home ground
    m = folium.Map(location=home_coords, zoom_start=12)
    
    # Add marker for home ground
    folium.Marker(
        home_coords,
        popup='Taylor\'s Avenue',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    # If it's an away game, add marker for away venue and adjust zoom
    if not is_home_game and away_location:
        # Extract just the coordinates for the marker
        away_coords = (away_location[0], away_location[1])
        away_venue_name = away_location[2]
        
        folium.Marker(
            away_coords,  # Use just the coordinates here
            popup=f'{away_venue_name}',  # Use the venue name in popup
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
        
        # Adjust zoom to show both locations
        bounds = [home_coords, away_coords]
        m.fit_bounds(bounds)
    
    # Add title as HTML
    match_day = match_datetime.strftime('%A')
    match_time = match_datetime.strftime('%H:%M')
    venue = "Taylor's Avenue" if is_home_game else away_location[2] if away_location else "Away Venue"
    
    title_html = f'''
        <h3 align="center">Carrick Rangers vs {opponent}<br>
        {venue}<br>
        {match_day} at {match_time}</h3>
    '''
    
    m.get_root().html.add_child(folium.Element(title_html))
    
    return m

# Example usage:
match_time = datetime(2024, 11, 16, 7, 00)  # Example: Nov 15, 2024 at 19:45

# For a home game:
home_map = create_match_map(
    opponent="Crusaders",
    match_datetime=match_time,
    is_home_game=True
)
home_map.save('home_game_map.html')

# For an away game:
#away_map = create_match_map(
#    opponent="Glentoran FC",
#    match_datetime=match_time,
#    is_home_game=False,
#    away_location=(54.6053, -5.8828, "The Oval")  # latitude, longitude, venue name
#)
#away_map.save('away_game_map.html')
