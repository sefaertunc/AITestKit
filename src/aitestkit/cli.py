import click

from aitestkit.frameworks.registry import format_framework_table


@click.group()
def cli() -> None:
    """AITestKit - AI-Powered Multi-Framework Test Generation Toolkit."""
    pass


@cli.command()
def info() -> None:
    """Display current configuration settings."""
    click.echo("Current configuration settings:")
    click.echo(" - Model for Code Generation: claude-opus-4-5-20251101")
    click.echo(" - Model for Analysis: claude-sonnet-4-5-20250929")
    click.echo(" - Model for Regression: claude-haiku-4-5-20251001")


@cli.command()
@click.option("--list", "list_frameworks", is_flag=True, help="List all supported frameworks.")
def frameworks(list_frameworks: bool) -> None:
    """Manage supported testing frameworks."""
    if list_frameworks:
        table = format_framework_table()
        click.echo(table)
