# Function to set and reset environment variables
resetVars <- function() {
  # Initialize matrix of centroid locations size=k*d
  kMEnv$centrds <-
    matrix(data = NaN,
           nrow = k,
           ncol = NCOL(df))
  # Initialize matrix of distances from all centroids; size=n*k
  kMEnv$dist <-
    matrix(data = NaN,
           nrow = NROW(df),
           ncol = k)
  
  # Vector of assigned clusters
  kMEnv$closeCent <-
    vector(mode = "numeric",
           length = NROW(df))
  
  # Vector sums of all points in a cluster
  kMEnv$sums <-
    matrix(data = NaN,
           nrow = k,
           ncol = NCOL(df))
  # Number of points assigned to a cluster
  kMEnv$nod <-
    vector(mode = "numeric",
           length = k)
  
  # Find neighbor centroids, and distances
  
  # Initialize an invalid bounds vectors
  kMEnv$drift <-
    vector(mode = "numeric",
           length = k)
  kMEnv$uper <-
    vector(mode = "numeric",
           length = NROW(df))
  kMEnv$lwer <-
    vector(mode = "numeric",
           length = NROW(df))
}

# Setup function
setup <- function(cacheOF) {
  # Setup environmental variables to hold data through iterations
  if (cacheOF) {
    ### need getters and setters
  }
  # Or, to save memory, call functions that return the neccessary data
  else {
    
  }
  return()
}