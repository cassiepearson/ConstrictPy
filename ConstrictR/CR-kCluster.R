# k-Means Clustering algorithm

# A bounds setup function
# Run K-means once first:
# 1. To get inital distances for all points,
# 2. To get clusters into better positions over seeding, expect large movement early
# 3. To setup bounds for geometric reasoning
boundSetup <- function() {
  # 1st: Calculate the distances to all the centroids
  kMEnv$dist[which(is.nan(kMEnv$dist))] <-
    apply(cbind((((which(is.nan(kMEnv$dist)) - 1) %% NROW(df)
    ) + 1), (((which(is.nan(kMEnv$dist)) - 1) %/% NROW(df)
    ) + 1)), 1, function(x) {
      sum((df[x[1], ] - kMEnv$centrds[x[2],]) ^ 2)
    })
  
  # 2nd: Move the centroids
  # Find the minimum distance from a data point to a cluster
  kMEnv$closeCent <-
    apply(kMEnv$dist, 1, which.min)
  # Get vector sum of the assigned datapoints and number of assignments
  for (c in 1:k) {
    if (is.vector(df[(kMEnv$closeCent == c), ]))
      kMEnv$sums[c, ] <- df[(kMEnv$closeCent == c), ]
    else
      kMEnv$sums[c, ] <- colSums(df[which(kMEnv$closeCent == c), ])
    kMEnv$nod[c] <-
      length(kMEnv$closeCent[kMEnv$closeCent == c])
    
    kMEnv$centrds[c, ] <- kMEnv$sums[c, ] / kMEnv$nod[c]
  }
  # 3rd: Bounds & Grouping
  ### centroidDistances <-
  # upper bound
  kMEnv$uper <- kMEnv$dist[cbind(NROW(df), kMEnv$closeCent)]
  # lower
  for (i in 1:NROW(df)) {
    kMEnv$lwer[i] <- min(kMEnv$dist[i, ][-kMEnv$closeCent[i]])
  }
} # done with initializations and setup


# K-Means single iteration.
# Repeat recursively until convergence...
kClustering <- function(recur)  {
  # Get distances between neighbor centroids
  centNeigh <- matrix(data = NaN,
                      nrow = k,
                      ncol = k)
  nMin <- double(k)
  for (x in 1:k) {
    for (y in 1:k) {
      if (x == y) {
        centNeigh[x, y] <- Inf
        next()
      }
      centNeigh[x, y] <-
        ((sum((kMEnv$centrds[x,] - kMEnv$centrds[y, ]) ^ 2
        )) / 2)
    }
    nMin <- min(centNeigh[x, ])
  }
  pcBall <- 1:NROW(df)
  for (i in 1:NROW(df)) {
    pcBall[i] <- nMin[kMEnv$closeCent[i]]
  }
  boundFilter <- pmax.int(pcBall, kMEnv$lwer)
  failedPoints <- which(boundFilter < kMEnv$uper)
  # can skip intermediate variables?
  # For data points that fail the upper bound filter, update the upper bound
  if (any(boundFilter < kMEnv$uper)) {
    kMEnv$uper[failedPoints] <-
      sapply(failedPoints, function(x) {
        sum((df[x,] - kMEnv$centrds[kMEnv$closeCent[x], ]) ^ 2)
      })
  }
  
  # If all the datapoints are in the best clustering positions
  # or we have run k-Means 250 times, then end k-means clustering
  if (all(boundFilter > kMEnv$uper))
    print(paste("best bounds, no filter at ", recur))###testing bounds
  if (recur > 250)
    return()
  
  # Hold index of data points that fail the upper bound test
  failedPoints <- which(boundFilter < kMEnv$uper)
  # And hold old assignment values
  #old <-
  test <- kMEnv$closeCent
  # Run cluster distance calculations on those data points
  dist2All(failedPoints)
  
  # If no points changed their respective cluster assignment
  if (all(test == kMEnv$closeCent)) {
    print(paste("no change", recur))
    return()
  }
  # Otherwise we need to change the clustering information
  #cChanged(old)
  moveCents()
  updateBounds()
  
  # Remove the old information
  rm(boundFilter)
  rm(centNeigh)
  rm(nMin)
  rm(pcBall)
  rm(old)
  # Recursively call clustering
  return(kClustering(recur + 1))
}