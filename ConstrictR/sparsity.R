# Sparsity Function
# 
# Description: Calculate the sparsity of a dataframe. Sparsity is the percentage of missing data in decimal form.
# Statistics: Sparsity
# Required Parameters: df: dataframe
# Optional Parameters: verbose: Change to true for printing returned results to console 

sparsity <- function(df,verbose=FALSE){
  # Find the number of
  count_zero = 0
  df_size = nrow(df) * ncol(df)
  for(i in 1:nrow(df)){
    for(j in 1:ncol(df)){
      if(df[i,j] == 0 || is.na(df[i,j]) || is.infinite(df[i,j])){
        count_zero = count_zero + 1
      }
    }
  }
  
  result <- count_zero / df_size
  
  # Print and return result
  if(verbose == TRUE){
    print(result)
  }
  return(result)
  
} # End sparse function