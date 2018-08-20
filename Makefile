all: text show
ru: textru showru

text:
	python3 build.py
textru:
	python3 build.py ru

show:
	cat output.txt
showru:
	cat output.ru.txt

clean:
	rm -f output.txt
