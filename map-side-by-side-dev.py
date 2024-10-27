import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

def create_scotland_map():
    """
    Creates a map of Scotland highlighting Musselburgh Athletic FC
    """
    
    # Set up the figure with a specific background color
    fig = plt.figure(figsize=(12, 16), facecolor='#F5F5F5')
    
    # Create a custom projection centered on Scotland
    proj = ccrs.TransverseMercator(central_longitude=-4.0, central_latitude=57.0)
    ax = fig.add_subplot(1, 1, 1, projection=proj)
    
    # Set map bounds to include all of Scotland and northern England
    ax.set_extent([-8, 0, 54.5, 60.5], crs=ccrs.PlateCarree())
    
    # Add detailed base features
    ax.add_feature(cfeature.LAND.with_scale('50m'), facecolor='#E8E8E8', alpha=0.6)
    ax.add_feature(cfeature.OCEAN.with_scale('50m'), facecolor='#ADD8E6', alpha=0.4)
    
    # Add detailed coastlines
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), 
                  edgecolor='#666666', 
                  linewidth=1.5,
                  alpha=0.8)
    
    # Add rivers
    ax.add_feature(cfeature.RIVERS.with_scale('50m'), 
                  edgecolor='#4BA6DB', 
                  linewidth=1.0,
                  alpha=0.6)
    
    # Add urban areas
    urban = cfeature.NaturalEarthFeature('cultural', 
                                        'urban_areas', 
                                        '50m', 
                                        facecolor='#FFE5E5',
                                        edgecolor='#FF9999')
    ax.add_feature(urban, alpha=0.4)
    
    # Major cities across Scotland
    cities = {
        'Edinburgh': (-3.19, 55.95),
        'Glasgow': (-4.25, 55.86),
        'Aberdeen': (-2.09, 57.15),
        'Inverness': (-4.22, 57.47),
        'Dundee': (-2.97, 56.46),
        'Perth': (-3.44, 56.40),
        'Stirling': (-3.94, 56.12),
        'Kirkwall': (-2.96, 58.98),  # Orkney
        'Musselburgh': (-3.0648, 55.9418),
        'Newcastle': (-1.61, 54.97),  # Reference point in England
        'Carlisle': (-2.94, 54.89)    # Reference point in England
    }
    
    # Plot cities
    for city, coords in cities.items():
        # Adjust size and color based on city importance
        if city == 'Musselburgh':
            size = 12
            color = '#FF4444'
            fontsize = 10
            fontweight = 'bold'
        elif city in ['Edinburgh', 'Glasgow', 'Aberdeen', 'Inverness']:
            size = 10
            color = '#FF8888'
            fontsize = 9
            fontweight = 'bold'
        else:
            size = 8
            color = '#FF8888'
            fontsize = 8
            fontweight = 'normal'
        
        ax.plot(coords[0], coords[1], 
                marker='o', 
                color=color, 
                markersize=size, 
                transform=ccrs.PlateCarree(),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])
        
        # Adjust text position based on location to avoid overcrowding
        x_offset = 0.1
        y_offset = 0
        if city == 'Kirkwall':
            x_offset = 0.2  # Move label right
        elif city in ['Glasgow', 'Inverness']:
            x_offset = -0.3  # Move label left
        
        ax.text(coords[0] + x_offset, coords[1] + y_offset, 
                city, 
                transform=ccrs.PlateCarree(),
                fontsize=fontsize,
                fontweight=fontweight,
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])
    
    # Add Olivebank Stadium location with special marker
    stadium_coords = (-3.0648, 55.9418)
    ax.plot(stadium_coords[0], stadium_coords[1], 
            marker='*', 
            color='#FFD700', 
            markersize=20, 
            transform=ccrs.PlateCarree(),
            path_effects=[pe.withStroke(linewidth=3, foreground='black')])
    
    # Add stadium label with leader line
    ax.annotate('Olivebank Stadium\nMusselburgh Athletic FC',
                xy=(stadium_coords[0], stadium_coords[1]),
                xytext=(stadium_coords[0] - 0.5, stadium_coords[1] - 0.2),
                transform=ccrs.PlateCarree(),
                fontsize=11,
                fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'),
                arrowprops=dict(arrowstyle='->',
                              connectionstyle='arc3,rad=0.2',
                              color='black'))
    
    # Add gridlines
    gl = ax.gridlines(draw_labels=True, 
                     linewidth=0.5, 
                     color='gray', 
                     alpha=0.5, 
                     linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    
    # Add a title with club colors
    plt.title('Musselburgh Athletic FC\nLocation in Scotland',
             pad=20,
             fontsize=16,
             fontweight='bold')
    
    # Add a north arrow
    x, y, arrow_length = -7.5, 55, 0.3
    ax.annotate('N', xy=(x, y), xytext=(x, y-arrow_length),
                arrowprops=dict(facecolor='black', width=5, headwidth=15),
                ha='center', va='bottom',
                transform=ccrs.PlateCarree(),
                fontsize=12, fontweight='bold')
    
    # Add text box with club info
    club_info = "Musselburgh Athletic FC\nFounded: 1924\nGround: Olivebank Stadium\nLeague: East of Scotland Football League"
    plt.figtext(0.15, 0.15, club_info,
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='black'),
                fontsize=10,
                transform=None)
    
    return fig

# Create the map
fig = create_scotland_map()
plt.show()
