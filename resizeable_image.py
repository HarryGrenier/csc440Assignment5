import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        """
        Finds the vertical seam with the minimum energy using dynamic programming.
        Returns the seam as a list of (i, j) tuples.
        """
        width, height = self.width, self.height

        # Create the dp table to store minimum energy up to each pixel
        dp = [[0] * height for _ in range(width)]
        backtrack = [[0] * height for _ in range(width)]

        # Initialize the dp values for the first row
        for i in range(width):
            dp[i][0] = self.energy(i, 0)

        # Fill the dp table row by row
        for j in range(1, height):
            for i in range(width):
                # Find the minimum energy from the row above
                min_energy = dp[i][j - 1]
                direction = 0  # Default is straight up

                if i > 0 and dp[i - 1][j - 1] < min_energy:
                    min_energy = dp[i - 1][j - 1]
                    direction = -1  # Diagonal left

                if i < width - 1 and dp[i + 1][j - 1] < min_energy:
                    min_energy = dp[i + 1][j - 1]
                    direction = 1  # Diagonal right

                # Update dp and backtrack tables
                dp[i][j] = self.energy(i, j) + min_energy
                backtrack[i][j] = direction

        # Find the starting point of the best seam
        # Get the index of the minimum energy in the last row of dp
        min_end_index = min(range(width), key=lambda i: dp[i][height - 1])

        # Recover the seam using the backtrack table
        seam = []
        i = min_end_index
        for j in range(height - 1, -1, -1):
            seam.append((i, j))
            i += backtrack[i][j]

        seam.reverse()  # Seam recovered from bottom to top; reverse it
        return seam
