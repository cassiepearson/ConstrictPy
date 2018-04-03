# Correlation Wrapper Function
# 
# Description: Calculate the correlation of values in a dataframe using the built-in correlation function.
# Statistics: Pearson, Spearman, and Kendall-Tau correlation
# Required Parameters: df: dataframe
# Optional Parameters: type: Change to desired correlation method, pearson is default,
#                      verbose: Change to true for printing returned results to console

corr <- function(df,type='pearson',verbose=FALSE){
  # Conditional for different types of correlation, default is pearson, if error in type name, runs pearson
  if(type == "kendall"){
    # Kendall Tau Correlation
    results <- cor(df, use="complete.obs", method="kendall")
    
  } else if(type == "spearman") {
    # Spearman Correlation
    results <- cor(df, use="complete.obs", method="spearman")
    
  } else {
    # Pearson Correlation
    results <- cor(df, use="complete.obs", method="pearson")
    
  } # End of conditional

  
  # Print and return results
  if(verbose == TRUE){
    print(results)
  }
  return(results)
  
} # End corr function