
class Move:

    inflict_status = {'burn': 'Burn', 'freez': 'Freeze', 'paralyz': 'Paralyze', 'flinch': 'Flinch',
                'poisoni': 'Poison', 'confus': 'Confuse'}
    boolean_vals = {'increased critical': 'High Crit', 'one-hit': 'Instakill', 'wild': 'Useless',
                    'recoil': 'Recoil', 'crash': 'Crash', ' following turn': 'Delayed',
                    'whatsoever': 'Useless'}
    stats = ['Attack', 'Defense', 'Special', 'Speed', 'accuracy', 'evasion']

    def __init__(self, stats):
        self.name = stats[0]
        self.type = stats[1]
        self.cat = stats[2]
        self.pp = int(stats[3])
        self.pow = int(stats[4])
        self.acc = float(stats[5])
        self.desc = stats[6].replace(';', '.')
        self.effects = {}
        self.generate_effects()

    def __str__(self):
        return f'{self.name}, a {self.type} {self.cat} move with {self.pow} POW'

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
                            self.effects['Paralyze']['immune'] = sent[sent.index('cannot paralyze') + 16:sent.index('-type')]

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












