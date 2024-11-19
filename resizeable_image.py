import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=True):
        width, height = self.width, self.height
        # Helper function to recursively compute seam energy
        def compute_seam_energy(i, j, memo):
            if j == height:  # Reached bottom row
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            energy = self.energy(i, j)
            min_energy = energy + min(
                compute_seam_energy(i + di, j + 1, memo)
                for di in (-1, 0, 1)
                if 0 <= i + di < width
            )
            memo[(i, j)] = min_energy
            return min_energy
        
        # Find the seam starting from top row with minimum energy
        memo = {}
        best_start = min((compute_seam_energy(i, 0, memo), i) for i in range(width))[1]
        
        # Recover seam from top to bottom
        seam = []
        i = best_start
        for j in range(height):
            seam.append((i, j))
            i += min(
                ((compute_seam_energy(i + di, j + 1, memo), di)
                 for di in (-1, 0, 1)
                 if 0 <= i + di < width),
                key=lambda x: x[0]
            )[1]
        
        return seam
