# Functions for selecting seeds by K-Means++ Method

# Find another way, don't need 2 env vars..
seedingData <- new.env()

# Recursive seeding function
sPP <- function(m) {
  # Select datapoint at a probability proportional to distance
  #   from nearest centroid
  seedingData$selected <-
    sample(1:length(seedingData$shortIndexVector),
           1,
           prob = seedingData$probabilityVector)
  # Save the new centroid
  kMEnv$centrds[m,] <-
    df[seedingData$shortIndexVector[seedingData$selected],]
  
  # If there are more centroids to be selected
  if (m < k) {
    # Remove data point from index selection vector
    seedingData$shortIndexVector <-
      seedingData$shortIndexVector[-seedingData$selected]
    
    # Get new minimum distance,
    #   either from the new centroid or from previous centroids
    kMEnv$dist[seedingData$shortIndexVector, m] <-
      apply(df[seedingData$shortIndexVector, ], 1, function(x) {
        sum((x - kMEnv$centrds[1,]) ^ 2)
      })
    
    # Remove the selected point from the probability distance vector
#    seedingData$probabilityDistances <-
#      seedingData$probabilityDistances[-seedingData$selected]
    # keep only the minimumdistances for probability calculations
    seedingData$probabilityDistances <-
      pmin.int(kMEnv$dist[seedingData$shortIndexVector, m],
               seedingData$probabilityDistances[-seedingData$selected])
    
    # Update the probability vector for available points
    seedingData$probabilityVector <-
      (seedingData$probabilityDistances ^ 2) /
      sum(seedingData$probabilityDistances ^ 2)
    
    #recursively call seeding function
    sPP(m + 1)
  }
  return()
}


# Initialization and 1st seed selection
kMPPSeed <- function() {
  # Create a vector of data points to choose from
  #   1st: Shrink the dataframe,
  #        this should reduce chances of outliers being chosen
  #        this will also reduce the number of distance calculations needed
  seedingData$shortIndexVector <-
    order(sample(1:NROW(df), as.integer(0.6 * NROW(df)), replace = FALSE))
  # Assign a first centroid at random
  seedingData$selected <-
    sample(1:length(seedingData$shortIndexVector), 1)
  kMEnv$centrds[1,] <-
    df[seedingData$shortIndexVector[seedingData$selected],]
  
  # Remove chosen point to ensure sampling without replacement
  seedingData$shortIndexVector <-
    seedingData$shortIndexVector[-seedingData$selected]
  
  # Get distances to newly created cluster
  kMEnv$dist[seedingData$shortIndexVector, 1] <-
    # is apply the right function?
    apply(df[seedingData$shortIndexVector,], 1, function(x) {
      sum((x - kMEnv$centrds[1,]) ^ 2)
    })
  # hold the distances for future operations..
  seedingData$probabilityDistances <-
    kMEnv$dist[seedingData$shortIndexVector, 1]
  # Calculate probablitit based on distance to clusters
  seedingData$probabilityVector <-
    (seedingData$probabilityDistances ^ 2) /
    sum(seedingData$probabilityDistances ^ 2)
  
  # k should be greater than 1, so we look for the second centroid
  sPP(2)
  
  rm(seedingData)
  return()
  # return is supposed to garbage collect a weak refernces
}
