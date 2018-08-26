# Adjacency Matrix Creation Function
#
# Description: Custom implementation of algorithm calculating the adjacendy matrix. This will
#              turn correlation data into network data, allowing various network analysis methods to be applied.
# Required Parameters: df: dataframe
# Optional Parameters: signed: To use the signed or unsigned adjacency in the analysis, signed by default,
#                      thresh: the threshold for the adjacency matrix calculation, recommended changed to 6 for unsigned,
#                      verbose: Change to true for printing returned results to console

adjMatrix <- function(df,
                      signed = TRUE,
                      thresh = 12,
                      verbose = FALSE) {
  # Create Pearson's correlation matrix
  corr <-
    cor(t(data.matrix(df)), use = "complete.obs", method = "pearson")
  
  # Create a matrix, then apply thresholding parameter (6 or 12 standard) to create adjacency matrix
  if (signed) {
    results <-
      apply(apply(corr, c(1, 2), function(x)
        0.5 + 0.5 * x), c(1, 2), function(x)
          x ** thresh)
  }
  else {
    results <-
      apply(apply(corr, c(1, 2), function(x)
        abs(x)), c(1, 2), function(x)
          x ** thresh)
  }
  
  # By convention, diagonal of an adjacency matrix should be all 0's
  results[cbind(1:nrow(results), 1:nrow(results))] <- 0
  
  # name the columns and rows of the adjacency matrix
  rownames(results) <- colnames(results) <- rownames(df)
  
  # Print and return results
  if (verbose) {
    print(results)
  }
  
  return(results)
  
} # End adjMatrix function
