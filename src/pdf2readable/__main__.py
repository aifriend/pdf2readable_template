"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Data Science Template."""


if __name__ == "__main__":
    main(prog_name="pdf2readable")  # pragma: no cover
