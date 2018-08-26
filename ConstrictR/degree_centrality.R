# Degree Centrality

degCent <- function(normalize = FALSE) {
  results <- vector(mode = "numeric",
                    length = nrow(c$adjMatrix))
  
  for (i in nrow(c$adjMatrix)) {
    for (j in ncol(c$adjMatrix)) {
      if (c$adjMatrix[i,j] == Inf || c$adjMAtrix[i,j] == 0)
        next()
      results[i] <<- results[i] + c$adjMAtrix[i,j]
    }
  }
  
  if (normalize == TRUE)
    results <<- results/(nrow(c$adjMatrix) - 1)
  
  return(results)
}