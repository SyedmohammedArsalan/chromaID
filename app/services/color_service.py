from app.models.schemas import ColorReport, PaletteSection

# Temporary in-memory store (replace with DB later)
user_store = {}


def analyze_user(name: str) -> str:
    # Mock logic (replace with ML later)
    return "Dark Autumn"


def generate_report(season_type: str) -> ColorReport:
    # Hardcoded based on your PDF

    return ColorReport(
        season_type="Dark Autumn",
        undertone="Warm-Neutral",

        day_palette=PaletteSection(
            context="Natural light",
            best_colors=[
                "Forest Green", "Saddle Brown", "Camel", "Rust",
                "Warm Teal", "Dark Chocolate", "Cognac",
                "Olive Green", "Deep Mustard", "Ivory",
                "Burnt Orange", "Dark Walnut"
            ],
            avoid_colors=[
                "Icy Blue", "Lavender", "Pure White",
                "Baby Pink", "Cool Grey", "Mint Green"
            ],
            metals=["Warm Gold", "Rose Gold"]
        ),

        night_palette=PaletteSection(
            context="Artificial light",
            best_colors=[
                "Burgundy", "Hunter Green", "Midnight Navy",
                "Deep Plum", "Rust Red", "Deep Teal",
                "Crimson", "Espresso Black", "Bronze",
                "Dark Gold", "Oxblood", "Dark Tobacco"
            ],
            avoid_colors=[
                "Pastel Grey", "Light Pink", "Sage",
                "Peach", "Icy Periwinkle", "Silver"
            ],
            metals=["Yellow Gold", "Bronze", "Copper"]
        )
    )