from enum import Enum


class API_TAGS(Enum):
    VEHICLES = 'Vehicles'
    PARTS = 'Parts'
    LISTINGS = 'Listings'


metadata_tag_info = [
    {'name': API_TAGS.VEHICLES.value, 'description': 'Vehicle purchase and lifecycle records'},
    {'name': API_TAGS.PARTS.value, 'description': 'Part inventory records by vehicle'},
    {'name': API_TAGS.LISTINGS.value, 'description': 'Marketplace listing records for parts'},
]
