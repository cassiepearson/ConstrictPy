# Basic Dataframe Descirptive Statistics
#
# Description: Calculate the basic descriptive statistics of your dataframe.
# Statistics: min, max, range, median, mean, variance, standard deviation, and standard error
# Required Parameters: df: dataframe
# Optional Parameters: column: Change to false if your table is organized row-wise,
#                      verbose: Change to true for printing returned results to console

desc_stats <- function(df,column=TRUE,verbose=FALSE){
  
  # Create the output dataframe
  results <- data.frame("min" = double(),
                        "max" = double(),
                        "range" = double(),
                        "median" = double(),
                        "mean" = double(),
                        "var" = double(),
                        "sd" = double(),
                        "se" = double())
  colnames(results) <- c("min","max","range","median","mean","var","sd","se")
  
  # Iterate column or row-wise through the dataframe
  if(column == TRUE){
    
    # Iterate through each column
    for(i in 1:ncol(df)){
      # Obtain the column without indecies
      current_col <- unlist(df[i], use.names=FALSE)

      # Create a new dataframe to calculate the statistics for the column
      current <- data.frame(min(current_col),
                            max(current_col),
                            range(current_col),
                            median(current_col),
                            mean(current_col),
                            var(current_col),
                            sd(current_col),
                            sd(current_col) / sqrt(nrow(df)))
      
      # Set the column names of current and then append to results
      colnames(current) <- colnames(results)
      results <- rbind(results, current)  
      
    } # End for
    
  }else{
    
    # Iterate through each row
    for(i in 1:nrow(df)){
      # Obtain the row without indecies
      current_row <- unlist(df[i,], use.names=FALSE)
      
      # Create a new dataframe to calculate the statistics for the row
      current <- data.frame(min(current_row),
                            max(current_row),
                            range(current_row),
                            median(current_row),
                            mean(current_row),
                            var(current_row),
                            sd(current_row),
                            sd(current_row) / sqrt(ncol(df)))
      
      # Set the column names of current and then append to results
      colnames(current) <- colnames(results)
      results <-rbind(results, current)  
      
    } # End for
    
  } # End if/else

  # Print and return results
  if(verbose == TRUE){
    print(results)
  }
  return(results)
  
} # End desc_stats function