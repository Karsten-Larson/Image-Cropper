import typer
from image_cropper.image_cropper import Image

app = typer.Typer()

@app.command()
def main(
    image_path: str = typer.Argument(..., help="Path to the image file"),
    x: int = typer.Option(0, "-x", help="X coordinate of the top-left corner"),
    y: int = typer.Option(0, "-y", help="Y coordinate of the top-left corner"),
    width: int = typer.Option(None, "-w", "--width", help="Width of the crop area"),
    height: int = typer.Option(None, "-h", "--height", help="Height of the crop area"),
    output_path: str = typer.Option(None, "--output", "-o", help="Path to save the cropped image")
):
    """
    Main function to run the image cropper.
    """
    typer.echo("Image Cropper is running...")

    # Load the image
    try:
        img = Image(image_path)
    except OSError as e:
        typer.secho("Error loading image:", fg=typer.colors.RED, bold=True)
        typer.secho(f"  {e}", fg=typer.colors.RED)
        typer.secho("Hint:", fg=typer.colors.YELLOW, bold=True)
        typer.echo("  Ensure the image path is correct and the file is a valid image format.")
        typer.secho("Exiting...", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # Set defaults if None
    if x is None:
        x = 0
    if y is None:
        y = 0
    if width is None:
        width = img.width
    if height is None:
        height = img.height

    try: 
        crop = img.crop(x, y, width, height)
    except ValueError as e:
        typer.secho("Error cropping image:", fg=typer.colors.RED, bold=True)
        typer.secho(f"  {e}", fg=typer.colors.RED)
        typer.secho("Hint:", fg=typer.colors.YELLOW, bold=True)
        typer.echo(f"  Ensure the crop dimensions are within the image bounds.")
        typer.echo(f"  Image size: {img.width} x {img.height}")
        typer.echo(f"  Crop: {width} x {height} at ({x}, {y})")
        typer.secho("Exiting...", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    if output_path is None:
        output_path = str(img.path.parent / f"cropped_{img.path.name}")

    crop.save(output_path)

    typer.echo(f"Cropped image saved to {output_path}")