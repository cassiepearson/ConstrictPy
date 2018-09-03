# Agglomerative Heirarchical Clustering


hierarchical <- function(linkage = "average") {
  # Set linkage criteria
if (linkage == "average") {
  linkCrit <- function(clustA, clustB) {
    sum(sum(distMetric(df[clustA, ], df[clustB, ]))) * (1 / ((length(clustA)) * (length(clustB))))
  }
} else {
  stop("linkage arg not correct")
}
# else if (linkage == "single") {
#   linkCrit <- function(clustA, clustB) {
#     #min(dist_metric(clustA[], clustB[]))
#   }
# }
# else if (linkage == "complete") {
#   linkCrit <- function(clustA, clustB) {
#     #max(dist_metric(clustA[], clustB[]))
#   }
# }

  # Create an empty distance matrix
  if (column) {
    distMatrix <-
      matrix(
        data = NaN,
        nrow = nrow(df),
        ncol = nrow(df),
        dimnames = list(row.names(df),
                        row.names(df))
      )
  } else {
    distMatrix <-
      matrix(
        data = NaN,
        nrow = ncol(df),
        ncol = ncol(df),
        dimnames = list(col.names(df),
                        col.names(df))
      )
    }

  # Create a matrix to return values
  returnMatrix <-
    matrix(
      NaN,
      nrow = nrow(distMatrix),
      ncol = (nrow(distMatrix) - 1),
      dimnames = list(rownames(distMatrix), paste("Iteration", 1:NCOL(df), sep = " "))
    )

  # Enter initial values into new data structures:
  # First index in return matrix is just the distance matrix labels
  returnMatrix[,1] <- rownames(distMatrix)

  # Find and enter distances into distance matrix
  for (x in 1:nrows(distMatrix)) {
    for (y in 1:ncol(distMatrix)) {
      # Distances are symmetric
      if (x > y) {
        distMatrix[x, y] = distMatrix[y, x]
      }
      # Keep distance from self at NaN
      else if(x == y) {
        next
      }
      # Get distance between points by calling linkage function
      else if(x < y) {
        distMatrix[x, y] <-
          linkCrit(colnames(distMatrix)[x], rownames(distMatrix)[y])
      }
    }
  }

  # Reset iterator tracker
  iter <- 1

  # Begin looping over distance matrix until we have 1 cluster
  while (length(unique(as.vector(returnMatrix[, iter]))) != 1) {
    # Find minimum distance and hold index values
    # This call returns only 1st location found when treating a matrix like a vector(?)
    minDistInd <-
      as.vector(arrayInd(which.min(distMatrix), dim(distMatrix)))

    # Get new cluster from previous cluster names from minimum distance indices
    newCluster <-
      which(returnMatrix[, ncol(returnMatrix)] == rownames(distMatrix[minDistInd, ]),
            arr.ind = TRUE)

    newName <- paste("clust", iter, sep = "-")

    # Duplicate the last column of the return matrix
    if (iter > 1) {
      returnMatrix[, iter - 1] <- returnMatrix[, iter]
    }
    # Replace cluster names for rows matching desired points
    for (name in rownames(newCluster)) {
      returnMatrix[name, paste("Iteration", iter, sep = " ")] <-
        paste("clust", iter, sep = "-")
    }

    # Delete previous rows and columns in distance matrix
    distMatrix <- distMatrix[-minDistInd,-minDistInd]
    # Add row and column to distance matrix to hold new distance values
    distMatrix <- cbind(distMatrix, NaN)
    distMatrix <- rbind(distMatrix, NaN)
    # Name the new row and column
    colnames(distMatrix)[ncol(distMatrix)] <- newName
    rownames(distMatrix)[nrow(distMatrix)] <- newName

    # Updated new row and column with distances to other clusters
    for (cn in 1:colnames(distMatrix)) {
      if (cn == newName) {
        break
      }
      # Find which points are in a cluster
      otherClust <-
        which(returnMatrix[, ncol(returnMatrix)] == cn,
              arr.ind = TRUE,
              useNames = TRUE)
      # Run linkage between the new cluster and current cluster in loop
      distMatrix[cn, nrow(distMatrix)] <-
        linkCrit(rownames(newCluster), rownames(otherClust))
      # Since distances are symmetric
      distMatrix[nrow(distMatrix), cn] <-
        distMatrix[cn, nrow(distMatrix)]
    }


    # Increment iterator
    iter <- iter + 1

  } # End Loop

  # Return list of iterations of clustering
  return(list)

# End hierarchical clustering function
}