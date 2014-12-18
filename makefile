CC = gcc 
#Using -Ofast instead of -O3 might result in faster code, but is supported only by newer GCC versions
CFLAGS = -lm -pthread -O2 -march=native -Wall -funroll-loops -Wunused-result

all: word2vec word2phrase distance distance-io word-analogy compute-accuracy txtvec2bin binvec2txt

word2vec : word2vec.c
	$(CC) word2vec.c -o word2vec $(CFLAGS)
word2phrase : word2phrase.c
	$(CC) word2phrase.c -o word2phrase $(CFLAGS)
distance : distance.c
	$(CC) distance.c -o distance $(CFLAGS)
distance-io : distance.c
	$(CC) distance-io.c -o distance-io $(CFLAGS)
word-analogy : word-analogy.c
	$(CC) word-analogy.c -o word-analogy $(CFLAGS)
compute-accuracy : compute-accuracy.c
	$(CC) compute-accuracy.c -o compute-accuracy $(CFLAGS)
txtvec2bin : txtvec2bin.c
	$(CC) txtvec2bin.c -o txtvec2bin $(CFLAGS)
binvec2txt : binvec2txt.c
	$(CC) binvec2txt.c -o binvec2txt $(CFLAGS)

clean:
	rm -rf word2vec word2phrase distance distance-io word-analogy compute-accuracy txtvec2bin binvec2txt
