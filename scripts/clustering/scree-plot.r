# Demo from: https://rpubs.com/GourabNath/Loopfunctionapplications

library(R.matlab)
library(plotrix)

k.max = 100

data = t(readMat("output00000000_cells_physicell.mat")$cells)
#data = t(readMat("Physicell/output/output00000000_cells_physicell.mat")$cells)
data <- data[!(data [,6]==2),]
data.c = data[,c(2,3,6)]


WSS. <- sapply(1:k.max, function(i){return(kmeans(data.c, centers = i)$tot.withinss)})

# Plot scree plot
plot(1:k.max, WSS., type="l", xlab = "No. of clusters", ylab = "Total WSS", main = "Scree Plot")



#############################################
#                                           #
#       Generate line plot with time vs.    #
#       WSS for different k                 #
#                                           #
#############################################

# Zero setup variables and load files matching expression
k.min = 8
k.max = 20
files <- list.files(pattern = "cells_physicell.mat$")

#First make matrix with rows being files and columns being WSS for different k
run =  matrix(0, nrow=length(files), ncol=(k.max-k.min + 1) ) 

# Second populate table
for(i in files) {
  data = t(readMat(i)$cells)
  data <- data[!(data [,6]==2),]
  data.c = data[,c(2,3)]
  
  WSS. <- sapply(k.min:k.max, function(j){return(kmeans(data.c, centers = j, iter.max=30)$tot.withinss)})
  
  index = as.integer(substr(i, 7, 14)) + 1
  
  run[index,] = WSS.
}

# Generate plot
matplot(run, type = c("l"),pch=1, col = rainbow(k.max)[k.min:k.max], xlab = "Output #", ylab = "Total WSS", main = "Model 3 WSS over time for different k")
legend("topleft", legend = k.min:k.max, col=rainbow(k.max)[k.min:k.max], pch=20, ncol = 2) # optional legend




#############################################
#                                           #
#       Generate line plot with time vs.    #
#       % A in each cluster                 #
#                                           #
#############################################

# Zero setup variables and load files matching expression
k.min = 20
k.max = 20
files <- list.files(pattern = "cells_physicell.mat$")

#First make matrix with rows being files and columns being WSS for different k
total_percents =  matrix(0, nrow=length(files), ncol=(k.max-k.min + 1) ) 

# Second populate table
for(i in files) {
  data = t(readMat(i)$cells)
  data <- data[!(data [,6]==2),]
  data.c = data[,c(2,3)]
  
  WSS. <- sapply(k.min:k.max, function(j) {
    data.t <- data.frame("cluster"=kmeans(data.c, centers = j, iter.max=30)$cluster, "type"=data[,6], "count"=rep(1, length(data[,1])))
    r = as.data.frame.matrix(xtabs(formula=count~cluster + type, data=data.frame("cluster"=kmeans(data.c, centers = j)$cluster, "type"=data[,6], "count"=rep(1, length(data[,1])))))
    r = 100 * r/rowSums(r)
    
    return(sum(abs(r[,1] - r[,2])/j))
  })
  
  index = as.integer(substr(i, 7, 14)) + 1
  
  total_percents[index,] = WSS.
}

# Generate plot
matplot(total_percents, type = c("l"),pch=1, col = rainbow(k.max)[k.min:k.max], xlab = "Output #", ylab = "% segregated", main = "Model 3 percent segregated over time for different k")
 legend("topleft", legend = k.min:k.max, col=rainbow(k.max)[k.min:k.max], pch=20, ncol = 2) # optional legend





