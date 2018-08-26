# All Pairs Shortest Path
#
# Vesrion 0.0.1:  Implementation of the Floyd Warshall Algorithm
# Required Parameters:
# Optional Parameters:

aPairsShortest <- function() {
  
  floydWarshall <- function(env = parent.frame()) {
    shortPath <- c$distMatrix
    
    for (k in nrow(c$distMatrix)) {
      for (i in nrow(c$distMatrix)) {
        if (i == k)
          next()
        for (j in ncol(c$distMatrix)) {
          if (j == k)
            next()
          # Check if k is on a shorter path
          if (shortPath[i, k] != Inf &&
              shortPath[k, j] != Inf &&
              shortPath[i, k] + shortPath[k, j] < shortPath[i, j])
            shortPath[i, j] <<- shortPath[i, k] + shortPath[k, j]
        }
      }
    }
  }
  
  
  return(shortPath)
}