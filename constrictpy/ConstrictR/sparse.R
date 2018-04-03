# Sparse Function
#
# The most hotly and confusingly debated item including in this package. Used to determine if data is sparse, 
# by 'our' definition. A compromise was made between mathematics, data science, statistics, and bioinformatics.
# If an empty or zero row or column exists, then the matrix is sparse.
# 
# Description: Determine if the dataframe is sparse. Useful in implementing more efficient forms of 
#              specific analysis algorithms. Under 'our' definition, a dataframe is sparse if there is
#              a complete null, zero, or infinite row or column. For more detailed information on the
#              amount of missing information in a dataframe, see the sparsity function.
# Statistics: Sparse
# Required Parameters: df: dataframe
# Optional Parameters: verbose: Change to true for printing returned results to console 

sparse <- function(df,verbose=FALSE){
  # Default value for result is FALSE
  result <- FALSE
  
  # Check for a null or inf row or column
  row_na_check <- apply(df, 1, function(x) any(is.na(x) | is.infinite(x)))
  col_na_check <- apply(df, 2, function(x) any(is.na(x) | is.infinite(x)))
  
  # Check for a zero row or column
  row_zero_check <- apply(df, 1, function(x) all(x == 0))
  col_zero_check <- apply(df, 2, function(x) all(x == 0))
  
  # Determine if sparse
  if(row_na_check || row_zero_check || col_na_check || col_zero_check){
    result <- TRUE
  } # End of conditional
  
  # Print and return result
  if(verbose == TRUE){
    print(result)
  }
  return(result)
  
} # End sparse function