from pydantic import BaseModel, Field
from typing import List


class PaletteSection(BaseModel):
    context: str = Field(..., examples=["Natural light", "Artificial light"])
    best_colors: List[str]
    avoid_colors: List[str]
    metals: List[str]


class ColorReport(BaseModel):
    season_type: str = Field(..., examples=["Dark Autumn"])
    undertone: str = Field(..., examples=["Warm-Neutral"])
    day_palette: PaletteSection
    night_palette: PaletteSection


class AnalyzeResponse(BaseModel):
    name: str
    season_type: str


class AnalyzeRequest(BaseModel):
    name: str