import time
import os
from resizeable_image import ResizeableImage

def measure_seam_generation(image_folder, output_file):
    """
    Measure the time it takes to generate a seam for each image in a folder.
    
    Args:
    - image_folder: Path to the folder containing images.
    - output_file: Path to save the results in a text file.
    
    Output:
    - A text file containing the image name and the time taken to generate a seam (in seconds, with precision).
    """
    results = []

    # Iterate through all images in the folder
    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)

        # Only process image files
        if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            continue

        print(f"Processing {image_name}...")

        # Create an instance of ResizeableImage
        image = ResizeableImage(image_path)

        # Measure time to generate the best seam
        start_time = time.perf_counter()
        seam = image.best_seam()  # Generate the seam
        elapsed_time = time.perf_counter() - start_time  # Time in seconds

        print(f"Time taken for {image_name}: {elapsed_time:.6f} seconds")
        results.append((image_name, elapsed_time))

    # Save results to a file
    with open(output_file, 'w') as f:
        f.write("Image Name, Time (seconds)\n")
        for image_name, elapsed_time in results:
            f.write(f"{image_name}, {elapsed_time:.6f}\n")

    print(f"Results saved to {output_file}")
# Example usage
image_folder = "Images/"
output_file = "seam_generation_times.csv"
measure_seam_generation(image_folder, output_file)
