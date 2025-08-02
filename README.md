# Image Cropper

Image Cropper is a Python and Rust-based CLI tool and library for cropping images efficiently. It leverages Rust's performance and safety via a native extension, exposed to Python using [PyO3](https://pyo3.rs/) and packaged with [maturin](https://github.com/PyO3/maturin).

## Features

- Crop images using a fast Rust backend.
- Simple Python API for integration.
- Command-line interface powered by [Typer](https://typer.tiangolo.com/).
- Supports common image formats (JPEG, PNG, etc.).
- Cross-platform (Linux, macOS, Windows).

## Installation

You need Python ≥3.8 and Rust installed.

## CLI Usage

```bash
image_cropper IMAGE_PATH [OPTIONS]
```

### Arguments

- `IMAGE_PATH`: Path to the image file to crop.

### Options

- `-x`: X-coordinate of the top-left corner of the crop rectangle.
- `-y`: Y-coordinate of the top-left corner of the crop rectangle.
- `-w`, `--width`: Width of the crop rectangle.
- `-h`, `--height`: Height of the crop rectangle.
- `-o`, `--output`: Output file path for the cropped image. Defaults to `cropped_<original_filename>`.

### Example

```bash
image_cropper my_image.jpg -x 50 -y 50 -w 200 -h 200 -o cropped_image.jpg
```

## Python API Usage

```python
from image_cropper import Image

img = Image("input.jpg")
cropped = img.crop(10, 20, 100, 200)
cropped.save("output.jpg")
```

## Project Structure

- `lib.rs`: Rust implementation of the image cropping logic, exposed to Python.
- `main.py`: Python CLI entry point using Typer.
- `pyproject.toml`: Project configuration for building and packaging.
- `__init__.py`: Python package initialization file.
- `image_cropper.pyi`: Type hints for the Python API.

## Development

- Build and test with maturin and Python.
- Rust code uses the [image](https://crates.io/crates/image) crate for image manipulation.
- Python CLI uses Typer for argument parsing and user interaction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
