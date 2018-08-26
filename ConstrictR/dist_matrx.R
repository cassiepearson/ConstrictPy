# Distance Matrix Creation Function
#
# Description:
# Required Parameters: df: dataframe
# Optional Parameters: drected: Change to TRUE if graph is directed,
#                      verbose: Change to true for printing returned results to console

distMatrix <- function(df,
                       #directed = FALSE,
                       verbose = FALSE) {
  # Create a distance martix
  results <- matrix(data = NaN,
                    nrow = nrow(df),
                    ncol = nrow(df))
  
  distMetric <- setDist()
  
  # Create a matrix, then calculate distances
  if (!directed) {
    for (i in 1:nrow(df)) {
      for (j in 1:nrow(df)) {
        results[i, j] <- distMetric(df[i], df[j])
      }
    }
  }
  else {
    for (i in 1:nrow(df)) {
      for (j in 1:nrow(df)) {
        results[i, j] <- distMetric(df[i], df[j])
      }
    }
  }
  
  # Diagonal of a distance matrix should be 0's
  results[cbind(1:nrow(results), 1:nrow(results))] <- 0
  
  # Name the columns and rows of the distance matrix
  rownames(results) <- colnames(results) <- rownames(df)
  
  # Print and return results
  if (verbose) {
    print(results)
  }
  
  return(results)
  
} # End distMatrix function
