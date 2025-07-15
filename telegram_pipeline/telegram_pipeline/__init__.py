from dagster import Definitions, load_assets_from_modules
from .pipe import telegram_pipeline_job
from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)

__all__ = ["telegram_pipeline_job"]
