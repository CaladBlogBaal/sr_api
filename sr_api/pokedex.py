class Pokedex:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.type = data['type']
        self.species = data['species']
        self.abilities = data['abilities']
        self.height = data['height']
        self.weight = data['weight']
        self.base_experience = data['base_experience']
        self.gender = data['gender']
        self.egg_groups = data['egg_groups']
        self.hp = data['stats']['hp']
        self.attack = data['stats']['attack']
        self.defense = data['stats']['defense']
        self.sp_atk = data['stats']['sp_atk']
        self.sp_def = data['stats']['sp_def']
        self.speed = data['stats']['speed']
        self.total = data['stats']['total']
        self.evolutionStage = data['family']['evolutionStage']
        self.evolutionLine = data['family']['evolutionLine']
        self.spriteNormal = data['sprites']['normal']
        self.spriteAnimated = data['sprites']['animated']
        self.description = data['description']
        self.generation = data['generation']