---
doc_id: "mta-wiki:14652"
title: "IsPlayerNameRandomized"
source_title: "IsPlayerNameRandomized"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerNameRandomized"
revision_id: 82626
language: "en"
categories: ["Useful_Functions"]
---

# IsPlayerNameRandomized

Checks whether the given player name looks like an automatically-generated random nickname.

## Syntax

```
bool isPlayerNameRandomized ( string name )
```

### Required Arguments

- **name**: The player name to check.

### Returns

Returns **true** if the given name is an auto-generated random nickname, or **false** otherwise.

## Code

Click to collapse [-]
Shared

```
local firstName, secondName = {
    "Aback",      "Abaft",      "Abandoned",  "Abashed",    "Aberrant",   "Abhorrent",  "Abiding",    "Abject",     "Ablaze",     "Able",       "Abnormal",
    "Aboard",     "Aboriginal", "Abortive",   "Abounding",  "Abrasive",   "Abrupt",     "Absent",     "Absorbed",   "Absorbing",  "Abstracted", "Absurd",
    "Abundant",   "Abusive",    "Acceptable", "Accessible", "Accidental", "Accurate",   "Acid",       "Acidic",     "Acoustic",   "Acrid",      "Actually",
    "Adhoc",      "Adamant",    "Adaptable",  "Addicted",   "Adhesive",   "Adjoining",  "Adorable",   "Afraid",     "Aggressive", "Agonizing",  "Agreeable",
    "Ahead",      "Ajar",       "Alcoholic",  "Alert",      "Alike",      "Alive",      "Alleged",    "Alluring",   "Aloof",      "Amazing",    "Ambiguous",
    "Ambitious",  "Amuck",      "Amused",     "Amusing",    "Ancient",    "Angry",      "Animated",   "Annoyed",    "Annoying",   "Anxious",    "Apathetic",
    "Aquatic",    "Aromatic",   "Arrogant",   "Ashamed",    "Aspiring",   "Assorted",   "Attractive", "Auspicious", "Automatic",  "Available",  "Average",
    "Awake",      "Aware",      "Awesome",    "Awful",      "Axiomatic",  "Bad",        "Barbarous",  "Bashful",    "Bawdy",      "Beautiful",  "Befitting",
    "Beneficial", "Bent",       "Berserk",    "Best",       "Better",     "Bewildered", "Big",        "Billowy",    "Bite-sized", "Bitter",     "Bizarre",
    "Black",      "Bloody",     "Blue",       "Blue-eyed",  "Blushing",   "Boiling",    "Boorish",    "Bored",      "Boring",     "Bouncy",     "Boundless",
    "Brainy",     "Brash",      "Brave",      "Brawny",     "Breakable",  "Breezy",     "Brief",      "Bright",     "Broad",      "Broken",     "Brown",
    "Bumpy",      "Burly",      "Bustling",   "Busy",       "Cagey",      "Callous",    "Calm",       "Capable",    "Capricious", "Careful",    "Careless",
    "Caring",     "Cautious",   "Ceaseless",  "Certain",    "Changeable", "Charming",   "Cheap",      "Cheerful",   "Chemical",   "Chief",      "Childlike",
    "Chilly",     "Chivalrous", "Chubby",     "Chunky",     "Clammy",     "Classy",     "Clean",      "Clear",      "Clever",     "Cloistered", "Cloudy",
    "Closed",     "Clumsy",     "Cluttered",  "Coherent",   "Cold",       "Colorful",   "Colossal",   "Combative",  "Common",     "Complete",   "Complex",
    "Concerned",  "Condemned",  "Confused",   "Conscious",  "Cooing",     "Cool",       "Courageous", "Cowardly",   "Crabby",     "Craven",     "Crazy",
    "Creepy",     "Crooked",    "Crowded",    "Cruel",      "Cuddly",     "Cultured",   "Cumbersome", "Curious",    "Curly",      "Curved",     "Curvy",
    "Cut",        "Cute",       "Cynical",    "Daffy",      "Daily",      "Damaged",    "Damaging",   "Damp",       "Dangerous",  "Dapper",     "Dark",
    "Dashing",    "Dazzling",   "Dead",       "Deadpan",    "Deafening",  "Dear",       "Debonair",   "Decisive",   "Decorous",   "Deep",       "Deeply",
    "Defeated",   "Defective",  "Defiant",    "Delicate",   "Delicious",  "Delightful", "Demonic",    "Delirious",  "Dependent",  "Depressed",  "Deranged",
    "Deserted",   "Detailed",   "Determined", "Devilish",   "Didactic",   "Different",  "Difficult",  "Diligent",   "Direful",    "Dirty",      "Disastrous",
    "Discreet",   "Disgusted",  "Disgusting", "Distinct",   "Disturbed",  "Divergent",  "Dizzy",      "Doubtful",   "Drab",       "Draconian",  "Dramatic",
    "Dreary",     "Drunk",      "Dry",        "Dull",       "Dusty",      "Dynamic",    "Eager",      "Early",      "Earthy",     "Easy",       "Eatable",
    "Economic",   "Educated",   "Efficient",  "Eight",      "Elastic",    "Elated",     "Elderly",    "Electric",   "Elegant",    "Elfin",      "Elite",
    "Eminent",    "Empty",      "Enchanted",  "Enchanting", "Endurable",  "Energetic",  "Enormous",   "Envious",    "Equable",    "Equal",      "Erect",
    "Erratic",    "Ethereal",   "Evanescent", "Evasive",    "Even",       "Excellent",  "Excited",    "Exciting",   "Exclusive",  "Exotic",     "Expensive",
    "Exuberant",  "Exultant",   "Fabulous",   "Faded",      "Faint",      "Fair",       "Faithful",   "Fallacious", "False",      "Familiar",   "Famous",
    "Fanatical",  "Fancy",      "Fantastic",  "Far",        "Far-flung",  "Fascinated", "Fast",       "Fat",        "Faulty",     "Fearful",    "Fearless",
    "Feeble",     "Feigned",    "Female",     "Fertile",    "Festive",    "Few",        "Fierce",     "Filthy",     "Fine",       "Finicky",    "First",
    "Five",       "Fixed",      "Flagrant",   "Flaky",      "Flashy",     "Flat",       "Flawless",   "Flimsy",     "Flippant",   "Flowery",    "Fluffy",
    "Fluttering", "Foamy",      "Foolish",    "Foregoing",  "Forgetful",  "Fortunate",  "Four",       "Frail",      "Fragile",    "Frantic",    "Free",
    "Freezing",   "Frequent",   "Fresh",      "Fretful",    "Friendly",   "Frightened", "Full",       "Fumbling",   "Functional", "Funny",      "Furry",
    "Furtive",    "Future",     "Futuristic", "Fuzzy",      "Gabby",      "Gainful",    "Gamy",       "Gaping",     "Garrulous",  "Gaudy",      "General",
    "Gentle",     "Giant",      "Giddy",      "Gifted",     "Gigantic",   "Glamorous",  "Gleaming",   "Glib",       "Glistening", "Glorious",   "Glossy",
    "Godly",      "Good",       "Goofy",      "Gorgeous",   "Graceful",   "Grandiose",  "Grateful",   "Gratis",     "Gray",       "Greasy",     "Great",
    "Greedy",     "Green",      "Grey",       "Grieving",   "Groovy",     "Grotesque",  "Grouchy",    "Grubby",     "Gruesome",   "Grumpy",     "Guarded",
    "Guiltless",  "Gullible",   "Gusty",      "Guttural",   "Habitual",   "Half",       "Hallowed",   "Halting",    "Handsome",   "Handsomely", "Handy",
    "Hanging",    "Hapless",    "Happy",      "Hard",       "Harmonious", "Harsh",      "Hateful",    "Heady",      "Healthy",    "Heavenly",   "Heavy",
    "Hellish",    "Helpful",    "Helpless",   "Hesitant",   "Hideous",    "High",       "Hilarious",  "Hissing",    "Historical", "Holistic",   "Hollow",
    "Homeless",   "Homely",     "Honorable",  "Horrible",   "Hospitable", "Hot",        "Huge",       "Hulking",    "Humdrum",    "Humorous",   "Hungry",
    "Hurried",    "Hurt",       "Hushed",     "Husky",      "Hypnotic",   "Hysterical", "Icky",       "Icy",        "Idiotic",    "Ignorant",   "Ill",
    "Illegal",    "Ill-fated",  "Imaginary",  "Immense",    "Imminent",   "Impartial",  "Imperfect",  "Impolite",   "Important",  "Imported",   "Impossible",
    "Incredible", "Infamous",   "Innate",     "Innocent",   "Insidious",  "Internal",   "Invincible", "Irate",      "Irritating", "Itchy",      "Jaded",
    "Jagged",     "Jazzy",      "Jealous",    "Jittery",    "Jobless",    "Jolly",      "Joyous",     "Judicious",  "Juicy",      "Jumbled",    "Jumpy",
    "Juvenile",   "Kaput",      "Keen",       "Kind",       "Kindly",     "Knotty",     "Knowing",    "Known",      "Labored",    "Lacking",    "Lame",
    "Lamentable", "Languid",    "Large",      "Last",       "Late",       "Laughable",  "Lavish",     "Lazy",       "Lean",       "Learned",    "Left",
    "Legal",      "Lethal",     "Level",      "Lewd",       "Light",      "Like",       "Likeable",   "Limping",    "Literate",   "Little",     "Lively",
    "Living",     "Lonely",     "Long",       "Longing",    "Long-term",  "Loose",      "Lopsided",   "Loud",       "Loutish",    "Lovely",     "Loving",
    "Low",        "Lowly",      "Lucky",      "Ludicrous",  "Lumpy",      "Lush",       "Luxuriant",  "Lying",      "Lyrical",    "Macabre",    "Macho",
    "Maddening",  "Madly",      "Magenta",    "Magical",    "Majestic",   "Makeshift",  "Male",       "Malicious",  "Mammoth",    "Maniacal",   "Many",
    "Marked",     "Massive",    "Married",    "Marvelous",  "Material",   "Mature",     "Mean",       "Measly",     "Meaty",      "Medical",    "Meek",
    "Mellow",     "Melodic",    "Melted",     "Merciful",   "Mere",       "Messy",      "Mighty",     "Military",   "Milky",      "Mindless",   "Miniature",
    "Minor",      "Miscreant",  "Misty",      "Mixed",      "Moaning",    "Modern",     "Moldy",      "Momentous",  "Motionless", "Muddled",    "Mundane",
    "Murky",      "Mushy",      "Mute",       "Mysterious", "Naive",      "Nappy",      "Narrow",     "Nasty",      "Natural",    "Naughty",    "Nauseating",
    "Near",       "Neat",       "Nebulous",   "Necessary",  "Needless",   "Needy",      "Neighborly", "Nervous",    "New",        "Next",       "Nice",
    "Nifty",      "Nimble",     "Nine",       "Nippy",      "Noiseless",  "Noisy",      "Nonchalant", "Nonstop",    "Normal",     "Nostalgic",  "Nosy",
    "Noxious",    "Null",       "Numberless", "Numerous",   "Nutritious", "Nutty",      "Oafish",     "Obedient",   "Obeisant",   "Obese",      "Obnoxious",
    "Obscene",    "Obsequious", "Observant",  "Obsolete",   "Obtainable", "Oceanic",    "Odd",        "Offbeat",    "Old",        "Omniscient", "One",
    "Onerous",    "Open",       "Opposite",   "Optimal",    "Orange",     "Ordinary",   "Organic",    "Ossified",   "Outgoing",   "Outrageous", "Oval",
    "Overjoyed",  "Overrated",  "Overt",      "Painful",    "Pale",       "Paltry",     "Panicky",    "Panoramic",  "Parallel",   "Parched",    "Past",
    "Pastoral",   "Pathetic",   "Peaceful",   "Penitent",   "Perfect",    "Periodic",   "Perpetual",  "Petite",     "Phobic",     "Physical",   "Picayune",
    "Pink",       "Piquant",    "Placid",     "Plain",      "Plant",      "Plastic",    "Plausible",  "Pleasant",   "Plucky",     "Pointless",  "Poised",
    "Polite",     "Political",  "Poor",       "Possessive", "Possible",   "Powerful",   "Precious",   "Premium",    "Present",    "Pretty",     "Previous",
    "Pricey",     "Prickly",    "Private",    "Probable",   "Productive", "Profuse",    "Protective", "Proud",      "Psychotic",  "Public",     "Puffy",
    "Pumped",     "Puny",       "Purple",     "Purring",    "Pushy",      "Puzzled",    "Puzzling",   "Quack",      "Quaint",     "Quick",      "Quickest",
    "Quiet",      "Quirky",     "Quixotic",   "Quizzical",  "Rabid",      "Racial",     "Ragged",     "Rainy",      "Rampant",    "Rapid",      "Rare",
    "Raspy",      "Ratty",      "Ready",      "Real",       "Rebel",      "Receptive",  "Recondite",  "Red",        "Redundant",  "Reflective", "Regular",
    "Relieved",   "Remarkable", "Repulsive",  "Resolute",   "Resonant",   "Rhetorical", "Rich",       "Right",      "Righteous",  "Rightful",   "Rigid",
    "Ripe",       "Ritzy",      "Roasted",    "Robust",     "Romantic",   "Roomy",      "Rotten",     "Rough",      "Round",      "Royal",      "Ruddy",
    "Rude",       "Rural",      "Rustic",     "Ruthless",   "Sable",      "Sad",        "Safe",       "Salty",      "Same",       "Sassy",      "Satisfying",
    "Savory",     "Scandalous", "Scarce",     "Scared",     "Scary",      "Scattered",  "Scientific", "Scrawny",    "Screeching", "Second",     "Secret",
    "Secretive",  "Sedate",     "Seemly",     "Selective",  "Selfish",    "Separate",   "Serious",    "Shaggy",     "Shaky",      "Shallow",    "Sharp",
    "Shiny",      "Shivering",  "Shocking",   "Short",      "Shrill",     "Shut",       "Shy",        "Sick",       "Silent",     "Silky",      "Silly",
    "Simple",     "Simplistic", "Sincere",    "Six",        "Skillful",   "Skinny",     "Sleepy",     "Slim",       "Slimy",      "Slippery",   "Sloppy",
    "Slow",       "Small",      "Smart",      "Smelly",     "Smiling",    "Smoggy",     "Smooth",     "Sneaky",     "Snobbish",   "Snotty",     "Soft",
    "Soggy",      "Solid",      "Somber",     "Sordid",     "Sore",       "Sour",       "Sparkling",  "Special",    "Spicy",      "Spiffy",     "Spiky",
    "Spiritual",  "Spiteful",   "Splendid",   "Spooky",     "Spotless",   "Spotted",    "Spotty",     "Spurious",   "Squalid",    "Square",     "Squealing",
    "Squeamish",  "Staking",    "Stale",      "Standing",   "Statuesque", "Steadfast",  "Steady",     "Stealthy",   "Steep",      "Sticky",     "Stiff",
    "Stingy",     "Stormy",     "Straight",   "Strange",    "Striped",    "Strong",     "Stupendous", "Stupid",     "Sturdy",     "Subdued",    "Subsequent",
    "Successful", "Succinct",   "Sudden",     "Sulky",      "Super",      "Superb",     "Supreme",    "Swanky",     "Sweet",      "Sweltering", "Swift",
    "Synonymous", "Taboo",      "Tacit",      "Tacky",      "Talented",   "Tall",       "Tame",       "Tan",        "Tangible",   "Tangy",      "Tart",
    "Tasteful",   "Tasteless",  "Tasty",      "Tawdry",     "Tearful",    "Tedious",    "Teeny",      "Teeny-tiny", "Telling",    "Temporary",  "Ten",
    "Tender",     "Tense",      "Tenuous",    "Terrible",   "Terrific",   "Tested",     "Testy",      "Thankful",   "Thick",      "Thin",       "Thinkable",
    "Third",      "Thirsty",    "Thoughtful", "Three",      "Thundering", "Tidy",       "Tight",      "Tiny",       "Tired",      "Tiresome",   "Toothsome",
    "Torpid",     "Tough",      "Towering",   "Tranquil",   "Trashy",     "Tremendous", "Tricky",     "Trite",      "Troubled",   "Truculent",  "True",
    "Truthful",   "Two",        "Typical",    "Ubiquitous", "Ugliest",    "Ugly",       "Ultra",      "Unable",     "Unadvised",  "Unarmed",    "Unbecoming",
    "Unbiased",   "Uncovered",  "Understood", "Unequal",    "Unequaled",  "Uneven",     "Unhealthy",  "Unique",     "Unkempt",    "Unknown",    "Unnatural",
    "Unruly",     "Unsightly",  "Unsuitable", "Untidy",     "Unused",     "Unusual",    "Unwieldy",   "Unwritten",  "Upbeat",     "Uppity",     "Upset",
    "Uptight",    "Used",       "Useful",     "Useless",    "Utopian",    "Utter",      "Uttermost",  "Vacuous",    "Vagabond",   "Vague",      "Valuable",
    "Various",    "Vast",       "Vengeful",   "Venomous",   "Verdant",    "Versed",     "Victorious", "Vigorous",   "Violent",    "Violet",     "Vivacious",
    "Voiceless",  "Volatile",   "Voracious",  "Vulgar",     "Wacky",      "Waggish",    "Waiting",    "Wakeful",    "Wandering",  "Wanting",    "Warlike",
    "Warm",       "Wary",       "Wasteful",   "Watery",     "Weak",       "Wealthy",    "Weary",      "Well-made",  "Well-off",   "Well-to-do", "Wet",
    "Whimsical",  "Whispering", "White",      "Whole",      "Wholesale",  "Wicked",     "Wide",       "Wide-eyed",  "Wiggly",     "Wild",       "Willing",
    "Windy",      "Wiry",       "Wise",       "Wistful",    "Witty",      "Woebegone",  "Womanly",    "Wonderful",  "Wooden",     "Woozy",      "Workable",
    "Worried",    "Worthless",  "Wrathful",   "Wretched",   "Wrong",      "Wry",
}, {
    "Aardvark",   "Buffalo",    "Alligator",  "Ant",        "Anteater",   "Antelope",   "Ape",        "Armadillo",  "Donkey",      "Baboon",     "Badger",
    "Barracuda",  "Bat",        "Bear",       "Beaver",     "Bee",        "Bison",      "Boar",       "Bush",       "Butterfly",   "Camel",      "Calf",
    "Cat",        "Kitten",     "Cattle",     "Chamois",    "Cheetah",    "Chicken",    "Chick",      "Chimpanzee", "Infant",      "Empress",    "Troop",
    "Cobra",      "Cockroach",  "Cormorant",  "Cougar",     "Coyote",     "Crab",       "Crane",      "Crocodile",  "Crow",        "Deer",       "Dog",
    "Dogfish",    "Dolphin",    "Dove",       "Dragonfly",  "Duck",       "Dugong",     "Eagle",      "Eaglet",     "Echidna",     "Eel",        "Eland",
    "Elephant",   "Elk",        "Falcon",     "Ferret",     "Finch",      "Fly",        "Fox",        "Frog",       "Gaur",        "Gazelle",    "Gerbil",
    "Giant",      "Giraffe",    "Gnu",        "Goat",       "Goose",      "Gorilla",    "Guanaco",    "Guinea",     "Guineapig",   "Gull",       "Hamster",
    "Hare",       "Hawk",       "Hedgehog",   "Heron",      "Hornet",     "Horse",      "Human",      "Hyena",      "Iguana",      "Jackal",     "Jaguar",
    "Jellyfish",  "Kangaroo",   "Koala",      "Komodo",     "Kouprey",    "Kudu",       "Lark",       "Lemur",      "Leopard",     "Lion",       "Llama",
    "Loris",      "Louse",      "Lobster",    "Lyrebird",   "Magpie",     "Mallard",    "Manatee",    "Meerkat",    "Mink",        "Mole",       "Monkey",
    "Moose",      "Mouse",      "Mosquito",   "Mule",       "Okapi",      "Oryx",       "Ostrich",    "Otter",      "Owl",         "Ox",         "Oyster",
    "Panther",    "Partridge",  "Peafowl",    "Pelican",    "Penguin",    "Pig",        "Pigeon",     "Pony",       "Porcupine",   "Quelea",     "Rabbit",
    "Bunny",      "Raccoon",    "Rail",       "Ram",        "Rat",        "Raven",      "Reindeer",   "Rhino",      "Salamander",  "Sealion",    "Seal",
    "Seahorse",   "Seastar",    "Shark",      "Sheep",      "Shrew",      "Skunk",      "Snail",      "Snake",      "Spider",      "Squid",      "Squirrel",
    "Stinkbug",   "Swan",       "Tapir",      "Tarsier",    "Tiger",      "Toad",       "Turkey",     "Turtle",     "Vicuna",      "Walrus",     "Wasp",
    "Weasel",     "Whale",      "Wolf",       "Worm",       "Yak",        "Zebra",      "Hat",        "Cap",        "Beret",       "Astrakhan",  "Beanie",
    "Hardhat",    "Pillbox",    "Monkeycap",  "Operahat",   "Bonnet",     "Bowler",     "Coonskin",   "Fedora",     "Derby",       "Montero",    "Cowboyhat",
    "Sombrero",   "Yarmulke",   "Skullcap",   "Tam",        "Sunbonnet",  "Toque",      "Tophat",     "Babushka",   "Balaclava",   "Turban",     "Diadem",
    "Earmuffs",   "Visor",      "Scarf",      "Veil",       "Warbonnet",  "Pithhelmet", "Hood",       "Miter",      "Butter",      "Icecream",   "Cakebatter",
    "Coffee",     "Tea",        "Soda",       "Beer",       "Wine",       "Cappuccino", "Jell-o",     "Nougats",    "Lambchops",   "Steaks",     "Chowder",
    "Fishsoup",   "Spaghetti",  "Sushi",      "Fondue",     "Crabslegs",  "Shrimp",     "Onions",     "Bratwurst",  "Kielbasa",    "Hotdog",     "Hamburger",
    "Herbs",      "Grains",     "Legumes",    "Zampone",    "Casserole",  "Beans",      "Seeds",      "Stew",       "Cereal",      "Polenta",    "Pudding",
    "Pasta",      "Macaroni",   "Ravioli",    "Wafer",      "Crackers",   "Cookies",    "Sandwich",   "Gyro",       "Wrap",        "Omelet",     "Popcorn",
    "Walnuts",    "Nuts",       "Almonds",    "Pizza",      "Mousse",     "Brulee",     "Cakes",      "Pancake",    "Waffles",     "Toast",      "Candy",
    "Pie",        "Senator",    "Governor",   "Councilman", "Detective",  "Sleuth",     "Musician",   "Maestro",    "Conductor",   "Composer",   "Singer",
    "Architect",  "Physician",  "Manager",    "Usher",      "Painter",    "Model",      "Designer",   "Guest",      "Attorney",    "Lawyer",     "Judge",
    "Mayor",      "Therapist",  "Teacher",    "Principal",  "Professor",  "Orator",     "Man",        "Woman",      "Teen",        "Child",      "Mother",
    "Father",     "Sister",     "Brother",    "Uncle",      "Aunt",       "Son",        "Daughter",   "In-laws",    "Boy",         "Girl",       "Nurse",
    "Sibling",    "Settler",    "Pioneer",    "Waiter",     "Hostess",    "Host",       "Cashier",    "Attendant",  "Publisher",   "Witch",      "Warlock",
    "Ghost",      "Knight",     "Prince",     "Princess",   "Maiden",     "Godmother",  "Fairy",      "Petal",      "Sepal",       "Stamen",     "Pineboughs",
    "Bud",        "Branch",     "Blossom",    "Fruit",      "Bloom",      "Tree",       "Maple",      "Elm",        "Oak",         "Palm",       "Baobab",
    "Mangrove",   "Cyprus",     "Pine",       "Dogwood",    "Alder",      "Flowers",    "Rose",       "Tulip",      "Cyclamen",    "Lily",       "Carnations",
    "Wisteria",   "Flytrap",    "Hoe",        "Weeds",      "Plants",     "Canes",      "Palms",      "Apple",      "Lemon",       "Orange",     "Grapefruit",
    "Tangerine",  "Peach",      "Tomato",     "Banana",     "Vegetables", "Artichokes", "Leeks",      "Lettuce",    "Eggplants",   "Zucchini",   "Squash",
    "Pumpkin",    "Cabbage",    "Pepper",     "Onion",      "Garlic",     "Poison",     "Venom",      "Fire",       "Ship",        "Ferryboat",  "Oceanliner",
    "Oars",       "Sails",      "Dinghy",     "Yacht",      "Canoe",      "Catamaran",  "Gondola",    "Boat",       "Battleship",  "Clipper",    "Dhow",
    "Flatboat",   "Houseboat",  "Galleon",    "Frigate",    "Hydrofoil",  "Junk",       "Ketch",      "Yawl",       "Submarine",   "Schooner",   "Scow",
    "Flatbed",    "Suv",        "Van",        "Caboose",    "Train",      "Bullet",     "Metro",      "Subway",     "Cart",        "Taxi",       "Car",
    "Racingcar",  "Buggy",      "Dunebuggy",  "Dragster",   "Motorcycle", "Gokart",     "Limo",       "Stretch",    "Wagon",       "Trolley",    "Tram",
    "Bus",        "Parachute",  "Tractor",    "Trailer",    "Golfkart",   "Jeep",       "Bigrig",     "Bulldozer",  "Dumptruck",   "Towtruck",   "Engine",
    "Fireengine", "Policecar",  "Tank",       "Locomotive", "Ocean",      "Oasis",      "Sea",        "Lake",       "Saltlake",    "Seafoam",    "Waves",
    "Bubbles",    "Current",    "Waterbasin", "Bridge",     "Harbor",     "Pond",       "Wharf",      "Pier",       "Dock",        "Port",       "Shore",
    "Beach",      "Sandbar",    "Coast",      "River",      "Brook",      "Rivulet",    "Puddle",     "Waterfall",  "Cascades",    "Canal",      "Channel",
    "Stream",     "Creek",      "Marsh",      "Bog",        "Swamp",      "Bayou",      "Estuary",    "Whirlpool",  "Eddy",        "Geyser",     "Well",
    "Monsoon",    "Hurricane",  "Typhoon",    "Air",        "Snow",       "Rain",       "Sleet",      "Storm",      "Hail",        "Blizzard",   "Wind",
    "Breeze",     "Gale",       "Whirlwind",  "Maelstrom",  "Duststorm",  "Cloudburst", "Tornado",    "Twister",    "Clouds",      "Fog",        "Peasoup",
    "Floods",     "Flashflood", "Acidrain",   "Tremors",    "Lightning",  "Avalanche",  "Eclipse",    "Alpenglow",  "Tsunami",     "Waterspout", "Smog",
    "Aneroid",    "Barometer",  "Radiosonde", "Station",    "Map",        "Chalice",    "Bijou",      "Candelabra", "Menorah",     "Curio",      "Figurine",
    "Music-box",  "Objetd'art", "Trinket",    "Trims",      "Windchimes", "Birdcage",   "Birdbath",   "Cans",       "Urn",         "Bucket",     "Arrow",
    "Bow",        "Sword",      "Dart",       "Epee",       "Dagger",     "Hatchet",    "Pickax",     "Dolls",      "Broom",       "Mop",        "Pail",
    "Squeegee",   "Caddy",      "Telephone",  "Pipe",       "Paints",     "Brushes",    "Easel",      "Canvas",     "Trunk",       "Hook",       "Gun",
    "Glue",       "Tissue",     "Toilet",     "Kleenex",    "Papertowel", "Ropes",      "Rubber",     "Coil",       "Toys",        "Dogleash",   "Balloon",
    "Vases",      "Planters",   "Pen",        "Pad",        "Typewriter", "Computer",   "Laptop",     "Netbook",    "Stylus",      "Pencil",     "Desk",
    "Backpack",   "Shoerack",   "Notebook",   "Vellum",     "Chalk",      "Badge",      "Saddle",     "Spurs",      "Paper",       "Rollbook",   "Guestbook",
    "Pot",        "Plate",      "Dishes",     "Fork",       "Spoons",     "Knives",     "Knife",      "Samovar",    "Sky",         "Forest",     "Heaven",
    "Hell",       "Earth",      "Sun",        "Star",       "Planet",     "Mercury",    "Venus",      "Mars",       "Jupiter",     "Saturn",     "Uranus",
    "Neptune",    "Ceres",      "Pluto",      "Haumea",     "Makemake",   "Eris",       "Outerspace", "Town",       "Village",     "City",       "Country",
    "Farm",       "Suburb",     "Roads",      "Streets",    "Blocks",     "Zoo",        "Park",       "Museum",     "Cemetery",    "Tunnels",    "Caves",
    "Churches",   "Temples",    "Mall",       "Dresser",    "Armoire",    "Chiffonier", "Credenza",   "Console",    "Bookcase",    "Buffet",     "Armchair",
    "Recliner",   "Easychair",  "Bench",      "Banquette",  "Chair",      "Couch",      "Davenport",  "Sofa",       "Ottoman",     "Deckchair",  "Loveseat",
    "Highseat",   "Divan",      "Inglenook",  "Pew",        "Throne",     "Sectional",  "Stool",      "Pottychair", "Workbench",   "Nighttable", "Bed",
    "Daybed",     "Bassinet",   "Crib",       "Cradle",     "Cot",        "Futon",      "Hammock",    "Tatamimat",  "Waterbed",    "Trundlebed", "Hassock",
    "Hatrack",    "Stepstool",  "Footrest",   "Footstool",  "Tripod",     "Mirror",     "Nightlight", "Torchiere",  "Sunlamp",     "Spotlight",  "Ceilingfan",
    "Cupboard",   "Cardtable",  "Hutch",      "Locker",     "Wetbar",     "Vanity",     "Rack",       "Hopechest",  "Sculpture",   "Painting",   "Eye",
    "Pupil",      "Iris",       "Retina",     "Eyeball",    "Eyelids",    "Eyelashes",  "Eyebrows",   "Lap",        "Waist",       "Belly",      "Tummy",
    "Rearend",    "Crotch",     "Abdomen",    "Beard",      "Mustache",   "Sideburns",  "Fingernail", "Hand",       "Forearm",     "Arm",        "Knuckles",
    "Thumb",      "Wrist",      "Elbow",      "Leg",        "Toes",       "Knee",       "Ankle",      "Shin",       "Thigh",       "Hip",        "Breast",
    "Chest",      "Torso",      "Tongue",     "Lips",       "Gums",       "Mouth",      "Teeth",      "Bones",      "Spine",       "Throat",     "Lungs",
    "Kidneys",    "Intestines", "Colon",      "Spleen",     "Glands",     "Blood",      "Head",       "Skull",      "Brain",       "Muscle",     "Hair",
    "Xylophone",  "Clavier",    "Virginal",   "Lute",       "Drum",       "Frenchhorn", "Piano",      "Violin",     "Cello",       "Guitar",     "Flute",
    "Tuba",       "Harp",       "Mariachi",   "Orchestra",  "Oboe",       "Bassoon",    "Woodwinds",  "Brass",      "Viola",       "Kettledrum", "Peyotedrum",
    "Tambourine", "Tambour",    "Saxophone",  "Marimba",    "Maracas",    "Shofar",     "Cymbals",    "Kazoo",      "Dulcimer",    "Accordion",  "Lyre",
    "Fiddle",     "Banjo",      "Balalaika",  "Sitar",      "Ukulele",    "Zither",     "Bagpipes",   "Piccolo",    "Clarinet",    "Cornet",     "Panpipe",
    "Tuningfork", "Metronome",  "Castanets",  "Woofer",     "Sniper",     "Marksman",   "Cleaner",    "Pyro",       "Attacker",    "Mechanic",   "Janitor",
    "Scrubber",   "Garbageman", "Technician", "Ninja",      "Medic",      "Spy",        "Assassin",   "Gunman",     "Triggerman",  "Butcher",    "Killer",
    "Dodger",     "Booger",     "Engineer",   "Doctor",     "Surgeon",    "Fighter",    "Shooter",    "Gunner",     "Soldier",     "Officer",    "Veteran",
    "Scout",      "Mercenary",  "Commando",   "Cadet",      "Guard",      "Warrior",    "Trooper",    "Gambler",    "Specialist",  "Shaper",     "Finisher",
    "Gladiator",  "Boxer",      "Wrestler",   "Warlord",    "Rival",      "Armory",     "Agent",      "Rebel",      "Brawler",     "Bruiser",    "Bully",
    "Champion",   "Hero",       "Battler",    "Combatant",  "Fencer",     "Swordsman",  "Expert",     "Gangster",   "Gangsta",     "Bandit",     "Hoodlum",
    "Mobster",    "Robber",     "Thief",      "Burglar",    "Pirate",     "Thug",       "Hitman",     "Hitperson",  "Dealer",      "Desperado",  "Criminal",
    "Crook",      "Hijacker",   "Carjacker",  "Villain",    "Convict",    "Fugitive",   "Mug",        "Outlaw",     "Ruffian",     "Cutthroat",  "Devil",
    "Murderer",   "Psycho",     "Punk",       "ASBO",       "Offender",   "Drifter",    "Rioter",     "Goon",       "Roughneck",   "Brute",      "Hacker",
    "Cabbie",     "Wheeler",    "Driver",     "Rider",      "Cyclist",    "Cowboy",     "Operative",  "Carrier",    "Transporter", "Trucker",    "Wheelman",
    "Vampire",    "Parasite",   "Tramp",      "Bum",        "Hobo",       "Hitchhiker", "Deadbeat",   "Acrobat",
}

function isPlayerNameRandomized(name)
    if type(name) ~= "string" then
        return false
    end

    local prefix, num = name:match("^(.-)(%d+)$")
    if not prefix or not num then
        return false
    end

    if not tonumber(num) or tonumber(num) < 0 or tonumber(num) > 100 then
        return false
    end

    for _, first in ipairs(firstName) do
        if prefix:sub(1, #first) == first then
            local rest = prefix:sub(#first + 1)

            for _, second in ipairs(secondName) do
                if rest == second then
                    return true
                end
            end
        end
    end

    return false
end
```

## Example

The example shows how to use function.

Click to collapse [-]
Server

```
addEventHandler("onPlayerConnect", root,
    function(playerNick)
        if isPlayerNameRandomized(playerNick) then
            cancelEvent(true, "Newbie players are not allowed!")
        end
    end
)
```

Author: [omar-o22](https://wiki.multitheftauto.com/wiki/User:O22)
  

Idea from: [Issue#2103](https://github.com/multitheftauto/mtasa-blue/issues/2103)

## See Also

### Table functions

- [addTableChangeHandler](mta://scripting/shared/functions/addtablechangehandler.md) » This function monitors the changes of a table.

- [pairsByKeys](mta://scripting/shared/functions/pairsbykeys.md) » This function sort pairs table.

- [rangeToTable](mta://scripting/shared/functions/rangetotable.md) » This function converts a string range to a table containing number values.

- [setTableProtected](mta://scripting/shared/functions/settableprotected.md) » This function protects a table and makes it read-only.

- [setTableToSql](mta://scripting/shared/functions/settabletosql.md) » This function is used to save the table in the database (sql).

- [Sort_Functions](mta://scripting/shared/functions/sort-functions.md) » These functions are able to sort your tables by a key.

- [getKeyFromValueInTable](mta://scripting/shared/functions/getkeyfromvalueintable.md) » This function returns the key of the specified value in a table.

- [getTableFromSql](mta://scripting/shared/functions/gettablefromsql.md) » This functionality is used to obtain saved tables using the function ([SetTableToSql](https://wiki.multitheftauto.com/wiki/SetTableToSql)).

- [isValueInTable](mta://scripting/shared/functions/isvalueintable.md) » This function returns true if the value exists in the table, false if the value does not exist in the table.

- [table.compare](mta://scripting/shared/functions/table-compare.md) » This function checks whether two given tables are equal.

- [table.copy](mta://scripting/shared/functions/table-copy.md) » This function copies a whole table and all the tables in that table.

- [table.deepmerge](mta://scripting/shared/functions/table-deepmerge.md) » This function deep merges two tables. Every nested table will be correspondingly merged.

- [table.element](mta://scripting/shared/functions/table-element.md) » This function returns a new table with only userdata content.

- [table.flip](mta://scripting/shared/functions/table-flip.md) » This function returns the table from the last value to the first value, such as reflection.

- [table.getRandomRows](mta://scripting/shared/functions/table-getrandomrows.md) » This function returns random rows from table.

- [table.map](mta://scripting/shared/functions/table-map.md) » This function goes through a table and replaces every field with the return of the passed function, where the field's value is passed as first argument and optionally more arguments.

- [table.merge](mta://scripting/shared/functions/table-merge.md) » This function merges two or more tables together.

- [table.random](mta://scripting/shared/functions/table-random.md) » This function retrieves a random value from a table.

- [table.removeValue](mta://scripting/shared/functions/table-removevalue.md) » This function removes a specified value from a table.

- [table.size](mta://scripting/shared/functions/table-size.md) » This function returns the absolute size of a table.

- [table.flatten](mta://scripting/shared/functions/table-flatten.md) » This function converts a nested table into a flattened table with concatenated keys.

### ACL functions

- [aclGroupClone](mta://scripting/shared/functions/aclgroupclone.md) » This function clone a group to another group with/without ACLs and/or objects.

- [renameAclGroup](mta://scripting/shared/functions/renameaclgroup.md) » This function gives an existing ACL group a new name.

- [getPlayersInACLGroup](mta://scripting/shared/functions/getplayersinaclgroup.md) » This function returns all players in an ACL group.

- [isPlayerInACL](mta://scripting/shared/functions/isplayerinacl.md) » This function checks if a player element is in an ACL group.

### Account functions

- [getPlayerFromAccountName](mta://scripting/shared/functions/getplayerfromaccountname.md) » This function is used to obtain a player by the name of his account.

- [isPlayerAccount](mta://scripting/shared/functions/isplayeraccount.md) » This function checks if the account is a valid player account (account exists and is not a guest account)

### Camera functions

- [smoothMoveCamera](mta://scripting/shared/functions/smoothmovecamera.md) » This function allows you to create a cinematic camera flight.

- [sCamera](mta://scripting/shared/functions/scamera.md) » The function creates a speed camera in-game, fines speeding vehicles, and notifies the driver and take money from player based on vehicle speed.

### Colshape functions

- [createGarageColShape](mta://scripting/shared/functions/creategaragecolshape.md) » This function creates a collision shape from the specified garage.

### Cursor functions

- [getCursorMovedOn](mta://scripting/shared/functions/getcursormovedon.md) » This function checks in which way the cursor is currently moving.

- [setCursorCenteredOnRectangle](mta://scripting/shared/functions/setcursorcenteredonrectangle.md) » This functions will center the cursor inside a rectangle.

### Drawing functions

- [dxDrawAnimWindow](mta://scripting/shared/functions/dxdrawanimwindow.md) » This function draws an animated 2D window on the screen.

- [dxDrawBorderedRectangle](mta://scripting/shared/functions/dxdrawborderedrectangle.md) » This is a function that will create a bordered rectangle.

- [dxDrawBorderedText](mta://scripting/shared/functions/dxdrawborderedtext.md) » This is a function that will create a bordered text.

- [dxDrawDashedLine](mta://scripting/shared/functions/dxdrawdashedline.md) » This function draws a line with dashes.

- [dxDrawEditbox](mta://scripting/shared/functions/dxdraweditbox.md) » This function draws a edit box across the screen - rendered for one frame. This should be used in conjunction with **onClientRender** in order to display continuously.

- [dxDrawGifImage](mta://scripting/shared/functions/dxdrawgifimage.md) » This function simulates the effect of a GIF image by using image sprites in 2D.

- [dxDrawImage3D](mta://scripting/shared/functions/dxdrawimage3d.md) » This function draws a 3D image in GTA world.

- [dxDrawImageOnElement](mta://scripting/shared/functions/dxdrawimageonelement.md) » This function draws an image on any element.

- [dxDrawLinedRectangle](mta://scripting/shared/functions/dxdrawlinedrectangle.md) » This is a function that will create a rectangle outline with dx lines.

- [dxDrawLoading](mta://scripting/shared/functions/dxdrawloading.md) » This function draws a loading bar on the screen.

- [dxDrawOctagon3D](mta://scripting/shared/functions/dxdrawoctagon3d.md) » This function creates a 3D Octagon

- [dxDrawPolygon](mta://scripting/shared/functions/dxdrawpolygon.md) » This function draws a custom polygon on the screen.

- [dxDrawProgressBar](mta://scripting/shared/functions/dxdrawprogressbar.md) » This function simulates a progress bar drawed using DirectDraw.

- [dxDrawRectangle3D](mta://scripting/shared/functions/dxdrawrectangle3d.md) » This function draws a 3D rectangle in GTA world.

- [dxDrawRectangleOnPlayer](mta://scripting/shared/functions/dxdrawrectangleonplayer.md) » This function draws a 3D rectangle above the player.

- [dxDrawRing](mta://scripting/shared/functions/dxdrawring.md) » This function draws a ring with dx lines.

- [dxDrawRombo](https://wiki.multitheftauto.com/index.php?search=dxDrawRombo) » This function creates a Rhombus.

- [dxDrawSprite](mta://scripting/shared/functions/dxdrawsprite.md) » This function draw a sprite in the 3D world.

- [dxDrawTextOnElement](mta://scripting/shared/functions/dxdrawtextonelement.md) » This function draws a text on any element.

- [dxDrawTextOnRectangle](mta://scripting/shared/functions/dxdrawtextonrectangle.md) » Esta funcion crea un rectangle con un texto dentro.

- [dxDrawTriangle](mta://scripting/shared/functions/dxdrawtriangle.md) » This is a function that will create a triangle with dx lines.

- [dxDrawBordered3DLine](mta://scripting/shared/functions/dxdrawbordered3dline.md) »This function creates a bordered area with 3D dx lines.

- [dxFade](mta://scripting/shared/functions/dxfade.md) » This function fade-in or fade-out any dxDraw by gradually changing its alpha value.

- [dxGetFontSizeFromHeight](mta://scripting/shared/functions/dxgetfontsizefromheight.md) » This function calculates the font size from given height.

- [dxGetRealFontHeight](mta://scripting/shared/functions/dxgetrealfontheight.md) » This function calculates the height of a font.

- [wordWrap](mta://scripting/shared/functions/wordwrap.md) » This function breaks a long string into a table of separate lines limited to a specific length in pixels, for drawing separately.

- [CreateRectangle3D](mta://scripting/shared/functions/createrectangle3d.md) » This is a function that will create a 3d rectangle on the player screen.

- [getScreenStartPositionFromBox](mta://scripting/shared/functions/getscreenstartpositionfrombox.md) » This function helps with getting the correct position for your dx-effects.

### Effects functions

- [attachEffect](mta://scripting/shared/functions/attacheffect.md) » This function allows you attach an effect to an element.

- [setScreenFlash](mta://scripting/shared/functions/setscreenflash.md) » This function will make the screen flash(like a screenshot).

### Element functions

- [autoAttach](mta://scripting/shared/functions/autoattach.md) » This function attaches one element into another at the same position and rotation they are.

- [attachElementToBone](mta://scripting/shared/functions/attachelementtobone.md) » This function allows you to attach an element to ped bone accurately using new bone functions.

- [getElementDirectionCardialPoint](mta://scripting/shared/functions/getelementdirectioncardialpoint.md) » This function returns the direction of the element according to the *wind rose*.

- [getElementSpeed](mta://scripting/shared/functions/getelementspeed.md) » This function returns the specified element's speed in m/s, km/h or mph.

- [getElementUsingData](mta://scripting/shared/functions/getelementusingdata.md) » This function returns table elements that contains the elements data with the given key and value.

- [getElementZoneFullName](mta://scripting/shared/functions/getelementzonefullname.md) » This function allows you to retrieve the zone full name of a element.

- [getElementsInDimension](mta://scripting/shared/functions/getelementsindimension.md) » This function returns a table of elements that are in the specified dimension.

- [getElementsWithinMarker](mta://scripting/shared/functions/getelementswithinmarker.md) » This function returns a table of elements that are within a marker's collision shape.

- [getNearestElement](mta://scripting/shared/functions/getnearestelement.md) » This function returns the nearest element (of a specific type) to a player.

- [getPositionInFrontOfElement](mta://scripting/shared/functions/getpositioninfrontofelement.md) » This function returns position in provided distance away from element, including element's rotation.

- [isElementInAir](mta://scripting/shared/functions/iselementinair.md) » This function checks if an element is in air or not.

- [isElementInPhotograph](mta://scripting/shared/functions/iselementinphotograph.md) » This function checks if an element is in the player's camera picture area.

- [isElementInRange](mta://scripting/shared/functions/iselementinrange.md) » This function allows you to check if an element's range to a main point is within the maximum range.

- [isElementMoving](mta://scripting/shared/functions/iselementmoving.md) » This function checks if an element is moving.

- [isElementPlayer](mta://scripting/shared/functions/iselementplayer.md) » This function checks whether the element is a player or not.

- [isElementWithinAColShape](mta://scripting/shared/functions/iselementwithinacolshape.md) » This function checks if an element is within a collision shape element.

- [multi_check](mta://scripting/shared/functions/multi-check.md) » This function checks one element to many, handy and clean.

- [setElementSpeed](mta://scripting/shared/functions/setelementspeed.md) » This function allows you to set the speed of an element in kph or mph units.

- [getElementResourceName](mta://scripting/shared/functions/getelementresourcename.md) » This function returns the name of the resource that created an element.

### Events

- [onClientPlayerTimeChange](mta://scripting/client/functions/onclientplayertimechange.md) » This code implements an event that is triggered when the player's real time change.

- [onPlayerZoneChange](mta://scripting/shared/functions/onplayerzonechange.md) » This code implements an event that is triggered when the player enters a new area on the map.

- [onVehicleWeaponFire](mta://scripting/shared/functions/onvehicleweaponfire.md) » This code implements an event that is triggered when a player in a vehicle fires a vehicle's weapon.

### Input functions

- [bindControlKeys](mta://scripting/shared/functions/bindcontrolkeys.md) » This function allows you to bind each key bound to a control individually. Doing this bypasses a little MTA restriction.

- [unbindControlKeys](https://wiki.multitheftauto.com/index.php?search=unbindControlKeys) » This function allows you to unbind each key bound to a control individually. Use this function with [bindControlKeys](mta://scripting/shared/functions/bindcontrolkeys.md).

- [getBoundControls](mta://scripting/shared/functions/getboundcontrols.md) » This function returns a table of control names that are bound to the specified key.

- [isCommandHandlerAdded](mta://scripting/shared/functions/iscommandhandleradded.md) » This function allows you to check if a command is added or not in the respective resource.

### Data functions

- [levenshtein](mta://scripting/shared/functions/levenshtein.md) » This function can be used to calculate the Levenshtein distance between two strings.

- [gregorianToJalali](mta://scripting/shared/functions/gregoriantojalali.md) » This function converts gregorian date to jalali/shamsi date.

- [byte2human](mta://scripting/shared/functions/byte2human.md) » This function converts an integer (number of bytes) into a human-readable unit.

- [capitalize](mta://scripting/shared/functions/capitalize.md) » This function capitalizes a given string.

- [convertDate](mta://scripting/shared/functions/convertdate.md) » This function converts date to another look.

- [convertServerTickToTimeStamp](mta://scripting/shared/functions/convertserverticktotimestamp.md) » This function converts server ticks to a unix timestamp.

- [convertTextToSpeech](mta://scripting/shared/functions/converttexttospeech.md) » This function converts the provided text to a speech in the provided language which players can hear.

- [findRotation3D](mta://scripting/shared/functions/findrotation3d.md) » This function takes two sets of XYZ coordinates. It returns the 3D direction from point A to point B.

- [findRotation](mta://scripting/shared/functions/findrotation.md) » This function takes two points and returns the direction from point A to point B.

- [formatDate](mta://scripting/shared/functions/formatdate.md) » This function formats a date on the basis of a format string and returns it.

- [formatNumber](mta://scripting/shared/functions/formatnumber.md) » This function formats large numbers by adding commas.

- [generateRandomASCIIString](mta://scripting/shared/functions/generaterandomasciistring.md) » This function returns a random string which uses ASCII characters.

- [generateString](mta://scripting/shared/functions/generatestring.md) » This function generates a random string with any characters.

- [getAge](mta://scripting/shared/functions/getage.md) » This function calculates the age of a given birthday.

- [getDistanceBetweenElements](mta://scripting/shared/functions/getdistancebetweenelements.md) » Returns the distance between two elements.

- [getDistanceBetweenPointAndSegment2D](mta://scripting/shared/functions/getdistancebetweenpointandsegment2d.md) » This function takes point coordinates and line (a segment) starting and ending coordinates. It returns the shortest distance between the point and the line.

- [getEasterDate](mta://scripting/shared/functions/geteasterdate.md) » This function returns easter date monthday and month for a given year.

- [getElementRelatedAngle](mta://scripting/shared/functions/getelementrelatedangle.md) » This function returns the related angle between one element to another. This is useful to check which side an element is to another.

- [getFreeDimension](mta://scripting/shared/functions/getfreedimension.md) » This function get free dimension.

- [getOffsetFromXYZ](mta://scripting/shared/functions/getoffsetfromxyz.md) » This function allows you to take an entity and a position and calculate the relative offset between them accounting for rotations.

- [getPointFromDistanceRotation](mta://scripting/shared/functions/getpointfromdistancerotation.md) » This function finds a point based on a starting point, direction and distance.

- [getRealMonth](mta://scripting/shared/functions/getrealmonth.md) » This function returns the current month name

- [getRGColorFromPercentage](mta://scripting/shared/functions/getrgcolorfrompercentage.md) »This function returns two integers representing red and green colors according to the specified percentage.

- [getScreenRotationFromWorldPosition](mta://scripting/shared/functions/getscreenrotationfromworldposition.md) » This function returns a screen relative rotation to a world position.

- [getTimestamp](mta://scripting/shared/functions/gettimestamp.md) » This function returns the UNIX timestamp of a specified date and time.

- [getServerAveragePing](mta://scripting/shared/functions/getserveraverageping.md) » This function gets average players ping.

- [gradientString](mta://scripting/shared/functions/gradientstring.md) » This function transforms a string in a new coloured gradient string.

- [hex2rgb](mta://scripting/shared/functions/hex2rgb.md) » This function convert hex to rgb.

- [hexColorToRGB](mta://scripting/shared/functions/hexcolortorgb.md) » This function convert hex string/number to RGBA values.

- [isLeapYear](mta://scripting/shared/functions/isleapyear.md) » This function returns a boolean representing if a given year is a leap year.

- [isValidMail](mta://scripting/shared/functions/isvalidmail.md) » This function checks whether a provided e-mail string is valid.

- [removeHex](mta://scripting/shared/functions/removehex.md) » This function is used to remove hexadecimal numbers (colors, for example) from strings.

- [RGBToHex](mta://scripting/shared/functions/rgbtohex.md) » This function returns a string representing the color in hexadecimal.

- [RGBToHSV](mta://scripting/shared/functions/rgbtohsv.md) » This function convert RGB to HSV color space.

- [RGBToDecimal](mta://scripting/shared/functions/rgbtodecimal.md) » This function convert RGB to Decimal color.

- [secondsToTimeDesc](mta://scripting/shared/functions/secondstotimedesc.md) » This function converts a plain seconds-integer into a user-friendly time description.

- [string.count](mta://scripting/shared/functions/string-count.md) » This function counts the amount of occurences of a string in a string.

- [string.explode](mta://scripting/shared/functions/string-explode.md) » This function splits a string at a given separator pattern and returns a table with the pieces.

- [string.insert](mta://scripting/shared/functions/string-insert.md) » This function inserts a string within another string at a given position.

- [splitMultiple](mta://scripting/shared/functions/splitmultiple.md) » This function improves the split function so that multiple characters can be used as the split at character.

- [switch](mta://scripting/shared/functions/switch.md) » This function allows the value of a variable or expression to control the flow of program execution via a multiway branch.

- [tocolor2rgba](mta://scripting/shared/functions/tocolor2rgba.md) » This function convert tocolor to rgba.

- [toHex](mta://scripting/shared/functions/tohex.md) » This function converts a decimal number to a hexadecimal number, as a fix to be used client-side.

- [var dump](mta://scripting/shared/functions/var-dump.md) » This function outputs information about one or more variables using outputConsole.

- [wavelengthToRGBA](mta://scripting/shared/functions/wavelengthtorgba.md) » This function converts a physical wavelength of light to a RGBA color.

- [fixPersianString](https://wiki.multitheftauto.com/index.php?search=fixPersianString) » This function returns a fixed sorted bilingual RTL for strings consisting of Farsi/Arabic and English.

- [getColorName](mta://scripting/shared/functions/getcolorname.md) » This function retrieves the nearest color name for a given RGB value using an online API.

### GUI functions

- [centerWindow](mta://scripting/shared/functions/centerwindow.md) » This function centers a CEGUI window element responsively in any resolution.

- [isMouseOnGUICloseButton](mta://scripting/shared/functions/ismouseonguiclosebutton.md) » This function allows you to check whether the mouse cursor/pointer is within a gui-window's native close button.

- [isMouseOnGuiElement](mta://scripting/shared/functions/ismouseonguielement.md) » This function allows you to check whether or not your mouse is over a specific gui element, this is especially useful if the gui element has a parent.

- [guiMoveElement](mta://scripting/shared/functions/guimoveelement.md) » This function moves guiElement by/like using moveObject.

- [guiSetStaticImageMovable](mta://scripting/shared/functions/guisetstaticimagemovable.md) » This function allows you to move a static image like a gui window.

##### Comboboxes

- [guiComboBoxAdjustHeight](mta://scripting/shared/functions/guicomboboxadjustheight.md) » This function adjusts a CEGUI combobox element to have the correct height.

##### Gridlists

- [convertGridListToText](mta://scripting/shared/functions/convertgridlisttotext.md) » This function converts grid list contents to text.

- [getGridListRowIndexFromText](mta://scripting/shared/functions/getgridlistrowindexfromtext.md) » This function returns the GridList row index from the specified text.

- [guiGridListAddPlayers](mta://scripting/shared/functions/guigridlistaddplayers.md) » This function add all online players to a grid list.

- [isTextInGridList](mta://scripting/shared/functions/istextingridlist.md) » This function checks if some text exist or not in the GridList.

- [guiGridListGetColumnIDFromTitle](mta://scripting/shared/functions/guigridlistgetcolumnidfromtitle.md) » This function gets a gridlist's column ID from the column title.

- [guiGridListGetSelectedText](mta://scripting/shared/functions/guigridlistgetselectedtext.md) » This function returns a string containing the inner text of a selected gridlist item.

- [guiGridListSetColumnNonSortable](mta://scripting/shared/functions/guigridlistsetcolumnnonsortable.md) » This function makes a gridlist column become non-sortable.

##### Labels

- [guiLabelAddEffect](mta://scripting/shared/functions/guilabeladdeffect.md) » This function add an effects to the gui-label like (shadow, outline).

### Marker functions

- [createMarkerAttachedTo](mta://scripting/shared/functions/createmarkerattachedto.md) » This function creates a marker that is attached to an element.

### Math functions

- [reMap](mta://scripting/shared/functions/remap.md) » Re-maps a number from one range to another.

- [math.clamp](mta://scripting/shared/functions/math-clamp.md) » This function returns the number between range of numbers or it's minimum or maximum.

- [math.getBezierPoint](mta://scripting/shared/functions/math-getbezierpoint.md) » Get N-th order bezier point.

- [math.hypot](mta://scripting/shared/functions/math-hypot.md) » This function returns the Hypotenuse of the triangle given by sides x and y.

- [math.isPointInPolygon](mta://scripting/shared/functions/math-ispointinpolygon.md) » Check if point is inside polygon or not.

- [math.lerp](mta://scripting/shared/functions/math-lerp.md) » Get val between two integer.

- [math.percent](mta://scripting/shared/functions/math-percent.md) » This function returns a percentage from two number values.

- [math.polygonArea](mta://scripting/shared/functions/math-polygonarea.md) » Compute area of any polygon.

- [math.randomDiff](mta://scripting/shared/functions/math-randomdiff.md) » Generates a pseudo-random integer that's always different from the last random number generated.

- [math.rotVecToEulerAngle](mta://scripting/shared/functions/math-rotvectoeulerangle.md) » Rotation Vector To Euler Angle

- [math.round](mta://scripting/shared/functions/math-round.md) » Rounds a number whereas the number of decimals to keep and the method may be set.

- [mathNumber](mta://scripting/shared/functions/mathnumber.md) » This function is a workaround for the client-side floating-point precision of 24-bits.

- [math.percentProgress](mta://scripting/shared/functions/math-percentprogress.md) » Returns a percentage progress from two specific values.

- [math.average](mta://scripting/shared/functions/math-average.md) » This function returns the simple arithmetic mean of multiple numbers.

- [math.absin](mta://scripting/shared/functions/math-absin.md) » This function returns a formula representing the just positive half of a sine wave.

### Map functions

- [assignLod](mta://scripting/shared/functions/assignlod.md) » This function lets you conveniently generate and apply a LOD model to a mapping object.

- [getWorldPositionFromMapPosition](mta://scripting/shared/functions/getworldpositionfrommapposition.md) » This function converts an F11 map position to world position.

- [getClosestPoint](mta://scripting/shared/functions/getclosestpoint.md) » This function finds the closest point from a given element to a list of points in 2D space.

### Ped functions

- [getAlivePlayersInTeam](mta://scripting/shared/functions/getaliveplayersinteam.md) » This function returns a table of the alive players in a team.

- [getGuestPlayers](mta://scripting/shared/functions/getguestplayers.md) » This function gets a players not login or players Guest .

- [getOnlineAdmins](mta://scripting/shared/functions/getonlineadmins.md) » This function returns a table of all logged-in administrators.

- [getPedEyesPosition](mta://scripting/shared/functions/getpedeyesposition.md) » This function allows you to get peds eyes position.

- [getPedGender](mta://scripting/shared/functions/getpedgender.md) » This function allows you to get peds their gender.

- [getPedMaxHealth](mta://scripting/shared/functions/getpedmaxhealth.md) » This function returns a pedestrians's maximum health by converting it from their maximum health stat.

- [getPedMaxOxygenLevel](mta://scripting/shared/functions/getpedmaxoxygenlevel.md) » This function returns a ped's maximum oxygen level by converting it from their maximum underwater stamina stat.

- [getPedWeaponSkill](mta://scripting/shared/functions/getpedweaponskill.md) » This function returns a ped's corresponding weapon skill level name.

- [getPedHitBone](mta://scripting/shared/functions/getpedhitbone.md) » This function gets the approximate number of the bone where the ped is hit.

- [getPlayerFromNamePart](https://wiki.multitheftauto.com/index.php?search=getPlayerFromNamePart) » This function returns a player from partial name.

- [getPlayerFromSerial](mta://scripting/shared/functions/getplayerfromserial.md) » This function returns a player from their serial.

- [getPlayersByData](mta://scripting/shared/functions/getplayersbydata.md) » This function returns a table of players that have the specified data name.

- [getPlayersInPhotograph](mta://scripting/shared/functions/getplayersinphotograph.md) » This function returns a table of all players in photograph.

- [getPlayersInVehicles](mta://scripting/shared/functions/getplayersinvehicles.md) » This function returns a table of the players insides vehicles from a specified dimension.

- [getPlayerNameFromID](mta://scripting/shared/functions/getplayernamefromid.md) » This function will get the player name from the ID element data.

- [isPedAiming](mta://scripting/shared/functions/ispedaiming.md)» This function checks if a pedestrian is aiming their weapon.

- [isPedAimingNearPed](mta://scripting/shared/functions/ispedaimingnearped.md) » This is similar to isPedAiming but uses a colshape to be more precise.

- [isPedDiving](mta://scripting/shared/functions/ispeddiving.md) » This feature checks that pedestrian is diving in the water.

- [isPedDrivingVehicle](mta://scripting/shared/functions/ispeddrivingvehicle.md) » This function checks if a specified pedestrian is driving a vehicle.

- [isPedNearbyWall](mta://scripting/shared/functions/ispednearbywall.md) » This function checks if player/ped is nearby a objects like buildings or walls.

- [isPlayerInTeam](mta://scripting/shared/functions/isplayerinteam.md) » This function checks if a player is in a specified team.

- [setPedAttack](mta://scripting/shared/functions/setpedattack.md) » This function will make a ped attack a specified target.

- [setPedFollow](mta://scripting/shared/functions/setpedfollow.md) » This function will make a ped follow a specified target.

- [isPedFalling](mta://scripting/shared/functions/ispedfalling.md) » This function checks if the player/ped is falling from a high place.

### Player functions

- [countPlayersInRange](mta://scripting/shared/functions/countplayersinrange.md) » This function returns the number of players that are within a certain range of the specified coordinates.

- [getPlayerPreviousAndNextWeapon](mta://scripting/shared/functions/getplayerpreviousandnextweapon.md) » This function returns the player previous and next weapon.

- [getPlayersInRange](mta://scripting/shared/functions/getplayersinrange.md) » This function make a table of players within certain range.

- [isPlayerActuallyInVehicle](mta://scripting/shared/functions/isplayeractuallyinvehicle.md) » This function checks if a player is actually in a vehicle instead of just in the process of entering.

- [isPlayerHitByVehicle](mta://reference/misc/isplayerhitbyvehicle.md) » This function cancels event when a element is hit by a vehicle.

- [toggleAllVehicleControls](mta://reference/misc/toggleallvehiclecontrols.md) » This function toggles all vehicle controls for a player on or off based on the provided boolean value.

- isPlayerNameRandomized » This function Checks whether the given player name looks like an automatically-generated random nickname.

### Resource functions

- [getResourceScripts](mta://scripting/shared/functions/getresourcescripts.md) » This function returns a table of the resource scripts.

- [getResourceSettings](mta://scripting/shared/functions/getresourcesettings.md) » This function returns a table of the resource settings.

- [getResourceSize](mta://scripting/shared/functions/getresourcesize.md) » This function returns the size of a specified resource in kB(kilobyte)

- [refreshResource](mta://scripting/shared/functions/refreshresource.md) » This function refreshes your resource if you changed any of the files

- [setResourcePriority](mta://scripting/shared/functions/setresourcepriority.md) » This function set resource download priority group.

### Sound functions

- [isSoundFinished](mta://scripting/shared/functions/issoundfinished.md) » This function checks if a sound element has finished.

- [stopSoundSlowly](mta://scripting/shared/functions/stopsoundslowly.md) » This function stop your sound element slowly.

### Browser functions

- [playVideo](mta://scripting/shared/functions/playvideo.md) » This function plays a video on the screen.

### Team functions

- [getTeamFromColor](mta://scripting/shared/functions/getteamfromcolor.md) » This function returns a team element by the specified color.

- [getTeamWithFewestPlayers](mta://scripting/shared/functions/getteamwithfewestplayers.md) » This function returns a team element with least players of all the specified teams.

### Vehicle functions

- [findEmptyCarSeat](mta://scripting/shared/functions/findemptycarseat.md) » This function finds you the first empty seat in a vehicle.

- [getNearestVehicle](mta://scripting/shared/functions/getnearestvehicle.md) » This function gets the nearest vehicle to the specified player in a specified distance.

- [getRandomVehicle](mta://scripting/shared/functions/getrandomvehicle.md) » This function gets a random vehicle.

- [getValidVehicleModels](mta://scripting/shared/functions/getvalidvehiclemodels.md) » This function returns a table of all valid vehicle models.

- [getVehiclesCountByType](mta://scripting/shared/functions/getvehiclescountbytype.md) » This function returns the amount of vehicles by the given type as an integer value.

- [getVehicleTurnVelocityCenterOfMass](mta://scripting/shared/functions/getvehicleturnvelocitycenterofmass.md)» This function gets a vehicle's turn velocity relative to the vehicle's center or mass.

- [isVehicleDoubleExhaust](mta://scripting/shared/functions/isvehicledoubleexhaust.md) » This function checks is exhaust vehicle double.

- [isVehicleEmpty](mta://scripting/shared/functions/isvehicleempty.md) » This function checks whether a vehicle is empty.

- [isVehicleOccupied](mta://scripting/shared/functions/isvehicleoccupied.md) » This function checks if a specified vehicle is occupied.

- [isVehicleOnRoof](mta://scripting/shared/functions/isvehicleonroof.md) » This function checks whether vehicle is on roof.

- [isVehicleOnFire](mta://scripting/shared/functions/isvehicleonfire.md) » This function checks if the vehicle is on fire or not.

- [isVehicleReversing](mta://scripting/shared/functions/isvehiclereversing.md) » This function checks if a specified vehicle is moving backwards.

- [isVehicleUpgraded](mta://scripting/shared/functions/isvehicleupgraded.md) » This function checks is vehicle upgraded by upgrade ID.

- [setVehicleGravityPoint](mta://scripting/shared/functions/setvehiclegravitypoint.md) » This function sets a vehicle's gravity in the direction of a 3 dimensional coordinate with the strength specified.

- [setVehicleTurnVelocityCenterOfMass](mta://scripting/shared/functions/setvehicleturnvelocitycenterofmass.md) » This function sets a vehicle's turn velocity relative to the vehicle's center or mass.

- [setVehicleHandlingFromText](mta://scripting/shared/functions/setvehiclehandlingfromtext.md) » This function sets a vehicle's handling from text.

- [setVehicleWheelModel](mta://scripting/shared/functions/setvehiclewheelmodel.md) » This function changes the wheel model of the informed vehicle.

- [setVehicleDirtEnabled](mta://scripting/shared/functions/setvehicledirtenabled.md) » This function toggles a dirt removal shader effect on the specified vehicle.

### Weapon functions

- [getJetpackWeaponsEnabled](mta://scripting/shared/functions/getjetpackweaponsenabled.md) » This function returns a table of enabled weapons usable on a jetpack.

### Object functions

- [getDynamicDoorObjectOpenRatio](mta://scripting/shared/functions/getdynamicdoorobjectopenratio.md) » This function tells you how open a dynamic door is in a range from 0 to 1.

- [isElementObject](mta://scripting/shared/functions/iselementobject.md) » This function tells you if an element is an object or no.

### XML functions

- [getXMLNodes](mta://scripting/shared/functions/getxmlnodes.md) » This function returns all children of a XML node.

### Engine functions

- [engineGetCOLsFromLibrary](mta://scripting/shared/functions/enginegetcolsfromlibrary.md) » This function gets the collision data from the col library.

- [engineLoadIMGContainer](mta://scripting/shared/functions/engineloadimgcontainer.md) » This function loads the IMG container.

### Utility

- [animate](mta://scripting/shared/functions/animate.md) » This function allows you to use interpolateBetween without render event and easily used.

- [callClientFunction](mta://scripting/shared/functions/callclientfunction.md) » This function allows you to call any client-side function from the server's side.

- [callServerFunction](mta://scripting/shared/functions/callserverfunction.md) » This function allows you to call any server-side function from the client's side.

- [check](mta://scripting/shared/functions/check.md) » This function checks if its arguments are of the right type and calls the error-function if one is not.

- [checkPassiveTimer](mta://scripting/shared/functions/checkpassivetimer.md) » This function allows you to use passive timers in your conditions. For example you want to prevent players repeatedly using a command.

- [coroutine.resume](mta://scripting/shared/functions/coroutine-resume.md) » This function applies a fix for hidden coroutine error messages.

- [compact](mta://scripting/shared/functions/compact.md) » This function create table containing variables and their values.

- [createDirectory](mta://scripting/shared/functions/createdirectory.md) » This function creates a directory in the resource's file system.

- [getBanBySerial](mta://scripting/shared/functions/getbanbyserial.md) » This function returns the ban if the serial is banned.

- [getBanFromName](mta://scripting/shared/functions/getbanfromname.md) » This functions returns the ban of the given playername.

- [getCurrentFPS](mta://scripting/shared/functions/getcurrentfps.md) » This function returns the frames per second at which GTA: SA is running.

- [getSkinNameFromID](mta://scripting/shared/functions/getskinnamefromid.md) » This function returns the name of the skin from the given id.

- [IfElse](mta://scripting/shared/functions/ifelse.md) » This function returns one of two values based on a boolean expression.

- [isLastExecuteInTimer](mta://scripting/shared/functions/islastexecuteintimer.md) » This function check if the execute is the last execute in the timer.

- [isMouseInCircle](mta://scripting/shared/functions/ismouseincircle.md) » This function checks if a cursor position is in circular area or not.

- [isMouseInPosition](mta://scripting/shared/functions/ismouseinposition.md) » This function allows you to check whether the mouse cursor/pointer is within a rectangular position.

- [iterElements](mta://scripting/shared/functions/iterelements.md) » This function returns *a time-saving* iterator for your for-loops.

- [PlotTrajectoryAtTime](mta://scripting/shared/functions/plottrajectoryattime.md) » Calculate projectile/water trajectory.

- [preprocessor](mta://scripting/shared/functions/preprocessor.md) » This function allow you to use gcc macros.

- [vector3:compare](mta://scripting/shared/functions/vector3-compare.md) » This method checks whether two vectors match, with optional precision.

- [svgCreateRoundedRectangle](mta://scripting/shared/functions/svgcreateroundedrectangle.md) » This function creates a rectangle with rounded edges.

- [debounce](mta://scripting/shared/functions/debounce.md) » This function is removing unwanted input noise.

- [listAllFiles](mta://scripting/shared/functions/listallfiles.md) » This function lists all files and subdirectories within a given directory and its subdirectories.

- [dumpdelete](mta://scripting/shared/functions/dumpdelete.md) » This function recursively deletes elements inside a table, destroying elements like vehicles, peds, or killing timers.

- [isEventHandlerAdded](mta://scripting/shared/functions/iseventhandleradded.md) » This function checks whether a specific event handler has already been added to an element.

- [wait](mta://scripting/shared/functions/wait.md) » This function pauses the execution of a function for a specific amount of time. It allows you to write sequential, readable code instead of using complex callback structures or multiple timers.

### String functions

- [string.endsWith](mta://scripting/shared/functions/string-endswith.md) » This function checks if a string ends with other string.

- [string.startsWith](mta://scripting/shared/functions/string-startswith.md) » This function checks if a string starts with other string.

- [string.repetition](mta://scripting/shared/functions/string-repetition.md) » This function repeats a substring n times.
