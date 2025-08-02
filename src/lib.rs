use image::DynamicImage;
use image::ImageReader;
use std::path::PathBuf;

use pyo3::prelude::*;

#[derive(Clone)]
#[pyclass(module = "image_cropper")]
struct Image {
    #[pyo3(get)]
    path: PathBuf,
    #[pyo3(get)]
    width: u32,
    #[pyo3(get)]
    height: u32,
    image_data: DynamicImage,
}

#[pymethods]
impl Image {
    /// Reads an image from a numpy array or PIL Image.
    #[new]
    fn new(path: PathBuf) -> PyResult<Self> {
        let img_reader = match ImageReader::open(&path) {
            Ok(reader) => reader,
            Err(e) => {
                return Err(PyErr::new::<pyo3::exceptions::PyIOError, _>(format!(
                    "Failed to open image: {}",
                    e
                )));
            }
        };

        let img = match img_reader.decode() {
            Ok(image) => image,
            Err(e) => {
                return Err(PyErr::new::<pyo3::exceptions::PyIOError, _>(format!(
                    "Failed to decode image: {}",
                    e
                )));
            }
        };

        Ok(Image {
            path: PathBuf::from(path),
            width: img.width(),
            height: img.height(),
            image_data: img,
        })
    }

    /// Crops the image to the specified rectangle.
    fn crop(&self, x: u32, y: u32, width: u32, height: u32) -> PyResult<Self> {
        if x + width > self.width || y + height > self.height {
            return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                "Crop rectangle exceeds image dimensions",
            ));
        }

        let cropped_data = self.image_data.crop_imm(x, y, width, height);

        Ok(Image {
            path: self.path.clone(),
            width,
            height,
            image_data: cropped_data,
        })
    }

    fn save(&self, path: PathBuf) -> PyResult<()> {
        self.image_data.save(&path).map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyIOError, _>(format!("Failed to save image: {}", e))
        })
    }
}

#[pymodule]
mod image_cropper {
    #[pymodule_export]
    use super::Image;
}
