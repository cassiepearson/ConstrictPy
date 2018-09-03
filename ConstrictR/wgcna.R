# WCGNA Function
#
# Description: Custom implementation of weighted correlation network analysis (WCGNA). This function
#              creates and returns the Topological Overlap Matrix (TOM) from the correlation of data
#              within the dataframe. This will turn corrleation data into network data, allowing
#              various network analysis methods to be applied.
# Required Parameters: df: dataframe
# Optional Parameters: signed: To use the signed or unsigned adjacency in the analysis, signed by default,
#                      thresh: the threshold for the adjacency matrix calculation, recommended changed to 6 for unsigned,
#                      verbose: Change to true for printing returned results to console

wgcna <- function(df,
                  signed = TRUE,
                  thresh = 12,
                  verbose = FALSE) {
  # Create an adjacency matrix
  adj <- adjMatrix(df)
  
  # Calculate needed information for creating the Topological Overlap Matrix (TOM)
  # Create two lists of row and column sums
  k <- rowSums(adj)
  l <- colSums(adj)
  
  # Create a matrix where Aij=ki*lj where u is all nodes in the matrix
  m <- matrix(, nrow = nrow(adj), ncol = ncol(adj))
  for (i in 1:nrow(adj)) {
    for (j in 1:ncol(adj)) {
      m[i, j] = k[i] * l[j]
    }
  }
  
  # Create the Topological Overlap Matrix (TOM)
  tom <- matrix(, nrow = nrow(adj), ncol = ncol(adj))
  for (i in 1:nrow(adj)) {
    for (j in 1:ncol(adj)) {
      if (i == j) {
        tom[i, j] = 1
      } else{
        tom[i, j] = (m[i, j] + adj[i, j]) / ((min(k[i], k[j]) + 1) - adj[i, j])
      }
    }
  }
  
  # Create a results dataframe
  results <- as.data.frame(tom)
  colnames(results) <- colnames(df)
  
  # Print and return results
  if (verbose == TRUE) {
    print(results)
  }
  return(results)
  
} # End desc_stats function
