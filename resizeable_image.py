import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=False):
        width, height = self.width, self.height

        def compute_seam_energy(seam):
            """Compute total energy for a given seam."""
            return sum(self.energy(x, y) for x, y in seam)

        def enumerate_seams(x, y):
            """Recursively generate all seams starting from pixel (x, y)."""
            if y == height - 1:
                return [[(x, y)]]
            
            seams = []
            for dx in [-1, 0, 1]:  # Explore (left-diagonal, vertical, right-diagonal)
                nx = x + dx
                if 0 <= nx < width:
                    for seam in enumerate_seams(nx, y + 1):
                        seams.append([(x, y)] + seam)
            return seams
        
        all_seams = []
        for x in range(width):
            all_seams.extend(enumerate_seams(x, 0))

        # Find the seam with the minimum energy
        best_seam = min(all_seams, key=compute_seam_energy)
        return best_seam
