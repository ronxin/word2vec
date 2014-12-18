// Convert text-format vector into binary format.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

const long long max_size = 2000;         // max length of strings
const long long N = 40;                  // number of closest words that will be shown
const long long max_w = 50;              // max length of vocabulary entries

int main(int argc, char **argv) {
  FILE *f;
  char file_name[max_size], output_file_name[max_size];
  // size is the size of the hidden layer
  long long words, size, a, b;
  float *M;
  char *vocab;
  if (argc < 3) {
    printf("Usage: ./binvec2txt <BIN_INPUT> <TXT_OUTPUT>\nwhere BIN_INPUT contains word projections in the BINARY FORMAT\n");
    return 0;
  }
  strcpy(file_name, argv[1]);
  strcpy(output_file_name, argv[2]);
  f = fopen(file_name, "rb");
  if (f == NULL) {
    printf("Input file not found\n");
    return -1;
  }
  fscanf(f, "%lld", &words);
  fscanf(f, "%lld", &size);
  vocab = (char *)malloc((long long)words * max_w * sizeof(char));
  M = (float *)malloc((long long)words * (long long)size * sizeof(float));
  if (M == NULL) {
    printf("M: Cannot allocate memory: %lld MB    %lld  %lld\n", (long long)words * size * sizeof(float) / 1048576, words, size);
    return -1;
  }
  
  // Read vectors.
  for (b = 0; b < words; b++) {
    fscanf(f, "%s", vocab + b * max_w);
    for (a = 0; a < size; a++) fscanf(f, "%f", &M[a + b * size]);
  }
  fclose(f);

  FILE *fo = fopen(output_file_name, "wb");
  fprintf(fo, "%lld %lld\n", words, size);
  for (a = 0; a < words; a++) {
    fprintf(fo, "%s ", vocab + a * max_w);
    for (b = 0; b < size; b++) fwrite(&M[a * size + b], sizeof(float), 1, fo);
    fprintf(fo, "\n");
  }
  return 0;
}
