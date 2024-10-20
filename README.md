# Water-Segmentation-using-Multispectral-and-optical-Data
The objective of this project is to develop a robust solution for accurately segmenting water bodies using multispectral and optical data. This solution is crucial for monitoring water resources, managing floods, and conserving the environment. Accurate segmentation of water bodies can significantly impact decision-making processes in these areas.

## Preprocessing and Model Development
To achieve the objective, the project focuses on the following key requirements:

### 1.Preprocessing:
- Data Preparation: Prepare the multispectral and optical data while maintaining the original shape and resolution of the images. This step is essential to preserve the spatial integrity of the data for accurate segmentation.
- Normalization: Apply normalization techniques to standardize the input data from different sensors. This improves model performance and stability during training.

### 2.Model Architecture and Training:
- Utilize deep learning models suited for segmentation tasks which is U-Net.It is effective for pixel-level classification and will be trained to segment water bodies from the input multispectral and optical data.
- Using DeepLabv3 architecture. To handle the problem of segmenting objects at multiple scales.
