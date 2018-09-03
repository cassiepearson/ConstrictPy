# Centrality Function
# 
# Description: "Parent Frame" for centrality functions
# Statistics: 
# Required Parameters: df: dataframe
# Optional Parameters: type: type of centrality measure
#                      ...

cent <- function(df,
                 type = "all",
                 ...) {
  source(degree_centrality.R)
  
  c <- new.env()
  # Create an Adjacency Matrix of the dataframe
  c$adjMatrx <- adjMatrix(df)
  # Create a Distance Matrix of the dataframe
  c$distMatrx <- distMatrix(df)
  # Create a Topological Overly Matrix of the dataframe
  c$topOMatrx <- topOMatrix(df)
  
  # Create a Shortest Path Matrix of the dataframe, expected that dist matrix exists in environment
  c$sPMatrx <- aPairsShortest()
  
  # Degree Centrality
  c$degree <- degCent()
  # Closeness Centrality
  c$close <- closCent()
  # Betweenness Centrality
  ###c$between <- btwCent()
  # Eigenvector Centrality
  ###c$eigen <- eigCent()
  # Harmonic Centrality
  # Katz Centrality 
  
  # Print and return results
  if(verbose == TRUE){
    print(results)
  }
  
  rm(c)
  return(results)
  
} # End graph centrality