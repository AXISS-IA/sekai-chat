import random

class SekaiUser:
    def __init__(self, username, balance=1000):
        self.username = username
        self.balance = balance
        self.inventory = []
        self.status = "Libre"
        self.infractions = 0

    def __str__(self):
        return f"[{self.status}] {self.username} - Balance: {self.balance}¥ - Objetos: {len(self.inventory)}"

class SekaiEngine:
    def __init__(self):
        self.relics_pool = {
            "Común": ["Llave de Cobre", "Fragmento de Código"],
            "Raro": ["Daga de Cristal", "Pase de Distrito"],
            "Épico": ["Ojo de Vigilante", "Cifrado Maestro"],
            "Legendario": ["Reliquia Ancestral de Sekai"]
        }

    def pull_gacha(self, user):
        cost = 500
        if user.balance < cost:
            return "❌ Fondos insuficientes."
        user.balance -= cost
        rarity = random.choices(["Común", "Raro", "Épico", "Legendario"], weights=[70, 20, 8, 2])[0]
        item = random.choice(self.relics_pool[rarity])
        user.inventory.append(item)
        return f"✨ ¡Obtenido [{rarity}] {item}!"

    def apply_prison_protocol(self, user, reason):
        user.status = "Prisionero"
        user.infractions += 1
        return f"🚨 PRISIÓN: {user.username} procesado por {reason}."

# Simulación rápida
engine = SekaiEngine()
player = SekaiUser("Explorer_01")
print(engine.pull_gacha(player))
