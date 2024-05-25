import json

# Carga los datos JSON
with open('comunas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Crea una nueva lista para almacenar los objetos de las comunas
comunas = []

# Itera sobre cada objeto en losF datos
for obj in data:
    # Itera sobre cada nombre en la lista de nombres
    for nombre in obj['fields']['nombre']:
        # Crea un nuevo objeto para la comuna
        comuna = {
            'model': 'Arriendos.comuna',
            'fields': {
                'nombre': nombre,
                'region': obj['fields']['region']
            }
        }
        # Añade el objeto de la comuna a la lista de comunas
        comunas.append(comuna)

# Imprime la nueva lista de comunas
print(json.dumps(comunas, indent=4))
with open('nuevas_comunas.json', 'w', encoding='utf-8') as f:
    json.dump(comunas, f, ensure_ascii=False, indent=4)