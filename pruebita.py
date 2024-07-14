import requests

def get_locations(locations, generation):
    regions = {
      'generation-i': 'kanto',
      'generation-ii': 'johto',
      'generation-iii': 'hoenn',
      'generation-iv': 'sinnoh',
      'generation-v': 'unova',
      'generation-vi': 'kalos'
    }
    filtered_location = []

    for location in locations:
      area_url = location['location_area']['url']
      area = requests.get(area_url).json()
      
      location_url = area['location']['url']
      location = requests.get(location_url).json()
      # print(location)
      # print("=========================================")

      if location['region']['name'] == regions[generation]:
        ruta = {"name": location['names'][-1]["name"], "region": location["region"]["url"][-2]}
        filtered_location.append(ruta)

    return filtered_location

url = f"https://pokeapi.co/api/v2/pokemon/tyranitar"
generation_url = f"https://pokeapi.co/api/v2/pokemon-species/tyranitar"

data = requests.get(url=url).json()
data_generation = requests.get(generation_url).json()['generation']['name']
data_locations = requests.get(data['location_area_encounters']).json()

filtered_locations = get_locations(data_locations, data_generation)

print("\n")
print(filtered_locations)