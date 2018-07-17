all: text show

text:
	python3 build.py

show:
	cat output.txt

clean:
	rm -f output.txt
