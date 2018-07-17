all: text

text:
	python3 build.py
clean:
	rm -f output.txt
