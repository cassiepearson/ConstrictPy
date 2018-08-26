# Helper functions for k-Means Clustering

# Helper function to move the centers and calculate distance moved
moveCents <- function() {
  # Save old centers
  oldCents <- kMEnv$centrds
  
  # Move the centroids
  for (c in 1:k) {
    if (is.vector(df[(kMEnv$closeCent == c),]))
      kMEnv$sums[c, ] <- df[(kMEnv$closeCent == c),]
    else
      kMEnv$sums[c,] <- colSums(df[which(kMEnv$closeCent == c),])
    kMEnv$nod[c] <-
      length(kMEnv$closeCent[kMEnv$closeCent == c])
    
    kMEnv$centrds[c,] <- kMEnv$sums[c,] / kMEnv$nod[c]
  }
  #Speed test the difference
  #kMEnv$centrds <-
  #  sapply(1:k
  #        function(j) {
  #          kMEnv$sums[j, ] /
  #            sum(length(kMEnv$closeCent[kMEnv$closeCent == j]))
  #        })
  
  # Calculate drift
  for (i in 1:k) {
    kMEnv$drift[i] <-
      sum((oldCents[i, ] - kMEnv$centrds[i, ]) ^ 2)
  }
  
  # Remove old clustering data and return
  rm(oldCents)
  return()
}

# Helper function to update the bounds
updateBounds <- function() {
  # Get index location of the largest mover.
  bigMover <- which.max(kMEnv$drift)
  
  kMEnv$uper <-
    kMEnv$uper + kMEnv$drift[matrix(c(1:NROW(df), kMEnv$closeCent), ncol = 2)[,2]]
  ### Faster than?
  
  # Decrease the lower bound by the distance of the bigest mover
  kMEnv$lwer[kMEnv$closeCent != bigMover] <-
    kMEnv$closeCent[kMEnv$closeCent != bigMover] - kMEnv$drift[bigMover]
  # If the closest centroid was the bigest mover,
  # then decrease lower bound by second biggest mover
  ###### why?
  kMEnv$lwer[kMEnv$closeCent == bigMover] <-
    kMEnv$closeCent[kMEnv$closeCent == bigMover] - max(kMEnv$drift[-bigMover])
  
  # remove biggest mover variable then return
  rm(bigMover)
  return()
}

# Helper function to calculate distances to centroids
dist2All <- function(cantAvoid) {
  # cantAvoid is a vector of indexes for the datapoints we need to calculate
  kMEnv$dist <-
    matrix(
      apply(cbind(
        rep.int(1:NROW(df), k), rep(1:k, each = NROW(df))
      ), 1, function(x) {
        sum((df[x[1], ] - kMEnv$centrds[x[2],]) ^ 2)
      }),
      nrow = NROW(df),
      ncol = k
    )
  
  #kMEnv$dist[cantAvoid, ] <-
  
  
  # Find the minimum distance from a data point to a cluster
  kMEnv$closeCent[cantAvoid] <-
    apply(kMEnv$dist[cantAvoid,], 1, which.min)
  
  # Hold the distance values, since it is the minimum
  kMEnv$uper[cantAvoid] <- 
    kMEnv$dist[cbind(cantAvoid, kMEnv$closeCent[cantAvoid])]
  
  # Find the minimum distance from a data point to the second closest cluster
  kMEnv$lwr[cantAvoid] <-
    vapply(1:length(cantAvoid), function(i) {
      min(kMEnv$dist[cantAvoid[i],][-kMEnv$closeCent[cantAvoid[i]]])
    }, double(1))
  
}

# Helper function to change cluster math
#cChanged <- function(change)
