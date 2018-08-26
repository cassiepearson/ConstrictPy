# K-Means clustering

#------------------------------------

# Get neccessary sub-functions for running k-Means Clustering
source("CR-kSeeding.R")
source("CR-kCluster.R")
source("CR-kCSetup.R")
source("CR-kHelp.R")

# Create an environment to hold clustering data through recursive calls
kMEnv <- new.env()

# Functional call of a single iteration of k-Means clustering
kSingle <- function() {
  # Get k Seeds
  kMPPSeed()
  # Initialize bounds
  boundSetup()
  # Run clustering
  kClustering(0)
}

# Delete environment variables and return the centroids
cleanup <- function() {
  best <- kMEnv$bestResults
  ### want to remove uneccessary variables, issues with rm call
  rm("kMEnv")
  return(best)
}

# Clustering function
cRKMPP <- function(nTimes, cached = TRUE) {
  # Setup function, cache data or have functional calls for data
  #setup() ----would move resetVars to inside this call
  
  # Set environment variables
  resetVars()
  
  # For holding best results through multiple clustering calls
  kMEnv$bestResults <-
    matrix(data = NaN,
           nrow = k,
           ncol = NROW(df))
  kMEnv$bestDiss <- 
    numeric(length = 1)
  
  ### Grouping vector  kMEnv$groups <-
  
  while (nTimes > 0) {
    kSingle()
    if (all(is.nan(kMEnv$bestResults))) {
      # Save the best results for later
      kMEnv$bestResults <- kMEnv$centrds
      # Get the dissimilarity; the sum of the intercluster variability
      # First update all the distances to the closest centroids
      
      # Finally hold the value
      kMEnv$bestDiss <- sum()
    }
    else if (nTimes > 1) {
      # Update the distances to the centroids
      kMEnv$dist[] <-
        apply(cbind(rep.int(1:NROW(df), k), rep(1:k, each = NROWS(df))),
              1, function(x) {sum((df[x[1], ] - kMEnv$centrds[x[2],]) ^ 2)
        })
      vNow <- 1:k
      # Get the sum of the variabilities
      for (v in 1:k) {
        vNow[v] <- sum(kMEnv$dist[whicch(kMEnv$closeCent == v),v])
      }
      thisDiss <- sum(vNow)
      if(thisDiss < kMEnv$bestDiss) {
        kMEnv$bestResults <- kMEnv$centrds
        kMEnv$bestDiss <- thisDiss
        
        nTimes <- nTimes - 1
        rm(thisDiss)
      } 
    }
    nTimes <- nTimes - 1
  }
  
  # Return K-Means cetroids
  return(cleanup())
} # End K-Means
