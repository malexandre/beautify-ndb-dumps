all:
	chmod +x ./beautify-ndb-dumps.py
	ln ./beautify-ndb-dumps.py /usr/bin/beautify-ndb-dumps

clean:
	chmod -x ./beautify-ndb-dumps.py
	rm /usr/bin/beautify-ndb-dumps