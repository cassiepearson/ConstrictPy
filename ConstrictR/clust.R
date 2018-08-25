# Clustering Function
#           Currently only heirarchical clustering
# Description: Clustering program for dataframe objects
# Statistics:
# Required Parameters: df: dataframe
# Optional Parameters: k: number of clusters, distance: distance metric, linkage: linkage criteria,
#     repeat: repeat clustering to gain more accurate results, column: column major, verbose: print results

clust <- function(df, k=Inf, distance="euclidean", linkage="avg", repeat=FALSE, column=TRUE, verbose=FALSE) {

  # Set distance metic for calculations
  if(distance == "euclidean"){
    dist_metric <- function(a, b) {
      sqrt(sum(((df[a,i] - df[b,i])^2), i==1, ncol(df)))
      }}
  elseif(distance == "euclid_square"){
     dist_metric <- function(a, b) {
        #sum((df[a,i] - df[b,i])^2), i==1, ncol(df))
       }}
  elseif(distance == "manhattan"){
    dist_metric <- function(a, b) {
      sum(abs(df[a,i] - df[b,i]), i==1, ncol(df))
      }}


  # Set linkage criteria
  if(linkage == "average"){
    link_crit <- function(clust_a, clust_b) {
      sum(sum(dist_metric(clust_a[i], clust_b[j]), j==1, length(clust_b)), i==1, length(clust_a)) * (1 / ((length(clust_a)) * (length(clust_a))))
      }}
  elseif(distance == "single"){
    link_crit <- function(clust_a, clust_b) {...}}
   elseif(distance == "complete"){
     link_crit <- function(clust_a, clust_b) {...}}


   # Create an distance matrix
   dist_matrix <- matrix(data = NaN, nrow = nrows(df), ncol = nrows(df), dimnames = list(row.names(df), row.names(df)))


   # Create a list,
   # Each index of list is another list of the clusters durring a given itteration.
   # Clusters are character vectors
   # First index is just the distance matrix labels
   list <- as.list(rownames(dist_matrix))

   # Create an iterator tracker
   it <- 1


   # Cluster creator function


   # Heirarchical Clustering
   if(k == Inf) {
     # Find and enter distances into distance matrix
     for(x in 1:nrows(dist_matrix)) {
       for(y in 1:ncol(dist_matrix)) {
         if(x != y) {
           matrix[x,y] <- link_crit(dist_matrix[x], dist_matrix[y])
         }}}

     # Begin looping over distance matrix until we have 1 cluster
     while(length(list[it]) != 1) {
       # Find minimum distance and hold index values
       current <- which(dist_matrix == min(dist_matrix), arr.index = TRUE, useNames = TRUE)

       # Merge old clusters into a new character vector
       new <- c(list[it][current[1]], list[it][current[2]])
       # Sort the cluster
       sort(new)

       # Name new cluster
       label(new) <- paste("clust", it, sep="")

       # Delete previous rows and columns in distance matrix
       dist_matrix <- dist_matrix[c(-current[1], -current[2]), c(-current[1], -current[2])]

       # Run linkage for new cluster
       for(i in 1:rownames(dist_matrix)) {
         new_dist[i] <- link_crit(new, list[it][i])
       }

       # Add NaN to end of distance cluster vector
       new_dist <- c(new_dist, NaN)

       # Bind new vector to matrix
       dist_matrix <- rbind(dist_matrix, label(new) = new_dist)
       dist_matrix <- cbind(dist_matrix, label(new) = new_dist)

       # Incrament iterator
       it <- it+1

       # Insert new data into list
       list[it] <- rownames(dist_matrix)

       } # End Loop
     } # End Heirarchical clustering
   } # End function