.PHONY: validate build clean

validate:
	python scripts/validate_cards.py

build: validate
	python scripts/build_anki.py

clean:
	rm -f dist/XGZ_Jazz_Arpeggios.apkg
