import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=False):
        width, height = self.width, self.height

        def enumerate_seams(x, y):
            """Generate all seams starting from pixel (x, y)."""
            if y == height - 1:
                return [[(x, y)]]  # Base case: return the current pixel as a seam

            seams = []
            for dx in [-1, 0, 1]:  # Explore neighbors: left, down, right
                nx = x + dx
                if 0 <= nx < width:
                    # Recursively generate seams for the next row
                    for seam in enumerate_seams(nx, y + 1):
                        seams.append([(x, y)] + seam)
            return seams

        # Collect all seams starting from the top row
        all_seams = []
        for x in range(width):
            all_seams.extend(enumerate_seams(x, 0))

        # Calculate the energy for each seam
        def compute_energy(seam):
            return sum(self.energy(x, y) for x, y in seam)

        # Find the seam with the minimum energy
        best_seam = min(all_seams, key=compute_energy)
        return best_seam
