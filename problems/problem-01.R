# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# 
# Bonus: Can you do this in one pass?

library(tidyverse)

key <- function(i) {
  as.character(i)
}

solution_01 <- function(l, k) {
  
  # Set the structure
  
  dict <- list()
  
  l_len <- l %>% 
    length()
  
  # Process first element
  
  l_item <- l[1]
  
  k_comp <- k - l_item
  
  dict[[key(k_comp)]] <- TRUE
  
  # Process every other element
  
  for (i in seq(2, l_len)) {
    l_item <- l[i]
    
    i_check <- dict[[key(l_item)]]
    
    if (!is.null(i_check) && i_check) { 
      
      print(str_c(l_item, 
                  " + ",
                  k - l_item))
       
      return (TRUE)
    }
    
    k_comp <- k - l_item
    
    dict[[key(k_comp)]] <- TRUE
  }
  
  return (FALSE)
}


















