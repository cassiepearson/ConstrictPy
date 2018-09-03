# Closeness Centrality

closCent <- function(normalize = FALSE) {
  results <- vector(mode = "numeric",
                    length = nrow(c$adjMatrix))
  
  for (i in nrow(c$distMatrix)) {
    for (j in ncol(c$distMatrix)) {
      if (c$distMatrix[i,j] == Inf || c$distMAtrix[i,j] == 0)
        next()
      results[i] <<- results[i] + c$distMAtrix[i,j]
    }
  }
  
  results <<- 1 / results
  
  if (normalize == TRUE)
    results <<- (nrow(c$distMatrix) - 1) / results
  
  return(results)
}