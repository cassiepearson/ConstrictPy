# A bounds setup function

# Run K-means once first:
# 1. To get inital distances for all points,
# 2. To get clusters into better positions over seeding, expect large movement early
# 3. To setup bounds for geometric reasoning
boundSetup <- function() {
  # 1st: Calculate the distances to all the centroids
  kMEnv$dist[which(is.nan(kMEnv$dist))] <-
    apply(cbind((((
      which(is.nan(kMEnv$dist)) - 1
    ) %% 500) + 1), (((
      which(is.nan(kMEnv$dist)) - 1
    ) %/% 500) + 1)), 1, function(x) {
      sum((df[x[1], ] - kMEnv$centrds[x[2],]) ^ 2)
    })
  
  # 2nd: Move the centroids
  # Find the minimum distance from a data point to a cluster
  kMEnv$closeCent <-
    apply(kMEnv$dist, 1, which.min)
  # Get vector sum of the assigned datapoints
  for (i in 1:k) {
    kMEnv$sums[i,] <- colSums(df[(kMEnv$closeCent == i), ])
  }
  # Get number of assignments
  for (i in 1:k) {
    kMEnv$nod[i] <- length(kMEnv$closeCent[kMEnv$closeCent == i])
  }
  # Move the centroids
  for (i in 1:k) {
    kMEnv$centrds[i,] <- 
      kMEnv$sums[i, ] /
      kMEnv$nod[i]
  }
  
  # 3rd: Bounds & Grouping
  ### centroidDistances <-
  # upper bound
  kMEnv$uper <- kMEnv$dist[cbind(1:500, kMEnv$closeCent)]
  # lower
  for (i in 1:NROW(df)) {
    kMEnv$lwer[i] <- min(kMEnv$dist[i, ][-kMEnv$closeCent[i]])
  }
} # done with initializations and setup