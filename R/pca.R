# dat <- read.table("vector-wiki-10word-20141209.csv", sep="\t", row.names=1)
dat <- read.table("output/vector-wiki-4word-20141210.csv", sep="\t", row.names=1)
normalize_vectors <- function(d) {
  for (i in 1:nrow(dat)) {
  	dat[i,] <- dat[i,] / sqrt(sum(dat[i,] * dat[i,]))
  }	
}
# Comment the line below to get original (unnormalized) vectors.
normalize_vectors(dat)
pca <- prcomp(dat)
plot(pca$x, xlim=c(-2, 1.5), ylim=c(-2, 1))  # print the first two PCA dimensions
text(pca$x[,1], pca$x[,2], rownames(dat), pos=3)  # Add text labels
