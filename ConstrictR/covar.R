# Covariance Wrapper Function
# 
# Description: Calculate the covariance of values in a dataframe using the built-in covariance function.
# Statistics: Covariance
# Required Parameters: df: dataframe
# Optional Parameters: method: Change to desired missing data handling method, complete is default,
#                      verbose: Change to true for printing returned results to console 

covar <- function(df,method="complete.obs",verbose=FALSE){
  # Conditional for different types of correlation, default is pearson, if error in type name, runs pearson
  results <- cov(df,use=method)
  
  # Print and return results
  if(verbose == TRUE){
    print(results)
  }
  return(results)
  
} # End corr function