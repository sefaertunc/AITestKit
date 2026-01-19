from pathlib import Path
from typing import Literal
import functools

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Model ID constants
OPUS_MODEL = "claude-opus-4-5-20251101"
SONNET_MODEL = "claude-sonnet-4-5-20250929"
HAIKU_MODEL = "claude-haiku-4-5-20251001"

# Type alias for model selection
ModelType = Literal["opus", "sonnet", "haiku"]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AITESTKIT_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra ="ignore"
    )
    anthropic_api_key: str = Field(..., validation_alias="ANTHROPIC_API_KEY")
    model_code_gen: str = OPUS_MODEL
    model_analysis: str = SONNET_MODEL
    model_regression: str = HAIKU_MODEL
    max_tokens: int = 4096
    temperature: float = 0.3
    output_dir: Path = Path("./generated")
    log_level: str = "INFO"
    default_framework: str = "pytest"
    warn_after_n: int = 10

    def get_model_id(self, model_type: ModelType) -> str:
        """Get the model ID for the specified model type.

        Args:
            model_type: The type of model ("opus", "sonnet", or "haiku")

        Returns:
            The full model ID string

        Raises:
            ValueError: If model_type is invalid
        """
        mapping = {
            "opus": self.model_code_gen,
            "sonnet": self.model_analysis,
            "haiku": self.model_regression,
        }

        if model_type not in mapping:
            raise ValueError(
                f"Invalid model_type: {model_type}. "
                f"Must be one of: {list(mapping.keys())}"
            )

        return mapping[model_type]


@functools.lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance.

    Uses LRU cache to ensure only one Settings instance is created.
    This prevents multiple reads of .env file.
    """
    return Settings()


# Project configuration models for .aitestkit/project.yaml
class ProductConfig(BaseModel):
    """Product-level configuration."""

    name: str
    type: Literal["web_app", "api", "desktop", "mobile", "cli"] = "web_app"
    tech_stack: list[str] = []


class DefaultsConfig(BaseModel):
    """Default settings for generation."""

    framework: str = "pytest"
    output_dir: str = "tests/generated"


class GenerationConfig(BaseModel):
    """Generation behavior configuration."""

    warn_after_n: int = 10


class ModelsConfig(BaseModel):
    """Model override configuration."""

    code_generation: str = OPUS_MODEL
    analysis: str = SONNET_MODEL
    regression: str = HAIKU_MODEL


class ProjectConfig(BaseModel):
    """Project-level configuration from .aitestkit/project.yaml."""

    schema_version: int = 1
    product: ProductConfig
    defaults: DefaultsConfig = DefaultsConfig()
    generation: GenerationConfig = GenerationConfig()
    models: ModelsConfig = ModelsConfig()


def load_project_config(project_root: Path | None = None) -> ProjectConfig | None:
    """Load project configuration from .aitestkit/project.yaml.

    Args:
        project_root: Root directory of the project. If None, uses current directory.

    Returns:
        ProjectConfig if file exists and is valid, None otherwise.
    """
    if project_root is None:
        project_root = Path.cwd()

    config_path = project_root / ".aitestkit" / "project.yaml"
    if not config_path.exists():
        return None

    with config_path.open() as f:
        data = yaml.safe_load(f)

    return ProjectConfig(**data) if data else None