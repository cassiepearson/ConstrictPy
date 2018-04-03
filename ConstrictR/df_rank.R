# Dataframe Rank Wrapper Function
# 
# Description: Calculate the rank of values in each row or column of a dataframe using the built-in 
#              rank function.
# Statistics: Rank
# Required Parameters: df: dataframe
# Optional Parameters: na: how to handle na data, default is keep,
#                      method: ties method, default is average,
#                      column: Change to false if your table is organized row-wise,
#                      verbose: Change to true for printing returned results to console

df_rank <- function(df,na="keep",method="average",column=TRUE,verbose=FALSE){
    # Create a List object
    List <- list()
  
    # Iterate column or row-wise through the dataframe
    if(column == TRUE){
      
      # Iterate through each column
      for(i in 1:ncol(df)){
        # Obtain the column without indecies
        current_col <- unlist(df[i], use.names=FALSE)
        
        # Calculate the ranks for the column
        current <- rank(current_col,na,method)
        List[[i]] <- current
        
        # Set the column names of current and then append to results
        results_matrix = do.call(cbind, List)
        
      } # End for
      
    }else{
      
      # Iterate through each row
      for(i in 1:nrow(df)){
        # Obtain the row without indecies
        current_row <- unlist(df[i,], use.names=FALSE)
        
        # Calculate the ranks for the row
        current <- rank(current_row,na,method)
        List[[i]] <- current
        
        # Set the column names of current and then append to results
        results_matrix = do.call(cbind, List)  
        
      } # End for
      
    } # End if/else
    
    # Create a results dataframe
    results_df <- as.data.frame(results_matrix)
    colnames(results_df) <- colnames(df)
    
    
    # Print and return results
    if(verbose == TRUE){
      print(results_df)
    }
    return(results_df)
  
} # End df_rank function