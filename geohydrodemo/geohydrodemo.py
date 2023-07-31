"""Main module."""
import os
import ipyleaflet
from ipyleaflet import TileLayer, FullScreenControl, LayersControl, DrawControl, MeasureControl, ScaleControl
from .utils import *

class Map(ipyleaflet.Map):
    """This Map class inherits thr ipyleaflet Map class

    Args:
        ipyleaflet (ipyleaflet.Map): An ipyleaflet map
    """
    def __init__(self, **kwargs):
        
        if "center" not in kwargs:
            kwargs["center"] = [40, -100]
        if 'zoom' not in kwargs:
            kwargs['zoom'] = 4
        if 'scroll_wheel_zoom' not in kwargs:
            kwargs['scroll_wheel_zoom'] = True

        super().__init__(**kwargs)  #inherit from ipyleaflet

        if 'height' not in kwargs:
            self.layout.height = "500px"
        else:
            self.layout.height = kwargs['height']

        self.add_control(FullScreenControl())
        self.add_control(LayersControl(position="topright"))
        self.add_control(DrawControl(position='topleft'))
        self.add_control(MeasureControl())
        self.add_control(ScaleControl(position='bottomleft'))

        if "google_map" not in kwargs:
            layer = TileLayer(
                url="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
                attribution="Google",
                name="Google Maps",
            )
            self.add_layer(layer)
    

    def add_geojson(self, in_geojson, style = None, layer_name = 'Untitled'):
        """Add a GeoJSON file to the map

        Args:
            in_geojson (str)): The file path to the input GeoJSON
            style (dict, optional): The style for the GeoJSON file. Defaults to None.
            layer_name (str, optional): The layer name for the GeoJSON file. Defaults to 'Untitled'.

        Raises:
            FileNotFoundError: if the provided file path does not exist.
            TypeError: If the input geojson is not a str or dict. 
        """

        import json
        if layer_name == "Untitled":
            layer_name = 'Untitled' + ' '+ random_string()

        if isinstance(in_geojson, str): 
            if not os.path.exists(in_geojson):
                raise FileNotFoundError('The provided GeoJSON file could not be found')
            
            with open(in_geojson) as f:
                data = json.load(f)

        elif isinstance(in_geojson, dict):
            data = in_geojson

        else:
            raise TypeError('The input geojson must be a type of str or dict')
        
        if style is None:
            style = {
                "stroke": True,
                'color' : '#000000',
                'weight': 2,
                'opacity': 1,
                'fill': True,
                'fillColor':'#000000',
                'fillOpacity':0.4,
            }

        geo_json = ipyleaflet.GeoJSON(data=data, style=style, name = layer_name)
        self.add_layer(geo_json)

    def add_shapefile(self, in_shp, style = None, layer_name = 'Untitled'):
        """Add a shapefile layer to the map

        Args:
            in_shp (str): The file path to the input shapefile
            style (dict, optional): The style dictionary. Defaults to None.
            layer_name (str, optional): The layer name for shapefile layer. Defaults to 'Untitled'.
        """        
        self.add_geojson(shp_to_geojson(in_shp), style=style, layer_name=layer_name)


def shp_to_geojson(in_shp, out_geojson = None):
    """Covert the shapefile to GeoJSON

    Args:
        in_shp (str): The file path to the input shapefile.
        out_geojson (str, optional): The file path to the output GeoJSON. Defaults to None.

    Raises:
        FileNotFoundError: if the input file does not exist.

    Returns:
        dict: The dictionary of the GeoJSON.
    """
    import json
    import shapefile

    in_shp = os.path.abspath(in_shp)

    if not os.path.exists(in_shp):
        raise FileNotFoundError('The provided shapfile could not be found')
    
    sf = shapefile.Reader(in_shp)
    geojson = sf.__geo_interface__

    if out_geojson is None:
        return geojson
    else:
        out_geojson = os.path.abspath(out_geojson)
        out_dir = os.path.dirname(out_geojson)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        with open(out_geojson, 'w') as f:
            f.write(json.dumps(geojson))

