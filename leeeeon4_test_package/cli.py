"""Console script for leeeeon4_test_package."""
import sys
import click
from leeeeon4_test_package.leeeeon4_test_package import ingredients


@click.command()
@click.argument('count', type=int)
def main(count):
    """Console script for leeeeon4_test_package."""
    ingredients(count)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
