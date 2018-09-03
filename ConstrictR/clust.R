# Clustering Function
#           Currently only heirarchical clustering
# Description: Clustering program for dataframe objects
# Statistics:
# Required Parameters: df: dataframe
# Optional Parameters: k: number of clusters, distance: distance metric, linkage: linkage criteria,
#     repeat: repeat clustering to gain more accurate results, column: column major, verbose: print results


# Load kmeans function file
source("CR-kMean.R")

clust <-
  function(df,
           k        = Inf,
           iter     = 1,
           linkage  = "avg",
           column   = TRUE,
           verbose  = FALSE,
           ...) {
    # Coerce data.frame to matrix
    df <- data.matrix(df)
    
    if (k == Inf) {
      # Set distance matrix
      distMetric <- setDist(distance = "euclidean")
        # Load agglomerative hierarcical function file
        source("hierarchical.R")
      # Run hierarchical clustering
      return(hierarchical())
    }
    else if (k < Inf) {
      # Set distance matrix
      distMetric <- setDist(distance = "euclid_square")
      # Run kmeans function
      return(cRKMPP(iter), ...)
    }
    
    return()
  } # End function