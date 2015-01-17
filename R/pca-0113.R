input_prefix <- '~/word2vec/output/10w-vectors/vector-wiki-10word-20150113-csv-'
output_prefix <- '~/word2vec/output/10w-pcas/wiki-10word-20150113-'

normalize_vectors <- function(d) {
  for (i in 1:nrow(d)) {
    d[i,] <- d[i,] / sqrt(sum(d[i,] * d[i,]))
  }
  return(d)
}

for (i in 0:10) {
  filename <- paste(input_prefix, i, sep='')
  dat <- read.table(filename, sep="\t", row.names=1)
  dat <- normalize_vectors(dat)
  pca <- prcomp(dat)
  pngname <- paste(output_prefix, i, '.png', sep='')
  png(pngname)
  plot(pca$x, xlim=c(min(pca$x[,1]-.2), max(pca$x[,1]+.2)), ylim=c(min(pca$x[,2]-.2), max(pca$x[,2]+.2)))  # print the first two PCA dimensions
  text(pca$x[,1], pca$x[,2], rownames(dat), pos=3)  # add text labels
  dev.off()
}
