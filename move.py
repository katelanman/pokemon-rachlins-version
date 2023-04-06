import random
import math


class Move:
    TYPE_ADVANTAGE = {
        "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 1,
                   "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 0.5, "Ghost": 0, "Dragon": 1, "Dark": 1,
                   "Steel": 0.5, "Fairy": 1},
        "Fire": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Grass": 2, "Electric": 1, "Ice": 2, "Fighting": 1,
                 "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 2, "Rock": 0.5, "Ghost": 1, "Dragon": 0.5,
                 "Dark": 1, "Steel": 2, "Fairy": 1},
        "Water": {"Normal": 1, "Fire": 2, "Water": 0.5, "Grass": 0.5, "Electric": 1, "Ice": 1, "Fighting": 1,
                  "Poison": 1, "Ground": 2, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 0.5,
                  "Dark": 1, "Steel": 1, "Fairy": 1},
        "Grass": {"Normal": 1, "Fire": 0.5, "Water": 2, "Grass": 0.5, "Electric": 1, "Ice": 1, "Fighting": 1,
                  "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1,
                  "Dragon": 0.5, "Dark": 1, "Steel": 0.5, "Fairy": 1},
        "Electric": {"Normal": 1, "Fire": 1, "Water": 2, "Grass": 0.5, "Electric": 0.5, "Ice": 1, "Fighting": 1,
                     "Poison": 1, "Ground": 0, "Flying": 2, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1,
                     "Dragon": 0.5, "Dark": 1, "Steel": 1, "Fairy": 1},
        "Ice": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Grass": 2, "Electric": 1, "Ice": 0.5, "Fighting": 1,
                "Poison": 1, "Ground": 2, "Flying": 2, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2,
                "Dark": 1, "Steel": 0.5, "Fairy": 1},
        "Fighting": {"Normal": 2, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 2, "Fighting": 1,
                     "Poison": 0.5, "Ground": 1, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Rock": 2, "Ghost": 0,
                     "Dragon": 1, "Dark": 2, "Steel": 2, "Fairy": 0.5},
        "Poison": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 2, "Electric": 1, "Ice": 1, "Fighting": 1,
                   "Poison": 0.5, "Ground": 0.5, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 0.5, "Ghost": 0.5,
                   "Dragon": 1, "Dark": 1, "Steel": 0, "Fairy": 2},
        "Ground": {"Normal": 1, "Fire": 2, "Water": 1, "Grass": 0.5, "Electric": 2, "Ice": 1, "Fighting": 1,
                   "Poison": 2, "Ground": 1, "Flying": 0, "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1, "Dragon": 1,
                   "Dark": 1, "Steel": 2, "Fairy": 1},
        "Flying": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 2, "Electric": 0.5, "Ice": 1, "Fighting": 2,
                   "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 2, "Rock": 0.5, "Ghost": 1, "Dragon": 1,
                   "Dark": 1, "Steel": 0.5, "Fairy": 1},
        "Psychic": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 2, "Poison": 2,
                    "Ground": 1, "Flying": 1, "Psychic": 0.5, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 0,
                    "Steel": 0.5, "Fairy": 1},
        "Bug": {"Normal": 1, "Fire": 0.5, "Water": 1, "Grass": 2, "Electric": 1, "Ice": 1, "Fighting": 0.5,
                "Poison": 0.5, "Ground": 1, "Flying": 0.5, "Psychic": 2, "Bug": 1, "Rock": 1, "Ghost": 0.5, "Dragon": 1,
                "Dark": 2, "Steel": 0.5, "Fairy": 0.5},
        "Rock": {"Normal": 1, "Fire": 2, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 2, "Fighting": 0.5, "Poison": 1,
                 "Ground": 0.5, "Flying": 2, "Psychic": 1, "Bug": 2, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1,
                 "Steel": 0.5, "Fairy": 1},
        "Ghost": {"Normal": 0, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 1,
                  "Ground": 1, "Flying": 1, "Psychic": 2, "Bug": 1, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 0.5,
                  "Steel": 1, "Fairy": 1},
        "Dragon": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 1, "Poison": 1,
                   "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 1,
                   "Steel": 0.5, "Fairy": 0},
        "Dark": {"Normal": 1, "Fire": 1, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 0.5, "Poison": 1,
                 "Ground": 1, "Flying": 1, "Psychic": 2, "Bug": 1, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 0.5,
                 "Steel": 1, "Fairy": 0.5},
        "Steel": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Grass": 1, "Electric": 0.5, "Ice": 2, "Fighting": 1,
                  "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 1,
                  "Dark": 1, "Steel": 0.5, "Fairy": 2},
        "Fairy": {"Normal": 1, "Fire": 0.5, "Water": 1, "Grass": 1, "Electric": 1, "Ice": 1, "Fighting": 2, "Poison": 1,
                  "Ground": 0.5, "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 2,
                  "Steel": 0.5, "Fairy": 1}
    }
    STAGES = {-6: 0.35, -5: 0.28, -4: 0.33, -3: 0.4, -2: 0.5, -1: 0.66,
              0: 1, 1: 1.5, 2: 2, 3: 2.5, 4: 3, 5: 3.5, 6: 4}

    inflict_status = {'burn': 'Burn', 'freez': 'Freeze', 'paralyz': 'Paralyze', 'flinch': 'Flinch',
                      'poisoni': 'Poison', 'confus': 'Confuse'}
    boolean_vals = {'increased critical': 'High Crit', 'one-hit': 'Instakill', 'wild': 'Useless',
                    'recoil': 'Recoil', 'crash': 'Crash', ' following turn': 'Delayed',
                    'whatsoever': 'Useless'}
    stats = ['Attack', 'Defense', 'Special', 'Speed', 'accuracy', 'evasion']

    def __init__(self, stats):
        self.name = stats[1]
        self.type = stats[2]
        self.cat = stats[3]
        self.pp = int(stats[4])
        self.pow = int(stats[5])
        self.acc = float(stats[6])
        self.desc = stats[7].replace(';', '.')
        self.effects = {}
        self.generate_effects()

    def __str__(self):
        return f'{self.name}, a {self.type} {self.cat} move with {self.pow} POW. \nEffects: {str(self.effects)}'

    def generate_effects(self):
        if 'no secondary effect' not in self.desc:
            sentences = self.desc.split('.')
            for sent in sentences:
                for phrase, effect in Move.inflict_status.items():
                    if phrase in sent:
                        if effect not in self.effects:
                            self.effects[effect] = {}
                        if '%' in sent and 'chance' not in self.effects[effect]:
                            self.effects[effect]['chance'] = float(
                                sent[(sent.index('%') - 3):sent.index('%')].strip()) / 100
                        if 'cannot paralyze' in sent:
                            self.effects['Paralyze']['immune'] = sent[
                                                                 sent.index('cannot paralyze') + 16:sent.index('-type')]

                for phrase, effect in Move.boolean_vals.items():
                    if phrase in sent and effect not in self.effects:
                        self.effects[effect] = {}

                if 'multi-' in sent or 'Multihit' in self.effects:
                    if 'Multihit' not in self.effects:
                        self.effects['Multihit'] = {}
                    if 'twice' in sent:
                        self.effects['Multihit']['times'] = 'twice'
                    elif '2-5' in sent:
                        self.effects['Multihit']['times'] = 'multiple'

                if 'increases' in sent or 'decreases' in sent or 'lower' in sent or 'raise' in sent:
                    if 'StatChange' not in self.effects:
                        self.effects['StatChange'] = {'change': 1, 'chance': 1}
                    if 'target' in sent or 'opponent' in sent:
                        self.effects['StatChange']['target'] = 'opponent'
                    if 'user' in sent:
                        self.effects['StatChange']['target'] = 'user'
                    if 'two' in sent:
                        self.effects['StatChange']['change'] = 2
                    if 'decreases' in sent or 'lowering' in sent:
                        self.effects['StatChange']['change'] = abs(self.effects['StatChange']['change']) * -1
                    if 'lowering' in sent:
                        self.effects['StatChange']['chance'] = 0.33
                    for stat in Move.stats:
                        if stat in sent:
                            self.effects['StatChange']['stat'] = stat.lower()

                if '2-5 turns' in sent and 'Multihit' not in self.effects:
                    if 'DOT' not in self.effects:
                        self.effects['DOT'] = {}

                if 'poisons' in sent and 'Poison' not in self.effects:
                    self.effects['Poison'] = {'chance': 1}

                if 'fatigue' in sent and 'Confuse' in self.effects:
                    del self.effects['Confuse']
                    self.effects['Fatigues'] = {}

                if 'user to faint' in sent and self.pow > 0:
                    if 'SelfDestruct' not in self.effects:
                        self.effects['SelfDestruct'] = {}

                if 'sleep' in sent and 'only' not in sent:
                    if 'Sleep' not in self.effects:
                        self.effects['Sleep'] = {}
                    if 'target' in sent:
                        self.effects['Sleep']['target'] = 'opponent'
                    else:
                        self.effects['Sleep']['target'] = 'self'

                if 'restore' in sent and 'once' not in sent:
                    if 'Heal' not in self.effects:
                        self.effects['Heal'] = {}
                    if 'target' in sent:
                        self.effects['Heal']['type'] = 'lifesteal'
                    elif self.effects['Heal'] == {}:
                        self.effects['Heal']['type'] = 'selfheal'

    def calc_damage(self, attacker, defender):

        hit_check = self.acc * attacker.accuracy / defender.evasion
        if random.random() > hit_check:
            print('It missed!')
            if 'Crash' in self.effects:
                print(f'{attacker.name} took 1 HP of crash damage!')
                attacker.health -= 1
            return 0

        # Checks category
        if self.cat == 'Physical':
            a = attacker.attack
            d = defender.defense
        elif self.cat == 'Special':
            a = attacker.spattack
            d = defender.spdefense
        else:
            self.check_status(attacker, defender)
            return 0

        # Checks critical
        crit_check = random.randint(0, 255)
        crit = 1
        if 'High Crit' in self.effects:
            crit_check = int(crit_check / 8)
        if crit_check < int(attacker.speed / 2):
            crit = 2

        damage = (((2 * attacker.lv * crit / 5 + 2) * self.pow * a / d) / 50 + 2)
        if self.type in attacker.types:
            damage *= 1.5
            # print('STAB!')
        for poke_type in defender.types:
            change = Move.TYPE_ADVANTAGE[self.type][poke_type]
            damage *= change
            # print(f'{self.type} type move attacking {poke_type} type Pokemon. Modifier: {change}')

        damage *= random.randint(217, 255) / 255
        damage = int(damage)

        if crit > 1:
            print('Critical!')

        print(f'{damage} damage dealt!')
        self.check_status(attacker, defender)

        return int(damage)

    def check_status(self, attacker, defender):
        if 'Burn' in self.effects and 'chance' in self.effects['Burn']:
            if 'Freeze' in defender.effects:
                del defender.effects['Freeze']
                print(f'{defender.name} thawed out!')
            if random.random() < self.effects['Burn']['chance']:
                if 'Fire' in defender.types:
                    print(f'{defender.name} got burned, but they are immune!')
                elif 'Burn' in defender.start_status:
                    print(f'{defender.name} got burned, but they are already burnt!')
                else:
                    print(f'{defender.name} got burned!')
                    defender.start_status['Burn'] = {}
                    defender.end_status['Burn'] = {}
        if 'Poison' in self.effects and 'chance' in self.effects['Poison']:
            if random.random() < self.effects['Poison']['chance']:
                if 'Poison' in defender.start_status:
                    print(f'{defender.name} got poisoned, but they are already poisoned!')
                else:
                    print(f'{defender.name} got poisoned!')
                    defender.end_status['Poison'] = {}
        if 'Freeze' in self.effects and 'chance' in self.effects['Freeze']:
            if random.random() < self.effects['Freeze']['chance']:
                if 'Freeze' in defender.start_status:
                    print(f'{defender.name} got frozen, but they are already frozen!')
                else:
                    print(f'{defender.name} got frozen!')
                    defender.start_status['Freeze'] = {}
        if 'Paralyze' in self.effects:
            if 'immune' not in self.effects['Paralyze'] or self.effects['Paralyze']['immune'] not in defender.types:
                if 'chance' not in self.effects['Paralyze'] or random.random() < self.effects['Paralyze']['chance']:
                    if 'Paralyze' in defender.start_status:
                        print(f'{defender.name} got paralyzed, but they are already paralyzed!')
                    else:
                        print(f'{defender.name} got paralyzed!')
                        defender.start_status['Paralyze'] = {}
                        defender.end_status['Paralyze'] = {}
            else:
                print(f'{defender.name} got paralyzed, but they are immune!')
        if 'Flinch' in self.effects and 'chance' in self.effects['Flinch']:
            if random.random() < self.effects['Flinch']['chance']:
                print(f'{defender.name} flinched!')
                defender.start_status['Flinch'] = {}
        if 'Confuse' in self.effects:
            if 'chance' not in self.effects['Confuse'] or random.random() < self.effects['Confuse']['chance']:
                if 'Confuse' in defender.start_status:
                    print(f'{defender.name} got confused, but they are already confused!')
                else:
                    print(f'{defender.name} got confused!')
                    defender.start_status['Confuse'] = {}

    def activate_move(self, attacker, defender):

        print(f'{attacker.name} uses {self.name} against {defender.name}. ')

        if 'Useless' in self.effects:
            print('It has no effect!')

        elif 'Delayed' in self.effects and 'Delayed' not in attacker.start_status:
            print(f'{attacker.name} is charging up!')
            attacker.start_status['Delayed'] = self.name

        elif 'Instakill' in self.effects:
            hit_check = self.acc * attacker.accuracy / defender.evasion
            if random.random() > hit_check or attacker.speed < defender.speed:
                print('It missed!')
            else:
                print(f'It hit! {defender.name} immediately fainted!')
                defender.health = 0

        elif 'Multihit' in self.effects:
            if self.effects['Multihit']['times'] == 'multiple':
                choice = [2, 3, 4, 5]
                times = random.choices(choice, weights=[3, 3, 1, 1], k=1)[0]
                print(f'It hits {times} times!')
                for i in range(times):
                    dmg = self.calc_damage(attacker, defender)
                    defender.health -= dmg

            elif self.effects['Multihit']['times'] == 'twice':
                print('It hits 2 times!')
                dmg = self.calc_damage(attacker, defender)
                defender.health -= dmg
                dmg = self.calc_damage(attacker, defender)
                defender.health -= dmg
        else:
            dmg = self.calc_damage(attacker, defender)
            defender.health -= dmg
            if 'Recoil' in self.effects:
                recoil = int(dmg / 4)
                print(f'{attacker.name} took {recoil} damage as recoil!')
                attacker.health -= recoil
            elif 'SelfDestruct' in self.effects:
                print(f'{attacker.name} fainted after the attack!')
                attacker.health = 0
