# Seed Words for World Building

**CRITICAL:** Do not "choose" a word from the list below. The human brain naturally picks words that feel "safe" or "relevant." The Simulation Protocol works best when the seed feels **irrelevant** or **uncomfortable**.

## The Generator Tool

Use the provided script to get a guaranteed random seed:

```bash
python3 generate_seed.py
```

Or use this one-liner if you don't want to save the file:

```bash
python3 -c "import random; words=['crystalline','molten','hollow','magnetic','buoyant','viscous','transparent','porous','elastic','brittle','instantaneous','glacial','cyclical','reversible','ephemeral','eternal','synchronized','staggered','encrypted','verified','anonymous','broadcast','whispered','forgotten','indelible','autonomous','choreographed','unanimous','anarchic','delegated','centralized','emergent','deterministic','abundant','rationed','communal','hoarded','renewable','depleting','borrowed','gifted','solitary','tribal','mirrored','competitive','symbiotic','parasitic','apprenticed','ancestral','mycelial','viral','metamorphic','dormant','migratory','territorial','pollinating','decomposing','blindfolded','echoing','fragrant','numb','synesthetic','magnified','inverted']; print(random.choice(words))"
```

---

## Seed Reference Library (For Context Only)

**Do not browse this list to pick a seed.** Use the generator above. Consult this list only *after* generation if you need help understanding the word's implication.

### Physical Properties
| Word | Implication |
|------|-------------|
| crystalline | Structure is rigid, faceted, refractive |
| molten | Everything flows, nothing holds shape |
| hollow | Interiors are empty, surfaces deceive |
| magnetic | Attraction/repulsion governs movement |
| buoyant | Default state is rising, weight = commitment |
| viscous | Movement is slow, resistance everywhere |
| transparent | Nothing can be hidden |
| porous | All barriers leak, gradients equalize |
| elastic | Everything bounces back, no permanent change |
| brittle | Things shatter, no graceful degradation |

### Temporal
| Word | Implication |
|------|-------------|
| instantaneous | No delay between cause and effect |
| glacial | Everything happens extremely slowly |
| cyclical | All patterns repeat, no linear progress |
| reversible | Any action can be undone |
| ephemeral | Nothing lasts, everything decays fast |
| eternal | Nothing changes, persistence is default |
| synchronized | Everything happens together or not at all |
| staggered | Everything happens in sequence, no parallelism |

### Information/Trust
| Word | Implication |
|------|-------------|
| encrypted | All information requires keys to access |
| verified | Nothing is trusted without proof |
| anonymous | Identity cannot be established |
| broadcast | All communication reaches everyone |
| whispered | Information travels only to adjacent nodes |
| forgotten | Memory degrades, nothing is retained |
| indelible | Everything is recorded permanently |

### Agency/Control
| Word | Implication |
|------|-------------|
| autonomous | Every entity acts independently |
| choreographed | All action follows predetermined scripts |
| unanimous | Decisions require complete agreement |
| anarchic | No central authority, emergent order only |
| delegated | Power flows downward through hierarchies |
| centralized | One entity controls everything |
| emergent | Order arises from simple rules, not design |
| deterministic | All outcomes are predictable from inputs |

### Resource/Scarcity
| Word | Implication |
|------|-------------|
| abundant | Resources are unlimited |
| rationed | Resources are strictly allocated |
| communal | All resources are shared |
| hoarded | Accumulation is the dominant strategy |
| renewable | Resources regenerate when used |
| depleting | Every use reduces total supply |
| borrowed | All possession is temporary loan |
| gifted | Transfer only happens through giving |

### Social/Relational
| Word | Implication |
|------|-------------|
| solitary | Entities cannot interact directly |
| tribal | Strong in-group, hostile to out-group |
| mirrored | All actions reflect back on the actor |
| competitive | Zero-sum, only winners survive |
| symbiotic | Entities must cooperate to survive |
| parasitic | Some entities extract from others |
| apprenticed | Knowledge only transfers through mentorship |
| ancestral | The past governs the present |

### Biological
| Word | Implication |
|------|-------------|
| mycelial | Underground networks connect everything |
| viral | Ideas/behaviors spread through contact |
| metamorphic | Entities transform through life stages |
| dormant | Systems can sleep and reawaken |
| migratory | Movement is seasonal/cyclical |
| territorial | Space must be defended |
| pollinating | Cross-fertilization creates new forms |
| decomposing | Decay is the source of renewal |

### Sensory/Perception
| Word | Implication |
|------|-------------|
| blindfolded | Visual information is unavailable |
| echoing | Information returns transformed |
| fragrant | Presence is detected before arrival |
| numb | Sensation is diminished or absent |
| synesthetic | Senses are crossed/combined |
| magnified | Small things appear large |
| inverted | Perception is opposite to reality |

---

## Combining Seeds (Advanced)

Only combine seeds if the generator gives you two, or if you run it twice.

```
[SEED 1] + [SEED 2]
```