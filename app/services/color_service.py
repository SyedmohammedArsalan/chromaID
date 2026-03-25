from app.models.schemas import ColorReport, PaletteSection

PALETTE_LIBRARY = {
    "Dark Autumn": {
        "undertone": "Warm-Neutral",
        "day_best": ["Forest Green", "Saddle Brown", "Camel", "Rust", "Warm Teal", "Dark Chocolate", "Cognac", "Olive Green", "Deep Mustard", "Ivory", "Burnt Orange", "Dark Walnut"],
        "day_avoid": ["Icy Blue", "Lavender", "Pure White", "Baby Pink", "Cool Grey", "Mint Green"],
        "day_metals": ["Warm Gold", "Rose Gold"],
        "night_best": ["Burgundy", "Hunter Green", "Midnight Navy", "Deep Plum", "Rust Red", "Deep Teal", "Crimson", "Espresso Black", "Bronze", "Dark Gold", "Oxblood", "Dark Tobacco"],
        "night_avoid": ["Pastel Grey", "Light Pink", "Sage", "Peach", "Icy Periwinkle", "Silver"],
        "night_metals": ["Yellow Gold", "Bronze", "Copper"]
    },
    "Winter": {
        "undertone": "Cool-Clear",
        "day_best": ["True Black", "Pure White", "Emerald Green", "Cobalt Blue", "Icy Pink", "Royal Purple"],
        "day_avoid": ["Warm Brown", "Mustard Yellow", "Olive Green", "Rust", "Peach"],
        "day_metals": ["Silver", "Platinum"],
        "night_best": ["Deep Sapphire", "Ruby Red", "Amethyst", "Charcoal", "Midnight Blue"],
        "night_avoid": ["Orange", "Golden Yellow", "Earth Tones"],
        "night_metals": ["Silver", "White Gold"]
    },
    "Spring": {
        "undertone": "Warm-Clear",
        "day_best": ["Peach", "Golden Yellow", "Coral", "Light Green", "Turquoise", "Warm Beige", "Cream"],
        "day_avoid": ["Black", "Dark Brown", "Burgundy", "Navy", "Cool Grey"],
        "day_metals": ["Light Gold", "Rose Gold"],
        "night_best": ["Bright Red", "Kelly Green", "Vibrant Violet", "Warm Teal", "Goldenrod"],
        "night_avoid": ["Charcoal", "Deep Plum", "Dusty Pink", "Silver"],
        "night_metals": ["Bright Yellow Gold"]
    },
    "Summer": {
        "undertone": "Cool-Muted",
        "day_best": ["Soft Navy", "Dusty Blue", "Lavender", "Powder Pink", "Soft White", "Taupe"],
        "day_avoid": ["Black", "Orange", "Mustard", "Rust", "Neon Colors"],
        "day_metals": ["Silver", "White Gold"],
        "night_best": ["Plum", "Raspberry", "Slate Blue", "Cool Burgundy", "Charcoal"],
        "night_avoid": ["Warm Brown", "Bright Yellow", "Warm Green", "Bronze"],
        "night_metals": ["Silver", "Platinum"]
    }
}

def generate_report(season_type: str) -> ColorReport:
    data = PALETTE_LIBRARY.get(season_type, PALETTE_LIBRARY["Dark Autumn"])

    return ColorReport(
        season_type=season_type,
        undertone=data["undertone"],
        day_palette=PaletteSection(
            context="Natural light",
            best_colors=data["day_best"],
            avoid_colors=data["day_avoid"],
            metals=data["day_metals"]
        ),
        night_palette=PaletteSection(
            context="Artificial light",
            best_colors=data["night_best"],
            avoid_colors=data["night_avoid"],
            metals=data["night_metals"]
        )
    )